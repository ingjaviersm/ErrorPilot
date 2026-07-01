let reportData = null;

async function loadReport() {
  const response = await fetch("report.json");
  reportData = await response.json();

  const levels = reportData.summary.levels;
  const priorities = reportData.summary.priorities;

  document.getElementById("app").innerHTML = `

        <div class="row g-3 mb-4">

            ${card("Eventos", reportData.summary.total_events, "primary")}
            ${card("Archivos", reportData.summary.total_files, "secondary")}
            ${card("Tipos", reportData.summary.problem_types, "info")}
            ${card("Warnings", levels.Warning ?? 0, "warning")}
            ${card("Fatal", levels["Fatal error"] ?? 0, "danger")}
            ${card("Críticos", priorities.CRITICO ?? 0, "danger")}
            ${card("Altos", priorities.ALTO ?? 0, "warning")}
            ${card("Medios", priorities.MEDIO ?? 0, "info")}
            ${card("Bajos", priorities.BAJO ?? 0, "success")}

        </div>

        <div class="card shadow-sm border-0 mb-4">
            <div class="card-body">
                <h4 class="mb-4">Top 10 problemas normalizados</h4>
                <canvas id="chartProblems" height="120"></canvas>
            </div>
        </div>

        <div class="card shadow-sm border-0 mb-4">
            <div class="card-body">

                <div class="d-flex justify-content-between align-items-center mb-3">
                    <h4 class="mb-0">Errores específicos</h4>

                    <input
                        type="text"
                        id="searchErrors"
                        class="form-control metrify-search"
                        placeholder="Buscar por mensaje, archivo o prioridad..."
                        onkeyup="renderErrorsTable()">
                </div>

                <div class="table-responsive">
                    <table class="table table-dark table-hover align-middle">
                        <thead>
                            <tr>
                                <th>Prioridad</th>
                                <th>Mensaje</th>
                                <th>Archivo</th>
                                <th>Línea</th>
                                <th class="text-end">Ocurrencias</th>
                            </tr>
                        </thead>
                        <tbody id="errorsTableBody"></tbody>
                    </table>
                </div>

            </div>
        </div>

    `;

  drawProblemsChart(reportData);
  renderErrorsTable();
}

function card(title, value, color) {
  return `
        <div class="col-xl-3 col-lg-4 col-md-6">
            <div class="card shadow-sm border-0 h-100">
                <div class="card-body">
                    <div class="text-${color} fw-bold mb-2">${title}</div>
                    <div class="display-5 fw-bold">${Number(value).toLocaleString()}</div>
                </div>
            </div>
        </div>
    `;
}

function drawProblemsChart(data) {
  const top = data.normalized_problems.slice(0, 10);

  const labels = top.map((x) => x.message);
  const values = top.map((x) => x.count);

  new Chart(document.getElementById("chartProblems"), {
    type: "bar",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Eventos",
          data: values,
        },
      ],
    },
    options: {
      responsive: true,
      indexAxis: "y",
      plugins: {
        legend: {
          display: false,
        },
      },
      scales: {
        x: {
          ticks: {
            color: "#d1d5db",
          },
          grid: {
            color: "#374151",
          },
        },
        y: {
          ticks: {
            color: "#d1d5db",
          },
          grid: {
            display: false,
          },
        },
      },
    },
  });
}

function renderErrorsTable() {
  const tbody = document.getElementById("errorsTableBody");

  if (!tbody || !reportData) {
    return;
  }

  const searchInput = document.getElementById("searchErrors");
  const search = searchInput ? searchInput.value.toLowerCase() : "";

  const priorityMap = buildPriorityMap();

  const rows = reportData.specific_errors
    .filter((error) => {
      const priority = getPriorityForError(error.message, priorityMap);

      const text = `
                ${priority}
                ${error.message}
                ${error.file_name}
                ${error.line}
            `.toLowerCase();

      return text.includes(search);
    })
    .slice(0, 200)
    .map((error) => {
      const priority = getPriorityForError(error.message, priorityMap);

      return `
                <tr>
                    <td>
                        <span class="badge badge-${priority.toLowerCase()}">
                            ${priority}
                        </span>
                    </td>
                    <td>${escapeHtml(error.message)}</td>
                    <td>${escapeHtml(error.file_name)}</td>
                    <td>${error.line}</td>
                    <td class="text-end">${Number(error.count).toLocaleString()}</td>
                </tr>
            `;
    })
    .join("");

  tbody.innerHTML = rows;
}

function buildPriorityMap() {
  const map = {};

  reportData.normalized_problems.forEach((problem) => {
    map[problem.message] = problem.priority;
  });

  return map;
}

function getPriorityForError(message, priorityMap) {
  for (const problem in priorityMap) {
    if (message.startsWith(problem)) {
      return priorityMap[problem];
    }
  }

  return "BAJO";
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

loadReport();

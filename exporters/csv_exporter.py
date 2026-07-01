import csv
from pathlib import Path

from analysis_models import AnalysisResult


class CsvExporter:

    def export(self, result: AnalysisResult, output_file: str):

        output_path = Path(output_file)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with output_path.open(
            "w",
            encoding="utf-8",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Prioridad",
                "Tipo",
                "Problema",
                "Mensaje",
                "Archivo",
                "Linea",
                "Ocurrencias"
            ])

            #
            # Creamos un índice para obtener la prioridad
            #

            priority_map = {
                p.message: p.priority
                for p in result.normalized_problems
            }

            #
            # Escribimos cada error específico
            #

            for error in result.specific_errors:

                normalized = error.message

                for problem in priority_map.keys():

                    if normalized.startswith(problem):
                        normalized = problem
                        break

                writer.writerow([
                    priority_map.get(normalized, ""),
                    "",
                    normalized,
                    error.message,
                    error.file_name,
                    error.line,
                    error.count
                ])

        print(f"Reporte CSV generado: {output_path}")
import shutil
from pathlib import Path


class HtmlExporter:

    def export(self):

        template_dir = Path("templates")
        report_dir = Path("reports")

        report_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        files = [
            "report.html",
            "app.js",
            "styles.css"
        ]

        for file in files:

            shutil.copy2(
                template_dir / file,
                report_dir / file
            )

        print("Dashboard HTML generado.")
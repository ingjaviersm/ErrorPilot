import json
from pathlib import Path

from analysis_models import AnalysisResult


class JsonExporter:

    def export(self, result: AnalysisResult, output_file: str):

        data = {

            "summary": {

                "total_events": result.summary.total_events,

                "first_event": result.summary.first_event,

                "last_event": result.summary.last_event,

                "levels": result.summary.levels,

                "priorities": result.summary.priorities,

                "total_files": len(result.files),

                "problem_types": len(result.normalized_problems)

            },

            "normalized_problems": [

                {

                    "message": p.message,

                    "priority": p.priority,

                    "count": p.count

                }

                for p in result.normalized_problems

            ],

            "specific_errors": [

                {

                    "message": e.message,

                    "file_name": e.file_name,

                    "line": e.line,

                    "count": e.count

                }

                for e in result.specific_errors

            ],

            "files": [

                {

                    "file_name": f.file_name,

                    "total_events": f.total_events,

                    "score": f.score,

                    "problems": f.problems

                }

                for f in result.files

            ]

        }

        output_path = Path(output_file)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with output_path.open(
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=2,
                ensure_ascii=False
            )

        print(f"Reporte JSON generado: {output_path}")
from analysis_models import AnalysisResult


class ConsoleReport:

    def print_summary(self, result: AnalysisResult, top: int = 20):

        print()
        print("========================================")
        print("ErrorPilot")
        print("========================================")

        print(f"Total eventos: {result.summary.total_events}")

        if result.summary.total_events > 0:
            print(f"Primer evento: {result.summary.first_event}")
            print(f"Último evento : {result.summary.last_event}")

        print()

        print("----------------------------------------")
        print("Resumen por tipo")
        print("----------------------------------------")

        for level, count in sorted(
            result.summary.levels.items(),
            key=lambda item: item[1],
            reverse=True
        ):
            print(f"{level:<20} {count:>10}")

        print()

        print("----------------------------------------")
        print("Resumen por prioridad")
        print("----------------------------------------")

        for priority in ["CRITICO", "ALTO", "MEDIO", "BAJO"]:
            count = result.summary.priorities.get(priority, 0)
            print(f"{priority:<20} {count:>10}")

        print()

        print("----------------------------------------")
        print(f"Top {top} problemas normalizados")
        print("----------------------------------------")

        for index, problem in enumerate(
            result.normalized_problems[:top],
            start=1
        ):
            print(f"{index}. {problem.count}x [{problem.priority}]")
            print(f"   {problem.message}")
            print()

        print("----------------------------------------")
        print(f"Top {top} errores específicos")
        print("----------------------------------------")

        for index, error in enumerate(
            result.specific_errors[:top],
            start=1
        ):
            print(f"{index}. {error.count}x")
            print(f"   {error.message}")
            print(f"   {error.file_name}:{error.line}")
            print()

        print("----------------------------------------")
        print(f"Ranking de archivos problemáticos")
        print("----------------------------------------")

        for index, file in enumerate(
            result.files[:top],
            start=1
        ):
            print(f"{index}. {file.file_name}")
            print(f"   Score: {file.score}")
            print(f"   Eventos: {file.total_events}")
            print(f"   Problemas distintos: {len(file.problems)}")
            print()

        print("----------------------------------------")
        print(f"Resumen por archivo")
        print("----------------------------------------")

        for index, file in enumerate(
            result.files[:top],
            start=1
        ):
            print(f"{index}. {file.file_name}")
            print(f"   Total eventos: {file.total_events}")
            print("   Problemas:")

            problemas = sorted(
                file.problems.items(),
                key=lambda item: item[1],
                reverse=True
            )

            for problema, cantidad in problemas[:5]:
                print(f"   - {cantidad}x {problema}")

            print()
import argparse
import functools
import http.server
import socketserver
import webbrowser
from pathlib import Path

from parser import LogParser
from filters import LogFilters
from analyzer_engine import AnalyzerEngine
from report import ConsoleReport

from exporters.json_exporter import JsonExporter
from exporters.csv_exporter import CsvExporter
from exporters.html_exporter import HtmlExporter


def serve_dashboard(port: int = 8000):
    reports_dir = Path("reports").resolve()

    handler = functools.partial(
        http.server.SimpleHTTPRequestHandler,
        directory=str(reports_dir)
    )

    url = f"http://localhost:{port}/report.html"

    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Servidor iniciado: {url}")
        print("Presiona CTRL + C para detenerlo.")
        webbrowser.open(url)
        httpd.serve_forever()


def main():

    parser = argparse.ArgumentParser(description="ErrorPilot")

    parser.add_argument("logfile", help="Ruta del archivo de log")

    parser.add_argument("--top", type=int, default=20, help="Cantidad de errores principales a mostrar")

    parser.add_argument("--level", default=None, help='Filtrar por tipo. Ejemplo: Warning, "Fatal error", Notice')

    parser.add_argument("--file", default=None, help="Filtrar por archivo o parte de la ruta. Ejemplo: componentFactory.php, Erp37c")

    parser.add_argument("--contains", default=None, help='Filtrar por texto en el mensaje. Ejemplo: "Undefined array key"')

    parser.add_argument("--json", action="store_true", help="Generar reporte JSON en la carpeta reports")

    parser.add_argument("--csv", action="store_true", help="Generar reporte CSV en la carpeta reports")

    parser.add_argument("--html", action="store_true", help="Generar dashboard HTML en la carpeta reports")

    parser.add_argument("--serve", action="store_true", help="Iniciar servidor local para abrir el dashboard")

    args = parser.parse_args()

    log_parser = LogParser()
    entries = log_parser.parse_file(args.logfile)

    log_filters = LogFilters()
    entries = log_filters.apply(
        entries,
        level=args.level,
        file=args.file,
        contains=args.contains
    )

    engine = AnalyzerEngine()
    result = engine.analyze(entries)

    report = ConsoleReport()
    report.print_summary(result, args.top)

    if args.json or args.html or args.serve:
        exporter = JsonExporter()
        exporter.export(result, "reports/report.json")

    if args.csv:
        exporter = CsvExporter()
        exporter.export(result, "reports/report.csv")

    if args.html or args.serve:
        exporter = HtmlExporter()
        exporter.export()

    if args.serve:
        serve_dashboard()


if __name__ == "__main__":
    main()
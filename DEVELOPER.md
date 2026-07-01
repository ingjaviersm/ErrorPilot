# Developer Guide

## Architecture

```text
Parser
   ↓
LogEntry
   ↓
Filters
   ↓
AnalyzerEngine
   ↓
AnalysisResult
   ├── Console
   ├── JSON
   ├── CSV
   └── HTML
```

## Components

- `parser.py`
- `analyzer_engine.py`
- `normalizer.py`
- `priority.py`
- `filters.py`
- `report.py`
- `exporters/`

## Adding a New Normalization Rule

1. Add the new pattern to `normalizer.py`.
2. Assign a priority in `priority.py`.
3. Validate the results using the dashboard.

## Adding a New Exporter

Create a new file inside the `exporters/` directory with the following method:

```python
export(result, output_file)
```

Always consume the `AnalysisResult` model instead of parsing log entries again.

## Best Practices

- Do not modify the parser when adding new exporters.
- Keep the analysis engine decoupled from presentation layers.
- Avoid duplicating logic between exporters.
- Keep exporters focused on rendering or serialization only.
- Extend the project through composition rather than modifying existing components whenever possible.

## Technical Roadmap

- File ranking
- File detail view
- Analysis history
- Log comparison
- Installable CLI
- Unit tests
- Optional AI integration
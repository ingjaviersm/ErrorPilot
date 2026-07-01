# ErrorPilot

> Stop reading thousands of log lines. Start fixing what really matters.

ErrorPilot is an open source tool that analyzes PHP log files and transforms them into actionable insights, helping developers prioritize and resolve issues faster.

## What problem does it solve?

Large PHP applications often generate log files containing tens or even hundreds of thousands of repeated entries. Finding the issues that truly matter can be time-consuming and frustrating.

ErrorPilot automatically groups similar errors, identifies the most affected files, and generates an interactive HTML dashboard that makes log analysis much easier.

## Features

- PHP log parser
- Error normalization
- Smart error prioritization
- Interactive HTML dashboard
- JSON and CSV export
- Filters by level, file, and text
- Searchable error table

## Quick Start

```bash
python analyzer.py samples/php-errors.log --serve
```

The command will:

1. Analyze the log file.
2. Generate the reports.
3. Start a local web server.
4. Open the interactive dashboard automatically.

## Use Cases

- ERP systems
- Legacy PHP applications
- Laravel
- Symfony
- WordPress
- CodeIgniter
- Custom PHP applications

## Roadmap

- File ranking
- File detail view
- Health Score
- Log comparison
- Analysis history
- Automatic recommendations
- Optional AI integration
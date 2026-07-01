# User Guide

## Analyze a Log File

```bash
python analyzer.py samples/php-errors.log
```

## Launch the Dashboard

```bash
python analyzer.py samples/php-errors.log --serve
```

This command will:

1. Analyze the log file.
2. Generate the HTML, JSON, and CSV reports.
3. Start a local web server.
4. Open the interactive dashboard in your default browser.

---

# Filters

## Filter by Error Level

```bash
--level Warning
```

```bash
--level "Fatal error"
```

## Filter by File

```bash
--file OrderController.php
```

## Filter by Text

```bash
--contains "Undefined array key"
```

## Limit Results

```bash
--top 50
```

---

# Export Formats

## JSON

```bash
--json
```

## CSV

```bash
--csv
```

## HTML

```bash
--html
```

## Interactive Dashboard

```bash
--serve
```

---

# Understanding Priority Levels

## 🔴 Critical

Errors that usually stop the application from running.

Examples:

- Fatal Error
- Parse Error
- Memory exhausted

---

## 🟠 High

Errors that are likely to cause application failures or unexpected behavior.

Examples:

- Attempt to read property on null
- Call to a member function on null

---

## 🔵 Medium

Common programming mistakes that should be fixed but generally do not stop execution.

Examples:

- Undefined array key
- Undefined property
- Undefined variable

---

## 🟢 Low

Minor warnings and notices with limited impact.

Examples:

- Session ini settings cannot be changed
- A non-numeric value encountered
- Deprecated warnings

> **Note:** Priority levels are based on common PHP error patterns and are intended to help developers prioritize their work. They should not replace engineering judgment.

---

# Recommended Workflow

1. Fix **Critical** issues first.
2. Resolve **High** priority errors.
3. Review the files with the highest number of issues.
4. Run ErrorPilot again.
5. Compare the results to measure progress.
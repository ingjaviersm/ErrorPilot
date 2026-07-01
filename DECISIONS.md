# Design Decisions

This document records the key architectural and technical decisions made during the development of ErrorPilot.

---

## 2026-06-30

### Why a static HTML dashboard?

To keep the project lightweight and free from unnecessary dependencies.

The dashboard only consumes the generated `report.json` file, making it easy to share, host, and run without requiring a backend framework or web server.

---

### Why `AnalysisResult`?

To decouple the analysis engine from the exporters.

All exporters (Console, JSON, CSV, HTML, and future ones) consume the same data model, making it easy to extend the project without modifying the core analysis logic.

---

### Why Chart.js?

Chart.js is lightweight, well-maintained, widely adopted, and does not require a build process.

It provides all the visualization capabilities needed while keeping the project simple.

---

### Why use custom priority levels?

PHP reports errors, warnings, notices, and deprecations, but it does not indicate which issues should be fixed first.

ErrorPilot introduces its own priority system to help developers focus on the most impactful issues before addressing less critical ones.

---

### Why a decoupled architecture?

A modular architecture makes the project easier to maintain and extend.

New exporters (PDF, Excel, Markdown, Discord, Slack, etc.) can be added without changing the analysis engine, reducing coupling and improving scalability.
# Decisiones de diseño

## 2026-06-30

### ¿Por qué un dashboard HTML estático?

Para evitar dependencias innecesarias. El dashboard consume únicamente
`report.json`, por lo que puede compartirse y ejecutarse fácilmente.

------------------------------------------------------------------------

### ¿Por qué `AnalysisResult`?

Para desacoplar el motor de análisis de los exportadores. Todos los
exportadores consumen la misma estructura de datos.

------------------------------------------------------------------------

### ¿Por qué Chart.js?

Es ligero, ampliamente soportado y no requiere un proceso de
compilación.

------------------------------------------------------------------------

### ¿Por qué prioridades propias?

PHP no clasifica los errores según su impacto para el desarrollador.
ErrorPilot asigna prioridades orientadas a facilitar la
corrección.

------------------------------------------------------------------------

### ¿Por qué una arquitectura desacoplada?

Permite agregar nuevos exportadores (PDF, Excel, Markdown, Discord,
etc.) sin modificar el motor de análisis.

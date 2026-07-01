# DEVELOPER

## Arquitectura

``` text
Parser
   ↓
LogEntry
   ↓
Filtros
   ↓
AnalyzerEngine
   ↓
AnalysisResult
   ├── Consola
   ├── JSON
   ├── CSV
   └── HTML
```

## Componentes

-   parser.py
-   analyzer_engine.py
-   normalizer.py
-   priority.py
-   filters.py
-   report.py
-   exporters/

## Agregar una nueva regla

1.  Añadir el patrón en `normalizer.py`.
2.  Asignar prioridad en `priority.py`.
3.  Validar el resultado en el dashboard.

## Agregar un exportador

Crear un nuevo archivo dentro de `exporters/` con un método:

``` python
export(result, output_file)
```

Consumir siempre `AnalysisResult`.

## Buenas prácticas

-   No modificar el parser para agregar exportadores.
-   Mantener desacoplado el motor de análisis.
-   Evitar duplicar lógica entre exportadores.

## Roadmap técnico

-   Ranking de archivos.
-   Vista por archivo.
-   Historial.
-   Comparación entre logs.
-   CLI instalable.
-   Tests unitarios.
-   Integración opcional con IA.

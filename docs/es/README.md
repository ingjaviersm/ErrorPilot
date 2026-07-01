# ErrorPilot

> Deja de leer miles de líneas de logs. Empieza a corregir lo que
> realmente importa.

ErrorPilot es una herramienta para analizar archivos de log de
PHP y transformarlos en información útil para priorizar la corrección de
errores.

## ¿Qué problema resuelve?

En proyectos grandes es común encontrar archivos de log con decenas o
cientos de miles de líneas repetidas. Encontrar los problemas realmente
importantes consume tiempo.

Esta herramienta agrupa automáticamente los errores, identifica los
archivos más afectados y genera un dashboard HTML interactivo para
facilitar el análisis.

## Características

-   Parser para logs de PHP.
-   Normalización de errores repetitivos.
-   Clasificación por prioridad.
-   Dashboard HTML.
-   Exportación JSON y CSV.
-   Filtros por nivel, archivo y texto.
-   Búsqueda de errores.

## Instalación rápida

``` bash
python analyzer.py samples/30062026.txt --serve
```

El comando:

1.  Analiza el log.
2.  Genera los reportes.
3.  Levanta un servidor local.
4.  Abre automáticamente el dashboard.

## Casos de uso

-   ERP
-   Sistemas legacy en PHP
-   Laravel
-   Symfony
-   WordPress
-   CodeIgniter
-   Aplicaciones PHP personalizadas

## Roadmap

-   Ranking de archivos.
-   Vista por archivo.
-   Health Score.
-   Comparación entre logs.
-   Historial.
-   Recomendaciones automáticas.
-   Integración opcional con IA.

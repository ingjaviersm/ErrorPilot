# Guía de uso

## Analizar un log

``` bash
python analyzer.py samples/php-errors.log
```

## Dashboard

``` bash
python analyzer.py samples/php-errors.log --serve
```

## Filtros

### Por nivel

``` bash
--level Warning
--level "Fatal error"
```

### Por archivo

``` bash
--file componentFactory.php
```

### Por texto

``` bash
--contains "Undefined array key"
```

### Top

``` bash
--top 50
```

## Exportadores

### JSON

``` bash
--json
```

### CSV

``` bash
--csv
```

### HTML

``` bash
--html
```

### Dashboard automático

``` bash
--serve
```

## ¿Cómo interpretar las prioridades?

### 🔴 CRÍTICO

Errores que normalmente detienen la ejecución.

Ejemplos:

-   Fatal Error
-   Parse Error
-   Memory exhausted

### 🟠 ALTO

Errores que pueden provocar fallas funcionales.

Ejemplos:

-   Attempt to read property on null
-   Call to member function on null

### 🔵 MEDIO

Errores frecuentes durante el desarrollo.

Ejemplos:

-   Undefined array key
-   Undefined property
-   Undefined variable

### 🟢 BAJO

Advertencias con menor impacto.

Ejemplos:

-   Session ini settings cannot be changed
-   A non-numeric value encountered

> La clasificación es una recomendación basada en patrones comunes de
> PHP y no sustituye el criterio del desarrollador.

## Flujo recomendado

1.  Corregir errores críticos.
2.  Corregir errores altos.
3.  Revisar los archivos con más incidencias.
4.  Ejecutar nuevamente el análisis.
5.  Comparar resultados.

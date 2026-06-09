# Decisiones Técnicas

## Calidad de Datos

### Recuperación de categorías nulas

La columna `tipo` presentaba un 53.9% de registros nulos. En lugar de descartar información, se implementó una inferencia mediante reglas de negocio sobre `tags` y `titulo`, consolidando el resultado con `COALESCE(tipo, tipo_inferido)`.

---

## Outliers de Precio

### Conservación de valores extremos

La revisión manual confirmó que los precios por encima del percentil 99 correspondían a productos reales (ediciones especiales y formatos no estándar). Se decidió conservarlos y segmentar el análisis mediante percentiles en lugar de eliminarlos.

---

## Homologación de Bodegas

### Estandarización de nombres

Se detectaron diferencias de nomenclatura entre tiendas para una misma bodega (por ejemplo, "Paco y Lola" vs "Paco & Lola"). Se implementaron reglas de homologación mediante SQL. Como mejora futura se propone incorporar Fuzzy Matching utilizando métricas de similitud como Levenshtein.

---

## Reclasificación de Categorías

### Corrección de inconsistencias de origen

Se identificó que algunas tiendas clasificaban incorrectamente productos espumantes bajo la categoría general de vino. En Silver se incorporaron reglas de reclasificación utilizando información proveniente de tags y títulos.

---

## Tratamiento Especial de Bodega Norton

### Exclusión del análisis de varietales

Los tags de Norton contienen principalmente información operativa y logística, sin exponer varietales de forma consistente. Para evitar clasificaciones incorrectas, la tienda fue excluida del análisis de distribución de varietales.


---

## Deduplicación de Productos

### Consolidación por tienda y título

Se detectaron productos con el mismo título dentro de una misma tienda pero con diferencias de precio asociadas a presentaciones especiales. Para evitar duplicidad conceptual en el análisis se conservó únicamente el registro de menor precio utilizando `ROW_NUMBER()`.

---

## Modelo Dimensional

### Esquema Estrella

Se implementó un modelo dimensional orientado al análisis de catálogo y pricing competitivo mediante una tabla de hechos (`fact_catalogo`) y dimensiones de producto, tienda y varietal.

### Relación Muchos a Muchos

Un producto puede estar asociado a múltiples varietales y un varietal puede estar presente en múltiples productos. Para preservar esta relación se incorporó la tabla puente `dim_producto_varietal`.

---

## Slowly Changing Dimensions (SCD)

### SCD Type 1

La dimensión de productos utiliza actualizaciones tipo SCD 1 mediante `MERGE`, ya que el negocio requiere únicamente el estado actual de atributos descriptivos como categoría, bodega y título, sin necesidad de conservar historial.
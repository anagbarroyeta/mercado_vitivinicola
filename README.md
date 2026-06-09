# Mercado Vitivinícola - Data Engineering Project

## Objetivo

Analizar el posicionamiento competitivo de vinotecas digitales internacionales mediante una arquitectura Lakehouse implementada en Databricks.

## Arquitectura

Shopify APIs → Landing → Bronze → Silver → Gold

## Tecnologías

- Databricks
- Delta Lake
- SQL
- Python
- GitHub

## Capas

### Bronze
Datos crudos provenientes de Shopify.

### Silver
Estandarización, calidad y deduplicación.

### Gold
Modelo dimensional orientado al análisis.

## Modelo dimensional

- dim_tiendas
- dim_productos
- dim_varietales
- dim_producto_varietal
- fact_catalogo

## Principales desafíos

- Recuperación de categorías nulas mediante inferencia.
- Reclasificación de espumantes mal catalogados.
- Homologación de bodegas.
- Tratamiento de ruido en tags.
- Resolución de relaciones muchos a muchos.

## Estado del proyecto

✅ Landing

✅ Bronze

✅ Silver

✅ Gold

✅ Workflow Databricks Jobs

🚧 Dashboards Power BI

🚧 KPIs finales

🚧 Documentación ampliada
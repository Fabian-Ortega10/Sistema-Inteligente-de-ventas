# Notas de ETL (Extract, Transform, Load)

## 1. Ingesta de datos
- Dataset original: `data/raw/train.csv`
- Fuente: Kaggle / descargas locales
- Número de registros iniciales: XXXX
- Número de columnas iniciales: XX

## 2. Limpieza realizada
- Eliminación de duplicados: Sí / No
- Tratamiento de valores nulos:
  - Columna `precio`: valores nulos reemplazados por 0
  - Columna `fecha`: nulos eliminados
- Formatos corregidos:
  - `fecha` convertida a tipo datetime
  - `producto_id` convertido a string

## 3. Transformaciones aplicadas
- Normalización de nombres de columnas (minúsculas, sin espacios).
- Creación de columna `mes` a partir de `fecha`.
- Agrupación de ventas por producto y periodo.

## 4. Resultados
- Registros finales: XXXX
- Columnas finales: XX
- Archivo limpio guardado en: `data/processed/ventas_clean.csv`

## 5. Observaciones
- Se detectaron outliers en la columna `cantidad`.
- Se recomienda revisar la calidad de datos en `cliente_id`.

Columnas normalizadas → nombres consistentes y fáciles de usar.

Nulos tratados por columna → cada variable tiene su estrategia (ejemplo: precio = 0, cantidad = mediana).

Fechas convertidas → permite análisis temporal.

Columnas derivadas (año, mes, día) → útiles para agrupaciones y visualizaciones.

Dataset limpio guardado en data/processed/ventas_clean.csv → listo para EDA.
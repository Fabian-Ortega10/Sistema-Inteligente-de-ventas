from config import RAW_DATA_PATH, PROCESSED_DATA_PATH
import pandas as pd
import numpy as np
import time
from utils.logger import get_logger

logger = get_logger("ETL", "etl.log")

def run_etl():
    start_time = time.time()
    logger.info("Inicio del proceso ETL")

    try:
        # 1. Extraer
        df = pd.read_csv(RAW_DATA_PATH)
        logger.debug(f"Datos cargados: {df.shape[0]} filas, {df.shape[1]} columnas")

        # 2. Normalización de nombres de columnas
        df.columns = (
            df.columns.str.strip()
                      .str.lower()
                      .str.replace(" ", "_")
        )

        # 3. Optimización de tipos de datos
        if "precio" in df.columns:
            df["precio"] = df["precio"].astype("float32").fillna(0)
        if "cantidad" in df.columns:
            df["cantidad"] = df["cantidad"].astype("int32").fillna(df["cantidad"].median())
        if "customer_id" in df.columns:
            df["customer_id"] = df["customer_id"].astype("category")
        if "product_id" in df.columns:
            df["product_id"] = df["product_id"].astype("category")

        # 4. Manejo de fechas
        if "fecha" in df.columns:
            df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
            df = df.dropna(subset=["fecha"])
            df["anio"] = df["fecha"].dt.year.astype("int16")
            df["mes"] = df["fecha"].dt.month.astype("int8")
            df["dia"] = df["fecha"].dt.day.astype("int8")

        # 5. Eliminación de duplicados
        df = df.drop_duplicates()

        # 6. Creación de métricas derivadas
        metrics = {}
        if {"precio", "cantidad"}.issubset(df.columns):
            df["sales"] = df["precio"] * df["cantidad"]
            metrics["ventas_totales"] = float(df["sales"].sum())
            metrics["promedio_por_orden"] = float(df["sales"].mean())
        if "customer_id" in df.columns:
            metrics["clientes_unicos"] = int(df["customer_id"].nunique())
        if "product_id" in df.columns:
            top_productos = (
                df.groupby("product_id")["sales"].sum()
                  .sort_values(ascending=False).head(10)
            )
            metrics["top_productos"] = top_productos.to_dict()

        # 7. Guardar dataset limpio en CSV y Parquet
        df.to_csv(PROCESSED_DATA_PATH, index=False)
        parquet_path = PROCESSED_DATA_PATH.replace(".csv", ".parquet")
        df.to_parquet(parquet_path, index=False)
        logger.info(f"Dataset guardado en {PROCESSED_DATA_PATH} y {parquet_path}")

        # 8. Guardar métricas derivadas
        metrics_path = PROCESSED_DATA_PATH.replace("ventas_clean.csv", "metrics.json")
        pd.Series(metrics).to_json(metrics_path, indent=4)
        logger.info(f"Métricas guardadas en {metrics_path}")

        # 9. Log de rendimiento
        elapsed = round(time.time() - start_time, 2)
        logger.info(f"ETL completado en {elapsed} segundos")
        logger.debug(f"Dimensiones finales: {df.shape}")

    except Exception as e:
        logger.error(f"Error en ETL: {e}", exc_info=True)

if __name__ == "__main__":
    run_etl()

from config import RAW_DATA_PATH, PROCESSED_DATA_PATH
import pandas as pd
from utils.logger import get_logger

logger = get_logger("ETL", "etl.log")

def run_etl():
    logger.info("Inicio del proceso ETL")
    try:
        df = pd.read_csv(RAW_DATA_PATH)
        logger.debug(f"Datos cargados: {df.shape[0]} filas, {df.shape[1]} columnas")

        # Normalización de columnas
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
        logger.debug(f"Columnas normalizadas: {df.columns.tolist()}")

        # Manejo de nulos
        if "precio" in df.columns:
            df["precio"] = df["precio"].fillna(0)
        if "cantidad" in df.columns:
            df["cantidad"] = df["cantidad"].fillna(df["cantidad"].median())

        # Guardar dataset limpio
        df.to_csv(PROCESSED_DATA_PATH, index=False)
        logger.info(f"ETL completado. Archivo guardado en {PROCESSED_DATA_PATH}")
        logger.debug(f"Dimensiones finales: {df.shape}")

    except Exception as e:
        logger.error(f"Error en ETL: {e}", exc_info=True)

if __name__ == "__main__":
    run_etl()

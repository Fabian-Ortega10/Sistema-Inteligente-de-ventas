# src/config.py
import os
from dotenv import load_dotenv

# Cargar variables desde .env
load_dotenv()

# Rutas de datos
RAW_DATA_PATH = os.getenv("RAW_DATA_PATH")
PROCESSED_DATA_PATH = os.getenv("PROCESSED_DATA_PATH")

# Configuración de base de datos
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Función auxiliar para construir rutas absolutas
def get_path(relative_path: str) -> str:
    """Devuelve la ruta absoluta a partir de una ruta relativa."""
    base_dir = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_dir, relative_path)

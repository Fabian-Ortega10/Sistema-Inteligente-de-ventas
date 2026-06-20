import logging
import os
from logging.handlers import TimedRotatingFileHandler

def get_logger(name: str, log_file: str) -> logging.Logger:
    """Configura un logger con salida a archivo y consola."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Nivel detallado para desarrollo

    # Evitar duplicados si ya existe
    if logger.hasHandlers():
        return logger

    # Carpeta de logs
    log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
    os.makedirs(log_dir, exist_ok=True)

    # Handler de archivo con rotación diaria
    file_handler = TimedRotatingFileHandler(
        os.path.join(log_dir, log_file),
        when="midnight",
        backupCount=7,
        encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)

    # Handler de consola
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Formato profesional
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Agregar handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# ===========================
# Sistema Inteligente de Ventas
# Orquestación reproducible
# ===========================

# Variables
PYTHON := python
STREAMLIT := streamlit
ETL_SCRIPT := src/etl.py
DASHBOARD_SCRIPT := src/dashboard.py
DATA_PROCESSED := data/processed
VENV := .venv

# ===========================
# Comandos principales
# ===========================

# Ejecutar ETL
etl:
    @echo "🔄 Ejecutando proceso ETL..."
    $(PYTHON) $(ETL_SCRIPT)
    @echo "✅ ETL completado."

# Ejecutar Dashboard
dashboard:
    @echo "🚀 Iniciando Dashboard de Inteligencia de Ventas..."
    $(STREAMLIT) run $(DASHBOARD_SCRIPT)

# Limpiar datos procesados
clean:
    @echo "🧹 Limpiando datos procesados..."
    rm -rf $(DATA_PROCESSED)/*
    @echo "✅ Limpieza completada."

# Ejecutar flujo completo
all: clean etl dashboard

# ===========================
# Utilidades
# ===========================

# Instalar dependencias
install:
    @echo "📦 Instalando dependencias..."
    pip install -r requirements.txt
    @echo "✅ Dependencias instaladas."

# Activar entorno virtual
venv:
    @echo "🔧 Activando entorno virtual..."
    source $(VENV)/Scripts/activate || source $(VENV)/bin/activate
    @echo "✅ Entorno activado."

# ===========================
# Ayuda
# ===========================
help:
    @echo "Comandos disponibles:"
    @echo "  make etl        → Ejecuta el proceso ETL"
    @echo "  make dashboard  → Inicia el dashboard Streamlit"
    @echo "  make clean      → Limpia los datos procesados"
    @echo "  make all        → Ejecuta todo el flujo completo"
    @echo "  make install    → Instala dependencias"
    @echo "  make venv       → Activa entorno virtual"

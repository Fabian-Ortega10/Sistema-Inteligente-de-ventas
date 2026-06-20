## Título
Sistema Inteligente de Ventas – ETL + Dashboard

## Objetivo
Este proyecto implementa un flujo completo de ETL (Extracción, Transformación y Carga) y un Dashboard interactivo en Streamlit para analizar ventas, clientes y productos.
El propósito es demostrar habilidades en ingeniería de datos, análisis y visualización, con un enfoque reproducible y profesional.

## Estructura del proyecto

Sistema-Inteligente-de-ventas/
│
├── data/               # Datos crudos y procesados
├── docs/               # Documentación técnica y ejecutiva
├── logs/               # Archivos de logging por módulo
├── notebooks/          # Exploración y EDA
├── src/                # Código fuente
│   ├── etl.py          # Proceso ETL optimizado
│   ├── dashboard.py    # Dashboard Streamlit
│   └── utils/          # Configuración y utilidades
│       ├── config.py
│       └── logger.py
├── .env                # Variables de entorno (no se sube a GitHub)
├── requirements.txt    # Dependencias
├── Makefile            # Orquestación reproducible
└── README.md           # Documentación principal

## Instalación y ejecución
# Clonar repositorio
git clone <URL>

# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar ETL
make etl

# Iniciar dashboard
make dashboard

Métricas calculadas en ETL
Ventas totales

Promedio por orden

Número de clientes únicos

Top 10 productos más vendidos

## Resultados esperados
Dataset limpio y optimizado en data/processed/ventas_clean.csv y .parquet.

Métricas derivadas en data/processed/metrics.json.

Dashboard interactivo con KPIs, filtros y gráficos.

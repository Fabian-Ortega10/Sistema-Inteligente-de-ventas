# Sistema de Inteligencia de Ventas con SQL, Python y Dashboard

##  Propósito
Este proyecto transforma datos de ventas en información útil y accionable para apoyar la toma de decisiones comerciales. Se busca identificar tendencias, productos de mayor desempeño y patrones de comportamiento que permitan optimizar inventario y estrategia comercial.

##  Objetivos
- Identificar productos con mejor desempeño en ventas.
- Analizar variaciones de ventas en diferentes periodos (mensual, trimestral, anual).
- Generar reportes ejecutivos y dashboards interactivos para facilitar la interpretación de resultados.
- Proveer recomendaciones basadas en datos para apoyar decisiones estratégicas.

##  Preguntas clave
- ¿Qué productos tienen mejor desempeño?
- ¿Cómo varían las ventas por periodo?
- ¿Qué tendencias ayudan a planear inventario?

##  Tecnologías utilizadas
- **SQL (MySQL/PostgreSQL):** gestión y consulta de datos.
- **Python (Pandas, NumPy, Matplotlib, Seaborn, Plotly):** análisis y visualización.
- **Streamlit/Dash:** construcción de dashboards interactivos.
- **Git + GitHub:** control de versiones y colaboración.
- **Docker (opcional):** reproducibilidad del entorno.

##  Estructura del proyecto
SistemaInteligenciaVentas/
├── data/              # Datos crudos y procesados
│   ├── raw/           # Dataset original (train.csv)
│   └── processed/     # Dataset limpio (ventas_clean.csv)
├── notebooks/         # Jupyter Notebooks (EDA, modelos, dashboards)
├── src/               # Scripts Python (ETL, análisis, visualizaciones)
├── visuals/           # Gráficos generados automáticamente
├── docs/              # Documentación (problema, objetivos, reportes ejecutivos)
├── requirements.txt   # Librerías necesarias
├── README.md          # Descripción general del proyecto
├── LICENSE            # Licencia de uso
└── .gitignore         # Archivos a excluir del repositorio

-----------------


##  Flujo del proyecto
1. **ETL (`src/etl.py`)**  
   - Limpieza y transformación del dataset crudo (`data/raw/train.csv`).  
   - Genera el archivo limpio `data/processed/ventas_clean.csv`.

2. **EDA (`notebooks/eda.ipynb`)**  
   - Estadísticas descriptivas y visualizaciones.  
   - Gráficos guardados en `visuals/`.  
   - Hallazgos documentados en `docs/eda_report.md`.

3. **Modelado y análisis avanzado**  
   - Feature engineering, clustering y predicciones.  
   - Scripts reproducibles en `src/`.

4. **Dashboard interactivo (`src/dashboard.py`)**  
   - Visualización ejecutiva en Streamlit/Dash.  
   - Integración con SQL para consultas dinámicas.

##  Instalación
Clonar el repositorio:
```bash
git clone https://github.com/Fabianoc10/SistemaInteligenciaVentas.git
cd SistemaInteligenciaVentas
---------------------------

Crear entorno virtual:
python -m venv venv
venv\Scripts\activate   # Windows

Instalar dependencias:
pip install -r requirements.txt

---------------------------------

Uso: Ejecutar el ETL:
python src/etl.py

Abrir notebooks en notebooks/ para análisis exploratorio.

Correr el dashboard:
streamlit run src/dashboard.py
----------------------------------

Documentación
Definición del problema y objetivos → docs/Definicion_Problema_Objetivos.md

Reporte de EDA → docs/eda_report.md

Próximos reportes ejecutivos se irán agregando en docs/.

📌 Próximos pasos
Integrar clustering con columna satisfaction_level.

Construir dashboard en Power BI/Streamlit.

Documentar hallazgos clave en reportes ejecutivos.

Automatizar despliegue con Docker.
----------------------------------------------

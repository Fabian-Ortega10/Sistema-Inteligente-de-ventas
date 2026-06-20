from config import PROCESSED_DATA_PATH
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils.logger import get_logger

# Inicializar logger
logger = get_logger("Dashboard", "dashboard.log")

# Cargar dataset limpio con manejo de errores
try:
    df = pd.read_csv(PROCESSED_DATA_PATH, parse_dates=["order_date"], dayfirst=True)
    logger.info("Dataset cargado correctamente en el dashboard")
except Exception as e:
    logger.error(f"Error al cargar dataset: {e}", exc_info=True)
    st.error("No se pudo cargar el dataset")
    df = pd.DataFrame()  # Evita que el dashboard se rompa si falla la carga

#----------------------------------------------

#Titulo
st.title(" Dashboard de Inteligencia de Ventas")
st.write("Este dashboard muestra KPIs, tendencias y análisis de ventas.")

if not df.empty:
    # KPIs 
    st.metric("Ventas Totales", f"${df['sales'].sum():,.2f}")
    st.metric("Promedio por Orden", f"${df['sales'].mean():,.2f}")
    st.metric("Número de Clientes", df['customer_id'].nunique())
    logger.debug("KPIs calculados correctamente")

    #Filtros interactivos
    fecha_inicio = st.date_input("Fecha inicio", df["order_date"].min())
    fecha_fin = st.date_input("Fecha fin", df["order_date"].max())
    df_filtrado = df[(df["order_date"] >= pd.to_datetime(fecha_inicio)) & (df["order_date"] <= pd.to_datetime(fecha_fin))]
    logger.debug(f"Filtro aplicado: {fecha_inicio} a {fecha_fin}, {len(df_filtrado)} registros")

    # Graficos de Ventas por Fecha
    fig, ax = plt.subplots(figsize=(10,5))
    df_filtrado.groupby("order_date")["sales"].sum().plot(ax=ax)
    ax.set_title("Ventas por fecha")
    st.pyplot(fig)
    logger.debug("Gráfico de ventas por fecha generado")

    #Top productos mas vendidos
    top_productos = df_filtrado.groupby("product_id")["sales"].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(8,5))
    sns.barplot(x=top_productos.index, y=top_productos.values, ax=ax)
    ax.set_title("Top 10 productos más vendidos")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)
    logger.debug("Gráfico de top productos generado")

    #Estacionalidad (Ventas por mes)
    df_filtrado["mes"] = df_filtrado["order_date"].dt.month
    ventas_por_mes = df_filtrado.groupby("mes")["sales"].sum()

    fig, ax = plt.subplots(figsize=(8,5))
    ventas_por_mes.plot(kind="bar", ax=ax)
    ax.set_title("Ventas por mes (estacionalidad)")
    st.pyplot(fig)
    logger.debug("Gráfico de estacionalidad generado")

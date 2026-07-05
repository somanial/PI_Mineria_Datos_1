import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dataset - PI Minería de Datos", page_icon="📊", layout="wide")

st.title("📊 Descripción General del Dataset y Calidad")
st.markdown("---")

# Resumen técnico requerido por la consigna
st.markdown("### 🔍 Resumen de Calidad Inicial")
st.write(
    "El dataset original provisto por la cátedra contenía un total de **8160 registros** "
    "y presentaba un total de **320 valores faltantes** distribuidos en las variables clave. "
    "Adicionalmente, se detectaron problemas de consistencia en variables categóricas debido a diferencias de tipeo (mayúsculas, minúsculas y acentos)."
)

# Sección de transformaciones principales
st.markdown("### ⚙️ Transformaciones Principales (ETL)")
st.markdown(
    """
    * **Tratamiento de Nulos:** Se realizó un proceso mixto de imputación y borrado de registros incompletos, alcanzando una **retención del 96.07%** del dataset original (7840 filas finales).
    * **Unificación de Categorías:** Se aplicaron diccionarios de mapeo explícitos mediante `.map()` para consolidar las variantes de texto en los planes (`Standard`, `Basic`, `Premium`) y géneros cinematográficos.
    """
)

st.info("💡 En una etapa posterior, aquí se acoplará la lectura automática de `data/processed/` para mostrar una vista previa interactiva de las filas del dataset limpio.")
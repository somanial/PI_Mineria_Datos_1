import streamlit as st

st.set_page_config(page_title="EDA - PI Minería de Datos", page_icon="📈", layout="wide")

st.title("📈 Análisis Exploratorio de Datos (EDA)")
st.markdown("---")

st.markdown("### 📊 Estructura de Visualizaciones Obligatorias")
st.write("A continuación se detallan los hallazgos críticos del análisis exploratorio, estructurados según los requerimientos de la cátedra (5 visualizaciones exactas).")

# Pestañas visuales para organizar el contenido interactivo
tab1, tab2, tab3 = st.tabs(["1. Análisis Univariado", "2. Análisis Bivariado", "3. Análisis Multivariado"])

with tab1:
    st.markdown("#### 🔹 Visualización 1 & 2: Distribución de Variables Clave")
    st.markdown("**Interpretación Obligatoria:**")
    st.write(
        "El análisis univariado reveló la distribución de las variables numéricas (como la edad y los minutos consumidos) "
        "y categóricas (planes y géneros). Esto permitió identificar que no existen sesgos masivos en la recolección inicial "
        "de la muestra, pero sí la necesidad de unificar los textos debido a la dispersión provocada por problemas de tipeo manual."
    )

with tab2:
    st.markdown("#### 🔹 Visualización 3 & 4: Relación entre Planes y Consumo")
    st.markdown("**Interpretación Obligatoria:**")
    st.write(
        "Al cruzar los tipos de planes con el tiempo de visualización mensual (`monthly_watch_time_mins`), descubrimos que los "
        "usuarios del Plan Premium presentan los niveles de consumo más altos y sostenidos de la plataforma. Este comportamiento "
        "no está condicionado por un rango de edad específico, distribuyéndose a lo largo de todo el perfil sociodemográfico."
    )

with tab3:
    st.markdown("#### 🔹 Visualización 5: Análisis Multivariado (El hallazgo crítico)")
    st.markdown("**Interpretación Obligatoria:**")
    st.write(
        "El análisis multivariado combinó simultáneamente el Plan, el Consumo Mensual y los Tickets de Soporte Técnico. "
        "La evidencia demuestra que los usuarios Premium no solo consumen más minutos, sino que generan la mayor tasa de fricción "
        "con el soporte. Esto indica que son clientes altamente exigentes cuyo riesgo de abandono (Churn) está directamente "
        "ligado a la experiencia y velocidad de resolución de sus problemas técnicos."
    )
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Home - PI Minería de Datos",
    page_icon="🏠",
    layout="wide"
)

# Título Principal
st.title("🎬 Proyecto Integrador: Análisis de Usuarios de Streaming")
st.subheader("Minería de Datos 1")

st.markdown("---")

# Columnas para organizar la información del alumno y la entrega
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 👤 Información del Proyecto")
    st.markdown("**🧑‍🏫 Integrante:** Alex Fernando Guerrero")
    st.markdown("**📅 Fecha:** 4 de Julio 2026")
    st.markdown("**📍 Ubicación:** Nueva Esperanza, Santiago del Estero, Argentina")

with col2:
    st.markdown("### 🔗 Enlaces Oficiales")
    # Dejamos el enlace listo para cuando subas tu repositorio a GitHub
    st.markdown("[📦 Repositorio Público de GitHub](https://github.com/)")

st.markdown("---")

# Contexto Breve exigido por la cátedra
st.markdown("### 📝 Contexto del Proyecto")
st.write(
    "Este proyecto consiste en un análisis de datos reproducible sobre el comportamiento "
    "de los usuarios de una plataforma de streaming. A través de las distintas pestañas laterales, "
    "se puede explorar la calidad inicial del dataset, las transformaciones de limpieza aplicadas, "
    "los hallazgos del análisis exploratorio (EDA) y los resultados de la reducción de dimensionalidad mediante PCA."
)

st.info("👈 Utilizá la barra lateral de la izquierda para navegar entre las distintas secciones del análisis.")
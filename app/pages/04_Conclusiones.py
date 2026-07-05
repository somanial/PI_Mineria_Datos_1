import streamlit as st

st.set_page_config(page_title="Conclusiones - PI Minería de Datos", page_icon="🏁", layout="wide")

st.title("🏁 Conclusiones del Análisis")
st.markdown("---")

st.markdown("### 🎯 Hallazgos y Decisiones Clave")
st.write(
    "Para cerrar el proyecto integrador, se consolidan las siguientes conclusiones de negocio "
    "y metodológicas, alineadas estrictamente con los objetivos planteados en la investigación:"
)

# Bloques destacados con las conclusiones principales del negocio y del método
st.info(
    "**1. Priorización del Segmento Premium:**\n\n"
    "Los usuarios del Plan Premium representan la mayor fuente de ingresos, pero también el mayor "
    "foco de fricción operativa debido al alto volumen de tickets de soporte técnico que generan. "
    "Se recomienda diseñar estrategias de retención enfocadas en optimizar los tiempos de resolución de este segmento."
)

st.success(
    "**2. Recomendación sobre Reducción de Dimensiones:**\n\n"
    "Desde una perspectiva puramente estadística y de minería de datos, la distribución uniforme "
    "de la varianza (~33% por componente en PCA) demuestra que cada variable retiene información única "
    "y ortogonal. Por lo tanto, no se justifica descartar componentes en etapas posteriores de modelado."
)
import streamlit as st

st.set_page_config(page_title="PCA - PI Minería de Datos", page_icon="🧬", layout="wide")

st.title("🧬 Reducción de Dimensionalidad (PCA)")
st.markdown("---")

st.markdown("### 🛠️ Preprocesamiento Obligatorio")
st.write(
    "Antes de aplicar el Análisis de Componentes Principales (PCA), las variables numéricas fueron "
    "transformadas utilizando `StandardScaler` de scikit-learn. Este paso es fundamental y obligatorio "
    "para garantizar que todas las variables tengan media 0 y varianza 1, evitando que aquellas con "
    "magnitudes numéricas más grandes (como los minutos consumidos) distorsionen los componentes."
)

st.markdown("---")

st.markdown("### 📊 Análisis de Varianza Explicada")
st.write(
    "Al evaluar los componentes principales obtenidos, se observó que la varianza se distribuye de manera "
    "muy equitativa entre ellos (aproximadamente un 33% de la información en cada uno de los tres primeros componentes)."
)

st.warning(
    "⚠️ **Decisión Metodológica Crítica:** Debido a esta distribución uniforme de la varianza, "
    "no se recomienda eliminar ningún componente para este dataset. Reducir dimensiones en este escenario "
    "implicaría perder una cantidad de información demasiado alta y crítica para cualquier modelado posterior."
)
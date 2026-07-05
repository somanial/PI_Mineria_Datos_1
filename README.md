# PI Minería de Datos 1 - Análisis de Usuarios de Streaming

## Información General
* **Integrantes:** Alex Fernando Guerrero
* **Proyecto:** Integrador de Minería de Datos 1
* **Lugar:** Nueva Esperanza, Santiago del Estero, Argentina

## Objetivo del Proyecto
El objetivo general es analizar la calidad, consistencia y comportamiento de los usuarios en la plataforma de streaming para justificar decisiones metodológicas y de negocio. Se busca identificar patrones de uso según los planes contratados y evaluar la estructura de los datos para futuros modelados.

## Dataset
El set de datos cuenta originalmente con 8160 registros y contiene información sociodemográfica y de consumo como edad, género, tipo de plan, minutos de visualización mensuales y tickets de soporte técnico. Presenta variables categóricas con problemas de formato y registros con valores faltantes que requieren tratamiento.

## Estructura del Repositorio
El repositorio mantiene la estructura oficial con carpetas dedicadas a datos crudos y procesados, cuadernos indexados del 01 al 05, bitácora de transformaciones ETL, reportes escritos y el código fuente para el despliegue de la interfaz interactiva.

## Preparación y Calidad de Datos
Se detectaron 320 registros con valores faltantes que fueron tratados mediante imputación y borrado según el caso, logrando una retención del 96.07%. Las variables categóricas de planes y géneros presentaban inconsistencias por mayúsculas y acentos, las cuales se corrigieron con diccionarios de mapeo explícitos para asegurar la integridad de la información.

## Resumen del Análisis Exploratorio
El análisis univariado y bivariado demostró que los usuarios del Plan Premium no se concentran en un único rango etario, pero registran los mayores tiempos de visualización mensuales. El análisis multivariado evidenció que este segmento Premium genera simultáneamente la mayor cantidad de tickets de soporte técnico.

## Reducción de Dimensionalidad
Se aplicó StandardScaler sobre las variables numéricas para evitar distorsiones por diferencias de escala. El Análisis de Componentes Principales reveló que la varianza explicada se distribuye equitativamente (~33% por componente), indicando que cada variable aporta información ortogonal y única al sistema.

## Visualización Interactiva
La aplicación pública interactiva se encuentra desplegada en Streamlit Cloud. Permite explorar el comportamiento del dataset, los gráficos del EDA con sus interpretaciones y el impacto de la varianza en PCA.
* **Enlace al Repositorio y Código de la App:** https://github.com/somanial/PI_Mineria_Datos_1

## Cómo Ejecutar Localmente
1. Clonar el repositorio de GitHub.
2. Instalar las dependencias mediante: `pip install -r requirements.txt`
3. Ejecutar la aplicación interactiva con el comando: `streamlit run app/Home.py`

## Conclusiones
Se concluye que los usuarios Premium representan el segmento de mayor valor y fricción, requiriendo atención prioritaria en soporte técnico. Metodológicamente, no se recomienda reducir dimensiones mediante PCA eliminando componentes debido a la pérdida crítica de varianza distribuida.
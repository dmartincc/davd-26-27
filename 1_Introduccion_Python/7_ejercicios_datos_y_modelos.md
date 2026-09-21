## Lectura de datos y creación de modelos de ML

> Para el pipeline de calidad con `ventas.csv` y el dataset abierto `penguins.csv`, usa [`5_ejercicios_pandas.md`](5_ejercicios_pandas.md).


### E1: Lectura y escritura de CSV

- A. Lee el fichero [airports.csv](https://raw.githubusercontent.com/tidyverse/nycflights13/main/data-raw/airports.csv) a partir de una ruta relativa o absoluta (descárgalo primero si hace falta).
- B. Exporta ese fichero en diferentes formatos (JSON, Excel).
- C. Crea una función que pueda leer cualquiera de los tres formatos indicándole, al menos, la ruta del fichero.

### E2: Clasificación con variable categórica

- A. Carga el dataset `load_breast_cancer` de scikit-learn.
- B. Pásalo a DataFrame incluyendo el target.
- C. Entrena un modelo de clasificación (el que prefieras de scikit-learn).
- D. Evalúa el modelo (accuracy, precision, recall, f1-score y/o matriz de confusión).

### E3: Regresión con variable numérica

- A. Carga el dataset `load_diabetes` de scikit-learn.
- B. Pásalo a DataFrame.
- C. Entrena un modelo de regresión.
- D. Evalúa el modelo (MSE, RMSE, MAE, R²).

### E4: Clusterización

- A. Carga el dataset Wine Recognition de scikit-learn.
- B. Entrena varios modelos de clusterización (**K-Means**, **AgglomerativeClustering**, **DBSCAN**, …).
- C. Evalúa los clusters (por ejemplo, Silhouette Score).
- D. Visualiza los clusters de cada modelo.
- E. (Opcional) Entrena un clasificador usando las etiquetas de cluster como target.

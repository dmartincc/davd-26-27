# Ejercicios de Machine Learning con Scikit-Learn

Cinco ejercicios prácticos con **scikit-learn**. Compleméntalos con `7_ejercicios_datos_y_modelos.md` si quieres practicar también lectura/escritura de ficheros.

## E1: Clasificación con el dataset de vinos

A. Carga el dataset **Wine Recognition** de scikit-learn.  
B. Divide los datos en entrenamiento y prueba (70 %–30 %).  
C. Entrena un modelo **SVM** para predecir la clase de vino.  
D. Evalúa con precisión, recall, f1-score y accuracy.  
E. Visualiza la matriz de confusión.

## E2: Regresión con precios de vivienda en California

> Nota: el dataset *Boston Housing* se eliminó de scikit-learn por consideraciones éticas. Usamos **California Housing**.

A. Carga el dataset **`fetch_california_housing`** de scikit-learn.  
B. Divide los datos en entrenamiento y prueba.  
C. Entrena un modelo de **regresión lineal** (u otro regressor) para predecir el valor medio de la vivienda.  
D. Evalúa con MSE, RMSE, MAE y R².  
E. Representa gráficamente valores reales frente a predichos.

## E3: Reducción de dimensionalidad con PCA

A. Carga el dataset **Wine Recognition**.  
B. Normaliza con `StandardScaler`.  
C. Aplica **PCA** a 2 dimensiones.  
D. Representa en 2D las observaciones coloreadas por clase.  
E. Interpreta si las clases se separan visualmente tras la reducción.

## E4: Clusterización

A. Carga el dataset **Wine Recognition**.  
B. Entrena varios modelos (**K-Means**, **AgglomerativeClustering**, **DBSCAN**, …).  
C. Evalúa con métricas como **Silhouette Score**.  
D. Visualiza los clusters.  
E. (Opcional) Entrena un clasificador a partir de las etiquetas de cluster.

## E5: Datos sintéticos a partir de distribuciones

Variables: sexo (categórica), peso, estatura y BMI (numéricas).

**Suposiciones:**
- 49 % hombres y 51 % mujeres.
- Estatura hombres: media 179.3, desv. 7.0.
- Estatura mujeres: media 176.3, desv. 6.6.
- Peso hombres: media 78.9, desv. 11.8.
- Peso mujeres: media 60.4, desv. 9.7.
- BMI = Peso / (Estatura en metros)².

**Tareas:**  
A. Genera **100.000** individuos.  
B. Agrupa BMIs y explora la relación con: bajo peso (< 18.5), normal (18.5–24.9), sobrepeso (25–29.9), obesidad (≥ 30).  
C. Entrena un modelo de **regresión** para estimar el BMI.  
D. Entrena un modelo de **clasificación** que indique si una persona tiene sobrepeso o no (BMI ≥ 25).

# Ejercicios de Machine Learning con Scikit-Learn

En este documento encontrarás 5 ejercicios prácticos para aprender a utilizar la librería **Scikit-Learn (sklearn)**.  

## E1: Clasificación con el dataset de vinos
A. Descarga el dataset **Wine Recognition** de sklearn.  
B. Divide los datos en conjunto de entrenamiento y prueba (70%-30%).  
C. Entrena un modelo de **Support Vector Machine (SVM)** para predecir la clase de vino.  
D. Evalúa el modelo usando métricas de clasificación (precisión, recall, f1-score, accuracy).  
E. Visualiza los resultados con una matriz de confusión.  

## E2: Regresión con el dataset de precios de Boston
A. Descarga el dataset **Boston Housing Prices** de sklearn.  
B. Divide los datos en entrenamiento y prueba.  
C. Entrena un modelo de **Regresión Lineal** para predecir el precio medio de las viviendas.  
D. Evalúa el modelo utilizando métricas de regresión (MSE, RMSE, MAE, R²).  
E. Representa gráficamente los valores reales vs. predichos.  

## E3: Reducción de dimensionalidad con PCA
A. Descarga el dataset **Wine Recognition**.  
B. Normaliza los datos usando `StandardScaler`.  
C. Aplica **PCA (Análisis de Componentes Principales)** para reducir los datos a 2 dimensiones.  
D. Representa en un gráfico 2D las observaciones coloreadas por clase.  
E. Interpreta si los clusters se separan visualmente tras la reducción.  

## E4: Crear modelos de clusterización
A. Descarga el fichero de datos **Wine Recognition Dataset** de sklearn.  
B. Crea varios modelos de clusterización (**K-means, NearestNeighbors, DBSCAN, ...**).  
C. Evalúa los clusters de cada modelo con métricas como **Silhouette Score**.  
D. Visualiza los clusters de cada modelo.  
E. Crea modelos de clasificación a partir de los clusters generados.  

## E5: Creación de un juego de datos sintéticos a partir de distribuciones estadísticas
El juego de datos se compondrá de las siguientes variables:  
- Sexo (categórica)  
- Peso (numérica)  
- Estatura (numérica)  
- BMI (numérica)  

**Suposiciones:**  
- El 49% son hombres y el 51% mujeres.  
- Estatura hombres: media 179.3, desviación típica 7.0.  
- Estatura mujeres: media 176.3, desviación típica 6.6.  
- Peso hombres: media 78.9, desviación típica 11.8.  
- Peso mujeres: media 60.4, desviación típica 9.7.  
- BMI = Peso / Estatura².  

**Tareas:**  
A. Crea **100.000 individuos** y sus variables.  
B. Clusteriza sus **BMIs** y explora si existe relación con las categorías:  
   - Bajo peso = menos de 18.5  
   - Peso normal = 18.5–24.9  
   - Sobrepeso = 25–29.9  
   - Obesidad = BMI ≥ 30  
C. Crea un modelo de **regresión** que calcule el BMI.  
D. Crea un modelo de **clasificación** que indique si una persona tiene sobrepeso o no.  

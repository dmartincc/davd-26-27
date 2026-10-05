# Ejercicios de visualización — datos sintéticos (BMI)

**Asignatura:** DAVD · Tema 1  
**Referencia de clase:** [`8_visualizaciones_sencillas.ipynb`](8_visualizaciones_sencillas.ipynb)  
**Dataset:** el generado en **E5** de [`7_ejercicios_modelos.md`](7_ejercicios_modelos.md) (sexo, peso, estatura, BMI)

> Si aún no tienes el DataFrame, genera **N = 10_000** individuos (para explorar en clase; el E5 de modelos pide 100_000). Usa `random_state=42` para que sea reproducible.

**Suposiciones (iguales que E5):**

- 49 % hombres y 51 % mujeres  
- Estatura hombres: media 179.3 cm, desv. 7.0  
- Estatura mujeres: media 176.3 cm, desv. 6.6  
- Peso hombres: media 78.9 kg, desv. 11.8  
- Peso mujeres: media 60.4 kg, desv. 9.7  
- `BMI = peso_kg / (estatura_m ** 2)`  
- Categoría BMI: bajo peso (&lt; 18.5), normal (18.5–24.9), sobrepeso (25–29.9), obesidad (≥ 30)

---

## Preparación

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

rng = np.random.default_rng(42)
N = 10_000
# ... genera sexo, estatura_cm, peso_kg, bmi, categoria_bmi
```

Checklist del DataFrame:

- columnas: `sexo`, `estatura_cm`, `peso_kg`, `bmi`, `categoria_bmi`
- `sexo` ∈ `{hombre, mujer}` (o `H`/`M`, pero sé consistente)
- sin BMI negativos; revisa nulos

---

## V1 — Distribuciones (histogramas) — 8 min

A. Histograma de `bmi` con KDE (Seaborn).  
B. El mismo histograma **separado por `sexo`** (`hue`).  
C. Histograma de `peso_kg` en horizontal (Matplotlib o Seaborn).  
D. Escribe 2 frases: ¿dónde se concentran los BMI? ¿hay diferencias claras por sexo?

---

## V2 — Comparar categorías (barras y conteos) — 8 min

A. `countplot` de `categoria_bmi` (orden: bajo peso → obesidad).  
B. Barras de **conteo** de `categoria_bmi` con `hue="sexo"`.  
C. Barras de la **media de `bmi`** por `sexo` (`barplot` + `estimator=np.mean`).  
D. ¿Qué categoría domina? ¿El mensaje cambiaría en un dashboard de salud?

---

## V3 — Relaciones (scatter y boxplot) — 8 min

A. Scatter `estatura_cm` vs `peso_kg` coloreado por `sexo`.  
B. Scatter `estatura_cm` vs `bmi` coloreado por `categoria_bmi` (muestra 2_000 puntos si va lento: `.sample(2000, random_state=42)`).  
C. Boxplot de `bmi` por `sexo`.  
D. Boxplot de `peso_kg` por `categoria_bmi`.  
E. Comenta un posible **outlier** visual y si lo filtrarías antes de un modelo.

---

## V4 — Composición (pie con criterio) — 4 min

A. Pie chart de la proporción de `categoria_bmi` (máx. 4 sectores).  
B. Incluye `%` en las etiquetas (`autopct`).  
C. Justifica en una línea por qué aquí el pie **sí** o **no** es mejor que un `countplot`.

---

## V5 — Mini dashboard estático (subplots) — 10 min

Construye una figura **2×2** (`plt.subplots`) con título general *"Perfil sintético BMI"*:

| Panel | Contenido |
| --- | --- |
| (0,0) | Histograma `bmi` por sexo |
| (0,1) | Count de `categoria_bmi` |
| (1,0) | Scatter estatura–peso por sexo |
| (1,1) | Boxplot `bmi` por sexo |

Requisitos: títulos de cada eje, `tight_layout()`, leyendas donde hagan falta.

---

## V6 — Puente a modelos (opcional)

Usando el mismo dataset:

A. Scatter de **BMI real vs BMI predicho** por tu regressor del E5 (si ya lo entrenaste).  
B. Barras o heatmap simple de la **matriz de confusión** del clasificador sobrepeso sí/no.  
C. Una frase: qué gráfico enseñarías primero a un usuario no técnico en un Dash.

---

## Entrega orientativa

- Notebook o script con los gráficos de **V1–V5**.  
- DataFrame generado con `random_state=42` (o semilla documentada).  
- Breve markdown (5–10 líneas) interpretando los hallazgos.

## Hecho cuando…

- [ ] DataFrame sintético reproducible  
- [ ] Al menos un histograma, un count/bar, un scatter, un boxplot y un grid 2×2  
- [ ] Ejes y títulos legibles (no figuras “mudas”)  
- [ ] Interpretación escrita de 2–3 hallazgos  

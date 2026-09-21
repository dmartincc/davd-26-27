# E1 — Procesamiento de datos con pandas (30–45 min)

**Asignatura:** DAVD · Tema 1  
**Referencia de clase:** [`5_lectura_de_datos.ipynb`](5_lectura_de_datos.ipynb)

Hay **dos datasets**. El de ventas es el núcleo (obligatorio). El de pingüinos es un **juego de datos abiertos** para practicar el mismo flujo sobre datos reales.

| Dataset | Fichero | Tipo |
| --- | --- | --- |
| A — Ventas | [`Datos/ventas.csv`](Datos/ventas.csv) | Sintético del curso |
| B — Pingüinos | [`Datos/penguins.csv`](Datos/penguins.csv) | Abierto (Palmer Penguins) |

Origen de B: documentado en [`Datos/README.md`](Datos/README.md).

## Preparación (antes de arrancar)

```bash
cd 1_Introduccion_Python
# puedes trabajar en celdas nuevas al final de 5_lectura_de_datos.ipynb
# o en un script propio (p. ej. ejercicios_solucion_pandas.py)
```

---

## Dataset A — Ventas (obligatorio)

### Parte A1 — Diagnóstico (8 min)

1. Carga el CSV con `pathlib.Path` (sin rutas absolutas hardcodeadas).
2. Imprime `shape`, `dtypes` y `isna().sum()`.
3. Lista por escrito (comentario o markdown) **qué filas parecen inválidas** y por qué.

### Parte A2 — Validación (10 min)

Implementa:

```python
def validar_ventas(frame: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    ...
```

Reglas mínimas:

- `unidades` numérica y `> 0`
- `precio_unitario` numérico y `> 0`
- columna derivada: `importe = unidades * precio_unitario` solo en válidos

Devuelve `(validos, errores)`.

**Checkpoint A:** **140 válidas** y **10 inválidas**.

### Parte A3 — Agregaciones (8 min)

Sobre `validos` (KPIs típicos de un cuadro de mando):

1. Importe total por `region` (ordenado desc).
2. Top 3 `producto` por importe.
3. `cliente_id` con más de una compra.

### Parte A4 — Exportación (4 min)

Escribe:

- `Datos/ventas_limpias.csv`
- `Datos/calidad_ventas.json` con:
  - `filas_totales`, `filas_validas`, `filas_invalidas`, `importe_total`

---

## Dataset B — Pingüinos (datos abiertos, obligatorio)

Repite el **mismo patrón** sobre [`Datos/penguins.csv`](Datos/penguins.csv).

### Parte B1 — Diagnóstico

1. Carga con `Path`.
2. `shape`, `dtypes`, `isna().sum()`.
3. Anota qué columnas tienen nulos y cómo afectan a un dashboard.

### Parte B2 — Validación

Implementa:

```python
def validar_penguins(frame: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    ...
```

Reglas mínimas:

- `bill_length_mm`, `bill_depth_mm`, `flipper_length_mm`, `body_mass_g` numéricos y `> 0`
- `sex` ∈ `{MALE, FEMALE}` (tras normalizar mayúsculas si hace falta)
- `species` e `island` no nulos

Devuelve `(validos, errores)`.

**Checkpoint B:** **333 válidas** y **11 inválidas**.

### Parte B3 — Agregaciones (para viz / Dash)

Sobre `validos`:

1. Masa corporal media (`body_mass_g`) por `species`.
2. Conteo por `island` y `sex`.
3. Top 5 filas con mayor `flipper_length_mm`.

### Parte B4 — Exportación

Escribe:

- `Datos/penguins_limpios.csv`
- `Datos/calidad_penguins.json` con:
  - `filas_totales`, `filas_validas`, `filas_invalidas`, `body_mass_mean`

---

## Extensión si terminas pronto

- En ventas: `fecha` como `datetime` y agregado por semana.
- En pingüinos:`body_mass_g` por `species`.
- Refactoriza ambos flujos en `cargar` / `validar` / `agregar` / `exportar`.

## Entrega orientativa

Código en tu repo del proyecto + evidencia de **ambos** JSON de calidad (`calidad_ventas.json` y `calidad_penguins.json`).

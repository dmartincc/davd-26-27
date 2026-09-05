# API de análisis de sentimiento con Flask

API sencilla con Flask + Flask-RESTful que clasifica opiniones con un modelo de Hugging Face Transformers.

## Requisitos

- Python 3.10+
- Entorno virtual recomendado

## Instalación

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

> La primera ejecución descargará el modelo `nlptown/bert-base-multilingual-uncased-sentiment` (puede tardar y ocupar espacio en disco).

## Arranque

```bash
python app.py
```

La API queda en http://127.0.0.1:5000/

## Endpoints

| Método | Ruta | Descripción |
| --- | --- | --- |
| `GET` | `/sentiment/<review_id>` | Obtiene una opinión (usa `0` o ajusta el recurso para listar todas) |
| `PUT` | `/sentiment/<review_id>` | Crea/actualiza una opinión y calcula el sentimiento |
| `DELETE` | `/sentiment/<review_id>` | Elimina una opinión |

Parámetros del `PUT`: `name` (obligatorio), `review` (obligatorio), `rating` (opcional).

## Ejemplo

```bash
curl -X PUT http://127.0.0.1:5000/sentiment/1 \
  -d "name=Juan" \
  -d "review=Este es un gran producto" \
  -d "rating=5"
```

Respuesta típica:

```json
{
  "name": "Juan",
  "review": "Este es un gran producto",
  "rating": 5,
  "prediction": "5",
  "probability": 0.98,
  "timestamp": "2026-10-27 14:52:03.123456"
}
```

También puedes probar con `python test.py`.

## Personalización

Cambia el parámetro `model` en `transformers.pipeline(...)` dentro de `app.py` para usar otro modelo de Hugging Face.

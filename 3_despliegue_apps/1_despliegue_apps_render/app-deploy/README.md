# Ejemplo de despliegue Dash en Render

Plantilla mínima con `app.py`, `Procfile`, `requirements.txt` y `render.yaml`.

```bash
pip install -r requirements.txt
python app.py
```

En producción, Gunicorn usa el objeto `server` expuesto por Dash (`app.server`).

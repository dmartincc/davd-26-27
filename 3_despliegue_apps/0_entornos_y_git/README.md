# 0 — Entornos virtuales y Git/GitHub (DAVD)

Material base del Tema 3 para montar un entorno reproducible y versionar el código **antes** de desplegar en Render o publicar APIs.

| Recurso | Descripción |
| --- | --- |
| [`01_entornos_y_git.md`](01_entornos_y_git.md) | Guía amplia (teoría, demos, troubleshooting) |
| [`ejercicios/E0_entornos_git.md`](ejercicios/E0_entornos_git.md) | Checklist práctico |
| [`ejemplos/check_entorno.py`](ejemplos/check_entorno.py) | Verifica venv + Dash/Plotly/pandas |
| [`ejemplos/gitignore_davd.txt`](ejemplos/gitignore_davd.txt) | Plantilla `.gitignore` para el proyecto |

## Arranque rápido

Desde la raíz de `davd-26-27`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r 2_app_visualizaciones/requirements.txt
python 3_despliegue_apps/0_entornos_y_git/ejemplos/check_entorno.py --strict
```

## Orden en el Tema 3

1. **`0_entornos_y_git/`** ← estás aquí  
2. `1_despliegue_apps_render/` — Dash en Render  
3. `2_creacion_api_rest/` — API Flask  
4. `3_aws_serverless_api_rest/` — Serverless en AWS  

También relacionado: ejercicio Git+Dash en `2_app_visualizaciones/4_dash_git_ejercicio.md`.

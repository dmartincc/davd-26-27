# E0 — Entornos virtuales y Git/GitHub (DAVD)

**Referencia:** [`../01_entornos_y_git.md`](../01_entornos_y_git.md)  
**Repo del curso:** https://github.com/dmartincc/davd-26-27

## Checklist rápido

1. Clona el curso y crea el venv:

```bash
git clone git@github.com:dmartincc/davd-26-27.git
cd davd-26-27
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r 2_app_visualizaciones/requirements.txt
```

2. Verifica el entorno:

```bash
python 3_despliegue_apps/0_entornos_y_git/ejemplos/check_entorno.py --strict
```

3. Crea tu repo personal `davd-26-27-apellido-nombre` (proyecto de aplicación).

4. Copia la plantilla de ignore:

```bash
cp 3_despliegue_apps/0_entornos_y_git/ejemplos/gitignore_davd.txt .gitignore
```

(en tu repo personal; ajusta la ruta si copias el fichero)

5. Rama `practica/entornos-git`, `README.md` del proyecto + notas, commit y **Pull Request** a `main`.

6. (Opcional) Arranca Dash:

```bash
cd 2_app_visualizaciones
python 2_Introduccion_a_Dash.py
# http://127.0.0.1:8050/
```

## Hecho cuando…

- `check_entorno.py --strict` → `ENTORNO OK`
- Repo personal en GitHub con `.gitignore` (sin `.venv` / `.env`)
- Al menos un PR o commits visibles
- Sabes explicar working tree / staging / commit / remoto

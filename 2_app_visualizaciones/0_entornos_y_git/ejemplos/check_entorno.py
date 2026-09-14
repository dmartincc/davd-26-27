"""Comprueba que el entorno DAVD está activo y usable (Dash / Plotly / pandas).

Uso (desde la raíz del repo davd-26-27, con venv activo):

  python 3_despliegue_apps/0_entornos_y_git/ejemplos/check_entorno.py
  python 3_despliegue_apps/0_entornos_y_git/ejemplos/check_entorno.py --strict
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Chequeo de entorno DAVD")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exige que sys.executable viva dentro de un directorio .venv",
    )
    args = parser.parse_args()

    print("Python:", sys.version.split()[0])
    print("Executable:", sys.executable)

    in_venv = ".venv" in sys.executable.replace("\\", "/")
    if not in_venv:
        msg = "parece que no estás usando .venv"
        if args.strict:
            print("FALLO:", msg)
            print("Activa primero: source .venv/bin/activate  (Windows: .venv\\Scripts\\activate)")
            return 2
        print("AVISO:", msg, "(continúo igual; usa --strict para exigirlo)")

    try:
        import dash
        import pandas as pd
        import plotly
    except ImportError as exc:
        print("FALLO: falta dependencia —", exc)
        print("Ejecuta (con venv activo):")
        print("  pip install -r 2_app_visualizaciones/requirements.txt")
        return 1

    # ejemplos/ -> 0_entornos_y_git/ -> 3_despliegue_apps/ -> repo root
    root = Path(__file__).resolve().parents[3]
    req = root / "2_app_visualizaciones" / "requirements.txt"
    if not req.exists():
        print("FALLO: no encuentro 2_app_visualizaciones/requirements.txt en", root)
        return 1

    print(f"Repo root: {root}")
    print(f"dash={dash.__version__} | plotly={plotly.__version__} | pandas={pd.__version__}")
    print("VIRTUAL_ENV:", os.environ.get("VIRTUAL_ENV", "(no definido)"))
    print("ENTORNO OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

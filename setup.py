# Biblioteca
import sys
from cx_Freeze import setup, Executable

# Dependências que serão detectadas (biblioteca adicional que será agregado ao exe)
build_exe_options = {"packages": ["os"], "includes": ["tableauserverclient", "tableauhyperapi", "glob", "logging", "shutil", "zipfile", "pandas", "datetime"]}

# Caso sua aplicação tenha interpretação gráfica
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Tableau",
    version = "0.1",
    description = "Minha aplicação de coleta de dados via Tableau.",
    options = {"build_exe": build_exe_options},
    executables = [Executable("Tableau.py", base=base)]
)
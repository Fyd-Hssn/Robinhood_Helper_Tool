# This file was used for the CxFreeze build, but is not currently in use for the final build
import sys
from cx_Freeze import setup, Executable
from datetime import date, datetime

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["os"],
    "include_files": ["config.py", "RS_Helper.py", "app_functions.py", "Robinhood_Logo.ico"],
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Robinhood Tool",
    version="0.1",
    description="My GUI application!",
    options={"build_exe": build_exe_options},
    executables=[Executable("RH_Tool.py", base=base)],
)

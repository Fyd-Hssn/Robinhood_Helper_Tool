import sys
from cx_Freeze import setup, Executable
from datetime import date, datetime

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="Robinhood Tool",
      version="0.1",
      description="My GUI application!",
      options={"build_exe": {"include_files": ['config.py',
                                               'RS_Helper.py', 'SP500_Tickers.py']}},
      executables=[Executable("application.py", base=base)])

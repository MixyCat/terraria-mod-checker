:: This script creates a standalone executable for the Terraria Modlist Checker using PyInstaller.
@echo off
:: Change directory to the location of the batch file.
cd /d %~dp0

:: Set pyinstaller executable.
set pyinstaller_exe=.\.venv\Scripts\pyinstaller.exe

:: Run the pyinstaller from there.
echo Running pyinstaller...
%pyinstaller_exe% main.py --name terraria-modlist-checker ^
    --onefile
@echo off
cd /d "D:\workspace\python\fast_api"
call .venv\Scripts\activate.bat
fastapi run main.py
call .venv\Scripts\deactivate.bat
pause
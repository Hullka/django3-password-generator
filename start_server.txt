@echo off
start /B python manage.py runserver
timeout /t 3 /nobreak >nul
browser-sync start --proxy "127.0.0.1:8000" --files "**/*"

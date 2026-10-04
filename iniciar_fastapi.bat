@echo off
echo Iniciando FastAPI - Sistema de Agenda Empresarial en http://127.0.0.1:8000
echo Documentacion Swagger disponible en http://127.0.0.1:8000/docs
echo Panel Web Jinja2 disponible en http://127.0.0.1:8000/views/agenda
call venv\Scripts\activate
uvicorn main:app --reload --host 0.0.0.0 --port 8000
pause

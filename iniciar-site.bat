@echo off
title Camping Chapeu de Sol - Servidor Local
echo ==============================================
echo   Iniciando servidor local Camping Chapeu de Sol
echo ==============================================
echo.
echo Abrindo o navegador em http://localhost:8080 ...
start http://localhost:8080
echo.
echo Servidor rodando! Para encerrar, feche esta janela.
python -m http.server 8080
pause

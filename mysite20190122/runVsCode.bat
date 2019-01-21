@echo off
cd /d %~dp0
call ".\env\Scripts\activate.bat"

rem start /b code .
rem start code .

call code .

rem exit


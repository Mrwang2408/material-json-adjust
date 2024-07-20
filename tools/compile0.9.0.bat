@echo off
::cd tmp
java -jar MaterialBinTool-0.9.0-all.jar -t 2 -c -o .\ .\include\*.json
timeout -t 2 -nobreak
pause
@echo off
cd tmp
java -jar ..\MaterialBinTool-0.8.2-all.jar -u .\*.material.bin -o .\src\
timeout -t 3 -nobreak
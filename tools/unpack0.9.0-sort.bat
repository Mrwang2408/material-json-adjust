@echo off
cd tmp
java -jar ..\MaterialBinTool-0.9.0-all.jar -u .\*.material.bin -o .\src\ --sort-variants
timeout -t 3 -nobreak
@echo off
cd tmp
cd src
java -jar ..\..\MaterialBinTool-0.6.0-all.jar -r * -o ..\
timeout -t 3 -nobreak
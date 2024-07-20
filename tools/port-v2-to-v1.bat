@echo off
setlocal enabledelayedexpansion

if exist src\ (
	rd /s /q .\src\
	echo Cleaning temp folder \src
	)
if exist *.material.bin (
	del .\*.material.bin
	echo Cleaning temp file material.bin
	)
echo.

set n=0
set input=folders
set /p input=Drag or Input a folder here:  

for /r %input% %%i in (*.material.bin) do (
	set /a n+=1
	echo.
	copy /y %%i %%~nxi >nul
	echo Opening !n!th file...
	java -jar MaterialBinTool-0.9.0-unofficial.jar -u .\%%~nxi -o .\src\
	if not exist src\ (
		set /a n-=1
		echo Error.
		del %%~nxi
		goto end
	)
	cd src
	for /d %%f in (*) do (
		set l=0
		for /f "delims=*" %%d in (%%f\%%f.json) do (
			set /a l+=1
			if "%%d" == "  "formatVersion": "V2"," (
				echo   "formatVersion": "V1",>> tmp.json
			) else (
				echo %%d>> tmp.json
			)
		)
		echo processed !l! lines
		copy /y tmp.json %%f\%%f.json >nul
		del tmp.json
	)
	cd ..	
	java -jar MaterialBinTool-0.8.2-all.jar -r .\src\* -o .\ 
	echo OK.
	copy /y %%~nxi %%i >nul
	del %%~nxi
	rd /s /q .\src\
)

:end
echo.
echo.
echo Success. %n% files in total
echo.
timeout -t 2 >nul
pause



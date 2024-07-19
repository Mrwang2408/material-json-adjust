@echo off
chcp 65001 > nul
title echo_0_100
	echo.
	echo ============
	echo by Mrwang2408
	echo ============
	echo.
	set a=0
	echo 当前目录：%~dp0
	echo 即将遍历目录下所有 *.ESSL_100.* 并替换为空文件
pause
	for /r "%~dp0" %%i in (*.ESSL_100.*) do (
		type nul >%%i
		echo %%i
		set /a a+=1
	)
echo.
echo 完毕！一共遍历了%a%个文件
echo.
pause
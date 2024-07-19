@echo off
chcp 65001 > nul
echo 确定仅保留两个essl100吗
pause
python leave_100.py
timeout /t 3 /nobreak
pause
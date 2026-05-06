@echo off
setlocal EnableDelayedExpansion

rem --------- 1. 清理旧产物 ----------
if exist release rmdir /s /q release
mkdir release

rem --------- 2. 复制必要文件 ----------
xcopy /y /i ui.html release\
xcopy /y /i style.css release\
xcopy /y /i script.js release\
xcopy /y /i deepseek_ui.bat release\
xcopy /y /i README.md release\
xcopy /y /i .gitignore release\

rem --------- 3. 生成 zip ----------
powershell -Command "Compress-Archive -Path release\* -DestinationPath release\deepseek-anti-ai-agent.zip -Force"

echo.
echo 打包完成：release\deepseek-anti-ai-agent.zip
pause

chcp 65001
@echo off
title Giải Mã RGSS3A(Fux2Pack)
:a

::set python=D:\Softs\Programme\Python\python.exe
::set Fux2Pack=D:\Softs\Programme\Python\WWW\Fux2Pack.py

set /p python=Kéo thả "python.exe" vào và nhấn Enter:
set /p Fux2Pack=Kéo thả "Fux2Pack.py" vào và nhấn Enter:

set /p rgss3a=Kéo thả "Game.rgss3a" vào và nhấn Enter:
%python% %Fux2Pack% %rgss3a%
echo Nhấn phím bất kỳ để bắt đầu lại, nhấn x để đóng
pause>nul
cls
goto a
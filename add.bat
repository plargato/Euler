echo off
set DIR=00%1
set DIR=%DIR:~-3%
mkdir %DIR%
copy template.py %DIR%\solve.py
cd %DIR%

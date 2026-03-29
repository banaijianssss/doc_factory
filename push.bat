@echo off
echo ========================================
echo 智能文档工厂 - Git推送脚本
echo ========================================
echo.
echo 仓库地址: https://github.com/banaijianssss/doc_factory
echo.

cd /d C:\Users\lovez\Desktop\doc-factory

echo [1/2] 检查远程仓库...
git remote -v
echo.

echo [2/2] 推送到GitHub...
git push origin main

if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo 推送成功！
    echo ========================================
    echo.
    echo 请访问：https://github.com/banaijianssss/doc_factory
) else (
    echo.
    echo ========================================
    echo 推送失败
    echo ========================================
    echo.
    echo 可能原因：
    echo 1. 网络连接问题
    echo 2. GitHub认证问题
    echo.
    echo 请稍后重试，或更换网络环境
)

echo.
pause

@echo off
chcp 65001
echo ========================================
echo 智能文档工厂 - Git推送重试工具
echo ========================================
echo.

set retry_count=0
set max_retries=5

:retry
echo [%retry_count%/%max_retries%] 尝试推送到GitHub...
git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo 推送成功！
    echo ========================================
    echo.
    echo 下一步：访问 https://railway.app 部署
    pause
    exit /b 0
) else (
    set /a retry_count+=1
    if %retry_count% lss %max_retries% (
        echo.
        echo 推送失败，5秒后重试...
        timeout /t 5 /nobreak >nul
        goto retry
    ) else (
        echo.
        echo ========================================
        echo 推送失败，已达到最大重试次数
echo ========================================
        echo.
        echo 可能的原因：
        echo 1. 网络连接问题
        echo 2. GitHub认证问题
        echo 3. 防火墙阻止
        echo.
        echo 解决方案：
        echo 1. 查看 UPLOAD_TO_GITHUB.md 手动上传
        echo 2. 使用GitHub Desktop
        echo 3. 设置代理后重试
        echo.
        pause
        exit /b 1
    )
)

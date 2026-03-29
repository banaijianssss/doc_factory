@echo off
chcp 65001
cls
echo ========================================
echo 智能文档工厂 - 一键部署工具
echo ========================================
echo.

echo [1/3] 检查Git配置...
git config --global user.email "docfactory@example.com"
git config --global user.name "Doc Factory"
echo OK
echo.

echo [2/3] 推送到GitHub...
git push -u origin main
if %errorlevel% neq 0 (
    echo.
    echo 推送失败，请检查：
    echo 1. 网络连接是否正常
    echo 2. GitHub仓库是否存在
    echo 3. 是否需要配置Personal Access Token
    echo.
    echo 查看 GITHUB_PUSH_GUIDE.md 获取详细帮助
    pause
    exit /b 1
)
echo OK
echo.

echo [3/3] 部署完成！
echo.
echo ========================================
echo 推送成功！
echo ========================================
echo.
echo 下一步：
echo 1. 访问 https://railway.app
echo 2. 点击 "New Project" 
echo 3. 选择 "Deploy from GitHub repo"
echo 4. 选择 doc_factory 仓库
echo 5. 等待部署完成（2-5分钟）
echo.
echo 查看 RAILWAY_DEPLOY.md 获取详细指南
echo.
pause

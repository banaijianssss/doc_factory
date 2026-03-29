#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
智能文档工厂 - GitHub推送助手
功能：自动创建git仓库并推送到GitHub
"""

import os
import subprocess

def run_cmd(cmd, description):
    """运行命令并输出结果"""
    print(f"\n[{description}]")
    print(f"$ {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("OK")
        if result.stdout:
            print(result.stdout)
    else:
        print(f"Error: {result.stderr}")
    return result.returncode == 0

def main():
    print("="*50)
    print("智能文档工厂 - GitHub推送助手")
    print("="*50)
    
    # 检查git是否安装
    if not run_cmd("git --version", "检查Git安装"):
        print("\n请先安装Git: https://git-scm.com/download")
        return
    
    # 初始化git仓库
    if not os.path.exists('.git'):
        run_cmd("git init", "初始化Git仓库")
    
    # 创建.gitignore
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
*.manifest
*.spec

# 虚拟环境
venv/
ENV/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo

# 上传的文件
uploads/*
!uploads/.gitkeep

# 生成的文件
output/*
!output/.gitkeep
custom_templates/*
!custom_templates/.gitkeep

# 发布版本
发布版本/
"""
    
    with open('.gitignore', 'w', encoding='utf-8') as f:
        f.write(gitignore_content)
    print("\n[OK] 创建 .gitignore")
    
    # 创建keep文件
    for folder in ['uploads', 'output', 'custom_templates']:
        keep_file = os.path.join(folder, '.gitkeep')
        if not os.path.exists(folder):
            os.makedirs(folder)
        if not os.path.exists(keep_file):
            with open(keep_file, 'w') as f:
                pass
    
    # 添加文件
    run_cmd("git add .", "添加文件到暂存区")
    
    # 提交
    run_cmd('git commit -m "Initial commit: 智能文档工厂 v2.1"', "提交代码")
    
    print("\n" + "="*50)
    print("本地仓库准备完成！")
    print("="*50)
    print("\n下一步：推送到GitHub")
    print("1. 在GitHub创建新仓库（不要初始化）")
    print("2. 运行以下命令：")
    print("\n   git remote add origin https://github.com/你的用户名/doc-factory.git")
    print("   git branch -M main")
    print("   git push -u origin main")
    print("\n3. 访问Railway.app部署")
    print("\n详细步骤查看 RAILWAY_DEPLOY.md")

if __name__ == '__main__':
    main()

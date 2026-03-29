#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
智能文档工厂 - Railway部署助手
功能：生成Railway部署所需的配置文件
"""

import os

def create_railway_config():
    """创建Railway部署配置"""
    
    # 创建 nixpacks.toml 配置
    nixpacks_content = """[phases.build]
cmds = ["pip install -r requirements.txt"]

[phases.setup]
nixPkgs = ["python311"]

[start]
cmd = "python app_v2.py"
"""
    
    with open('nixpacks.toml', 'w', encoding='utf-8') as f:
        f.write(nixpacks_content)
    
    print("[OK] 创建 nixpacks.toml")
    
    # 创建 Procfile
    procfile_content = "web: python app_v2.py"
    
    with open('Procfile', 'w', encoding='utf-8') as f:
        f.write(procfile_content)
    
    print("[OK] 创建 Procfile")
    
    # 更新 railway.json
    railway_config = {
        "$schema": "https://railway.app/railway.schema.json",
        "build": {
            "builder": "NIXPACKS"
        },
        "deploy": {
            "startCommand": "python app_v2.py",
            "healthcheckPath": "/",
            "healthcheckTimeout": 100,
            "restartPolicyType": "ON_FAILURE",
            "restartPolicyMaxRetries": 10
        }
    }
    
    import json
    with open('railway.json', 'w', encoding='utf-8') as f:
        json.dump(railway_config, f, indent=2)
    
    print("[OK] 更新 railway.json")
    
    # 创建部署说明
    readme_content = """# Railway部署指南

## 一键部署步骤

### 1. 准备代码
确保以下文件已准备好：
- app_v2.py
- requirements.txt
- templates/index_v2.html
- nixpacks.toml
- Procfile
- railway.json

### 2. 推送到GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/你的用户名/doc-factory.git
git push -u origin main
```

### 3. Railway部署
1. 访问 https://railway.app
2. 点击 "New Project"
3. 选择 "Deploy from GitHub repo"
4. 选择你的仓库
5. 点击 "Deploy"
6. 等待部署完成（约2-3分钟）

### 4. 获取公网地址
部署完成后，Railway会自动分配一个域名：
- 格式：`https://doc-factory-xxx.up.railway.app`
- 在Dashboard中查看

### 5. 自定义域名（可选）
1. 在Railway Dashboard中点击你的项目
2. 进入 Settings → Domains
3. 点击 "Generate Domain" 或添加自定义域名

## 免费额度
- Railway提供免费额度：每月$5
- 足够支撑小型应用运行
- 超过额度后会暂停，下个月自动恢复

## 注意事项
- 文件上传功能在免费版可能受限
- 建议用于演示和小规模使用
- 生产环境建议升级付费版

---
部署完成！
"""
    
    with open('RAILWAY_DEPLOY.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("[OK] 创建 RAILWAY_DEPLOY.md")
    
    print("\n" + "="*50)
    print("Railway部署配置已生成！")
    print("="*50)
    print("\n下一步：")
    print("1. 将代码推送到GitHub")
    print("2. 访问 https://railway.app 部署")
    print("3. 查看 RAILWAY_DEPLOY.md 获取详细指南")


if __name__ == '__main__':
    create_railway_config()

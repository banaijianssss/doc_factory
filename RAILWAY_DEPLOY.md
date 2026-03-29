# Railway部署指南

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

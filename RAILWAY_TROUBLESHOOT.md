# Railway部署问题排查指南

## 问题：Railway显示"没有找到仓库"

## 解决方案

### 方案1：检查GitHub仓库权限

1. 访问 https://github.com/banaijianssss/doc_factory
2. 确认仓库是 **Public**（公开）
3. 如果不是，点击 Settings → Change visibility → Make public

### 方案2：重新授权Railway

1. 访问 https://github.com/settings/applications
2. 找到 "Railway"
3. 点击 "Revoke access"（撤销授权）
4. 重新登录 https://railway.app
5. 重新授权GitHub访问

### 方案3：手动导入仓库

如果自动检测不到，可以手动导入：

1. 在Railway点击 "New Project"
2. 选择 "Deploy from GitHub repo"
3. 点击 "Configure GitHub App"
4. 选择 "All repositories" 或手动选择 `doc_factory`
5. 返回Railway刷新页面

### 方案4：使用Railway CLI部署

1. 安装Railway CLI：
   ```bash
   npm install -g @railway/cli
   ```

2. 登录Railway：
   ```bash
   railway login
   ```

3. 进入项目目录并部署：
   ```bash
   cd doc-factory
   railway init
   railway up
   ```

### 方案5：使用Docker部署

1. 在Railway创建新项目
2. 选择 "Empty Project"
3. 点击 "New" → "Dockerfile"
4. 选择 "GitHub Repo"
5. 选择 `banaijianssss/doc_factory`

### 方案6：备选部署平台

如果Railway始终无法部署，可以尝试：

#### 方案A：部署到Render
1. 访问 https://render.com
2. 点击 "New Web Service"
3. 连接GitHub仓库
4. 选择Python环境
5. 启动命令：`python app_v2.py`

#### 方案B：部署到Heroku
1. 访问 https://heroku.com
2. 创建新应用
3. 连接GitHub部署
4. 自动识别Python项目

#### 方案C：部署到Fly.io
1. 安装Fly CLI
2. 运行 `fly launch`
3. 自动部署

---

## 快速检查清单

- [ ] GitHub仓库是公开的
- [ ] Railway有GitHub访问权限
- [ ] 仓库包含 `requirements.txt`
- [ ] 仓库包含 `Procfile`
- [ ] GitHub账号已登录Railway

---

## 联系支持

如果以上方法都无效：
1. Railway Discord: https://discord.gg/railway
2. Railway支持: https://railway.app/help
3. 或尝试其他部署平台

---

## 临时解决方案

如果公网部署暂时无法实现，可以：
1. 使用本地exe文件提供服务
2. 通过TeamViewer远程操作
3. 等待网络问题解决后再部署

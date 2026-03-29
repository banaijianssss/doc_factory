# GitHub推送指南

## 当前状态

✅ Git仓库已初始化
✅ 所有文件已提交（23个文件）
✅ 远程仓库已配置

## 手动推送步骤

由于网络原因，请按以下步骤手动推送：

### 步骤1：打开命令行
在 `doc-factory` 文件夹中，右键点击 "Git Bash Here" 或打开PowerShell

### 步骤2：检查远程仓库
```bash
git remote -v
```

应该显示：
```
origin  https://github.com/lovez/doc_factory.git (fetch)
origin  https://github.com/lovez/doc_factory.git (push)
```

### 步骤3：推送到GitHub
```bash
git push -u origin main
```

如果提示输入用户名密码：
- 用户名：你的GitHub用户名
- 密码：使用Personal Access Token（不是登录密码）

### 步骤4：验证推送
访问：https://github.com/lovez/doc_factory
确认文件已上传

---

## Railway部署步骤

### 1. 登录Railway
访问：https://railway.app
使用GitHub账号登录

### 2. 创建新项目
1. 点击 "New Project"
2. 选择 "Deploy from GitHub repo"
3. 选择 `doc_factory` 仓库
4. 点击 "Deploy"

### 3. 等待部署
- 部署时间：2-5分钟
- 会自动识别Python项目并安装依赖

### 4. 获取域名
部署完成后：
1. 点击项目进入Dashboard
2. 点击 "Settings" → "Domains"
3. 点击 "Generate Domain"
4. 获得类似 `https://doc-factory-xxx.up.railway.app` 的地址

### 5. 访问公网地址
在浏览器中打开分配的域名即可使用！

---

## 常见问题

### Q: 推送时提示认证失败？
A: 需要使用Personal Access Token
1. 访问 https://github.com/settings/tokens
2. 点击 "Generate new token"
3. 选择 "repo" 权限
4. 复制token作为密码使用

### Q: Railway部署失败？
A: 检查以下几点：
- 确认 requirements.txt 存在
- 确认 Procfile 格式正确
- 查看Railway日志排查错误

### Q: 如何更新部署？
A: 推送新代码到GitHub后，Railway会自动重新部署

---

## 部署成功后的地址

部署完成后，你将获得：
- **公网地址**：`https://doc-factory-xxx.up.railway.app`
- **分享给他人**：任何人都可以访问
- **长期使用**：免费额度内可持续运行

---

## 下一步

1. 推送代码到GitHub
2. Railway自动部署
3. 获得公网地址
4. 分享给客户使用！

祝部署顺利！🚀

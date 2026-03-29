# Railway部署步骤

## ✅ 代码已推送到GitHub

仓库地址：https://github.com/banaijianssss/doc_factory

## 部署步骤

### 步骤1：登录Railway
1. 访问 https://railway.app
2. 点击 "Login" 或 "Get Started"
3. 选择 "Continue with GitHub"
4. 授权Railway访问你的GitHub账号

### 步骤2：创建新项目
1. 点击 "New Project"
2. 选择 "Deploy from GitHub repo"
3. 在列表中找到并选择 `banaijianssss/doc_factory`
4. 点击 "Deploy Now"

### 步骤3：等待部署
- Railway会自动检测Python项目
- 自动安装依赖（requirements.txt）
- 自动启动服务（Procfile）
- 等待时间：2-5分钟

### 步骤4：获取公网地址
1. 部署完成后，点击项目进入Dashboard
2. 点击 "Settings"（设置图标）
3. 点击 "Domains"
4. 点击 "Generate Domain"
5. 获得类似 `https://doc-factory-xxx.up.railway.app` 的地址

### 步骤5：访问公网地址
在浏览器中打开分配的域名即可使用！

---

## 部署成功标志

- ✅ Railway Dashboard显示 "Deployed"
- ✅ 可以访问分配的域名
- ✅ 网页正常显示6种证书模板
- ✅ 可以正常生成证书

---

## 常见问题

### Q: 部署失败怎么办？
A: 查看Railway日志：
1. 点击项目进入Dashboard
2. 点击 "Deployments"
3. 查看错误日志

### Q: 如何更新部署？
A: 推送新代码到GitHub，Railway会自动重新部署

### Q: 免费额度多少？
A: 每月$5免费额度，足够小型应用运行

---

## 部署完成后

你可以：
1. 分享公网地址给客户
2. 嵌入到宣传文案中
3. 作为在线服务收费

祝部署顺利！🚀

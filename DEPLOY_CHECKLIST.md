# Render部署检查清单

## 部署前准备

- [ ] 已注册Render账号（使用GitHub登录）
- [ ] GitHub仓库是公开的
- [ ] 仓库包含 `requirements.txt`
- [ ] 仓库包含 `app_v2.py`
- [ ] 代码已推送到GitHub

---

## 部署步骤检查

### 步骤1：创建服务
- [ ] 点击 "New +" → "Web Service"
- [ ] 找到并选择 `banaijianssss/doc_factory`
- [ ] 点击 "Connect"

### 步骤2：基本配置
- [ ] Name: `doc-factory`
- [ ] Region: `Singapore`
- [ ] Branch: `main`

### 步骤3：运行时配置
- [ ] Runtime: `Python 3`
- [ ] Build Command: `pip install -r requirements.txt`
- [ ] Start Command: `python app_v2.py`

### 步骤4：选择套餐
- [ ] Instance Type: `Free`

### 步骤5：高级设置
- [ ] Auto-Deploy: `Yes`
- [ ] Health Check Path: `/`

### 步骤6：创建
- [ ] 点击 "Create Web Service"

---

## 部署中检查

- [ ] 看到部署日志输出
- [ ] 日志显示 "Installing dependencies"
- [ ] 日志显示 "Your service is live"
- [ ] 页面显示绿色 "Live" 状态

---

## 部署后验证

### 访问测试
- [ ] 可以打开分配的URL
- [ ] 看到智能文档工厂界面
- [ ] 显示6种证书模板

### 功能测试
- [ ] 手动输入可以生成证书
- [ ] Excel上传可以生成证书
- [ ] 可以下载zip文件
- [ ] 证书内容正确

---

## 部署成功后

- [ ] 复制公网地址
- [ ] 保存到安全的地方
- [ ] 测试分享给朋友访问
- [ ] 开始提供服务

---

## 如果失败

- [ ] 查看部署日志
- [ ] 检查错误信息
- [ ] 查看 `RAILWAY_TROUBLESHOOT.md`
- [ ] 尝试重新部署
- [ ] 联系支持

---

**完成所有检查后，你的服务就可以使用了！** ✅

# Render部署指南（备选方案）

如果Railway部署失败，Render是更好的备选方案。

## 为什么选Render？

- ✅ 免费额度更宽松
- ✅ 部署更简单
- ✅ 支持GitHub自动部署
- ✅ 国内访问速度较好

---

## 部署步骤

### 步骤1：注册Render
1. 访问 https://render.com
2. 点击 "Get Started for Free"
3. 使用GitHub账号登录

### 步骤2：创建Web Service
1. 登录后点击 "New +"
2. 选择 "Web Service"
3. 连接GitHub账号
4. 搜索并选择 `banaijianssss/doc_factory`

### 步骤3：配置部署
填写以下信息：

| 配置项 | 值 |
|--------|-----|
| Name | doc-factory |
| Region | Singapore (Asia Pacific) |
| Branch | main |
| Runtime | Python 3 |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `python app_v2.py` |

### 步骤4：高级设置（可选）
点击 "Advanced"：
- Auto-Deploy: Yes
- Health Check Path: `/`

### 步骤5：创建服务
点击 "Create Web Service"

等待部署完成（约3-5分钟）

### 步骤6：获取公网地址
部署完成后，Render会分配一个域名：
- 格式：`https://doc-factory.onrender.com`
- 在Dashboard中查看

---

## 部署成功标志

- ✅ Render Dashboard显示 "Live"
- ✅ 可以访问分配的域名
- ✅ 网页正常显示

---

## 与Railway对比

| 特性 | Railway | Render |
|------|---------|--------|
| 免费额度 | $5/月 | 750小时/月 |
| 休眠策略 | 无活动暂停 | 15分钟无活动暂停 |
| 部署难度 | 中等 | 简单 |
| 国内访问 | 一般 | 较好 |
| 自定义域名 | 支持 | 支持 |

---

## 推荐

如果Railway找不到仓库，**强烈建议使用Render**：
1. 部署成功率更高
2. 配置更简单
3. 免费额度够用

---

## 部署后

获得公网地址后：
1. 测试所有功能
2. 分享给客户
3. 开始提供服务

祝部署顺利！🚀

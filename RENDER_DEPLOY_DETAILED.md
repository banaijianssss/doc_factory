# Render部署详细图文指南

## 前言

本指南将手把手教你如何将智能文档工厂部署到Render平台，获得公网访问地址。

**预计时间：** 5-10分钟  
**难度：** ⭐⭐（简单）

---

## 第一步：注册Render账号

### 1.1 访问Render官网
打开浏览器，访问：https://render.com

### 1.2 点击注册
在首页点击 **"Get Started for Free"** 绿色按钮

### 1.3 选择GitHub登录
点击 **"Continue with GitHub"**  
（使用你的GitHub账号登录，无需额外注册）

### 1.4 授权Render
- 页面会跳转到GitHub授权页面
- 点击 **"Authorize render"**
- 等待跳回Render

**✅ 完成：** 你现在应该看到Render的Dashboard页面

---

## 第二步：创建Web Service

### 2.1 点击新建服务
在Dashboard页面，点击右上角的 **"New +"** 按钮

### 2.2 选择Web Service
在下拉菜单中选择 **"Web Service"**

### 2.3 连接GitHub仓库
你会看到GitHub仓库列表：

1. 在搜索框输入：`doc_factory`
2. 找到 `banaijianssss/doc_factory`
3. 点击 **"Connect"**

**如果没有显示仓库：**
- 点击页面下方的 **"Configure account"**
- 在弹出的GitHub页面中，找到Repository access
- 选择 "All repositories" 或手动选择 `doc_factory`
- 点击 "Save"
- 返回Render刷新页面

---

## 第三步：配置服务

### 3.1 基本信息
填写以下配置：

| 配置项 | 填写内容 | 说明 |
|--------|----------|------|
| **Name** | `doc-factory` | 服务名称，只能用小写字母和连字符 |
| **Region** | `Singapore` | 选择亚太地区，国内访问更快 |
| **Branch** | `main` | 默认就是main |

### 3.2 运行时配置

**Runtime（运行时）**
- 选择：`Python 3`

**Build Command（构建命令）**
```bash
pip install -r requirements.txt
```

**Start Command（启动命令）**
```bash
python app_v2.py
```

### 3.3 选择套餐

向下滚动到 "Instance Type"：

- 选择 **"Free"**（免费套餐）
- 规格：512 MB RAM，共享CPU
- 足够本项目使用

---

## 第四步：高级设置（可选）

点击 **"Advanced"** 展开高级选项：

### 4.1 自动部署
- **Auto-Deploy**: 选择 `Yes`
- 这样每次推送代码到GitHub，Render会自动重新部署

### 4.2 健康检查
- **Health Check Path**: 填写 `/`
- Render会访问这个路径检查服务是否正常

### 4.3 环境变量（可选）
如果需要，可以添加环境变量：
- 点击 "Add Environment Variable"
- Key: `FLASK_ENV`
- Value: `production`

---

## 第五步：创建服务

### 5.1 检查配置
确认所有配置正确：
- ✅ Name: doc-factory
- ✅ Region: Singapore
- ✅ Runtime: Python 3
- ✅ Build Command: pip install -r requirements.txt
- ✅ Start Command: python app_v2.py
- ✅ Instance Type: Free

### 5.2 点击创建
点击页面底部的 **"Create Web Service"** 蓝色按钮

---

## 第六步：等待部署

### 6.1 查看部署日志
创建后会自动跳转到部署页面：

你会看到实时日志输出：
```
==> Cloning repository...
==> Checking out commit...
==> Installing dependencies...
Collecting flask
Collecting pandas
...
==> Running build command...
pip install -r requirements.txt
...
==> Running start command...
python app_v2.py
```

### 6.2 部署时间
- 首次部署：3-5分钟
- 后续更新：1-2分钟

### 6.3 部署成功标志
当看到以下日志时，表示部署成功：
```
==> Deploying...
==> Your service is live
```

页面顶部会显示绿色 **"Live"** 状态

---

## 第七步：获取公网地址

### 7.1 查看域名
部署成功后，在页面顶部可以看到：

**URL:** `https://doc-factory-xxx.onrender.com`

（xxx是一串随机字符）

### 7.2 访问网站
点击URL链接，或复制到浏览器打开

你应该看到：
- 智能文档工厂的网页界面
- 6种证书模板选择
- 手动输入和Excel上传功能

---

## 第八步：测试功能

### 8.1 测试手动输入
1. 选择 "荣誉证书" 模板
2. 输入姓名：
   ```
   张三
   李四
   王五
   ```
3. 活动名称：测试活动
4. 颁发单位：测试单位
5. 点击 "生成证书"
6. 确认可以下载zip文件

### 8.2 测试Excel上传
1. 点击 "上传Excel" 标签
2. 上传 `sample_data.xlsx`
3. 点击 "上传并生成"
4. 确认可以下载证书

**✅ 如果以上测试都通过，说明部署成功！**

---

## 常见问题

### Q1: 部署失败，显示Build Error
**原因：** 依赖安装失败  
**解决：**
1. 检查 `requirements.txt` 是否正确
2. 查看详细错误日志
3. 确认Python版本兼容

### Q2: 服务显示"Deploy failed"
**原因：** 启动命令错误  
**解决：**
1. 检查Start Command是否为 `python app_v2.py`
2. 确认app_v2.py在根目录
3. 查看日志中的错误信息

### Q3: 网站可以访问，但生成证书失败
**原因：** 可能是文件系统权限  
**解决：**
1. 检查代码中的文件路径
2. 确保使用内存文件而非磁盘文件
3. 查看Render日志

### Q4: 服务自动休眠
**原因：** Render免费版15分钟无访问会休眠  
**解决：**
1. 首次访问可能需要等待30秒唤醒
2. 这是正常现象，不影响使用
3. 如需持续运行，需升级付费版

---

## 部署后的操作

### 更新代码
1. 推送新代码到GitHub
2. Render会自动重新部署
3. 等待1-2分钟即可

### 查看日志
在Render Dashboard：
1. 点击你的服务
2. 点击 "Logs" 标签
3. 查看实时日志

### 自定义域名（可选）
1. 在Dashboard点击 "Settings"
2. 找到 "Custom Domains"
3. 点击 "Add Custom Domain"
4. 按提示配置DNS

---

## 下一步

部署成功后，你可以：

1. **分享公网地址** 给客户使用
2. **嵌入到宣传文案** 中
3. **开始收费服务** 
4. **监控使用情况** 在Render Dashboard

---

## 需要帮助？

- Render文档：https://render.com/docs
- Render支持：https://render.com/help
- 项目GitHub：https://github.com/banaijianssss/doc_factory

---

**祝部署顺利！** 🚀

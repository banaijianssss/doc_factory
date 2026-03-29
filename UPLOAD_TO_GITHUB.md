# 手动上传到GitHub指南

由于网络限制，请使用以下方法上传代码到GitHub：

## 方法一：GitHub网页直接上传

### 步骤1：准备文件
我已经为你创建了需要上传的所有文件，位于：
`C:\Users\lovez\Desktop\doc-factory\`

### 步骤2：创建ZIP压缩包
1. 打开文件资源管理器
2. 进入 `doc-factory` 文件夹
3. 选中所有文件（Ctrl+A）
4. 右键 → 发送到 → 压缩(zipped)文件夹
5. 命名为 `doc-factory.zip`

### 步骤3：上传到GitHub
1. 访问 https://github.com/lovez/doc_factory
2. 点击 "Add file" → "Upload files"
3. 拖放或选择 `doc-factory.zip`
4. 点击 "Commit changes"

### 步骤4：解压（在GitHub上）
GitHub会自动处理ZIP文件

---

## 方法二：使用GitHub Desktop

### 步骤1：下载GitHub Desktop
访问 https://desktop.github.com 下载安装

### 步骤2：添加本地仓库
1. 打开GitHub Desktop
2. File → Add local repository
3. 选择 `C:\Users\lovez\Desktop\doc-factory`
4. 点击 "Add repository"

### 步骤3：推送到GitHub
1. 确认远程仓库 URL: `https://github.com/lovez/doc_factory`
2. 点击 "Publish branch"
3. 等待上传完成

---

## 方法三：分文件上传

如果ZIP上传失败，可以逐个上传核心文件：

### 必须上传的文件：
1. `app_v2.py` - 主程序
2. `requirements.txt` - 依赖列表
3. `Procfile` - 启动配置
4. `railway.json` - Railway配置
5. `nixpacks.toml` - 构建配置
6. `templates/index_v2.html` - 网页模板

### 上传步骤：
1. 访问 https://github.com/lovez/doc_factory
2. 点击 "Add file" → "Create new file"
3. 文件名输入：`app_v2.py`
4. 内容复制粘贴本地文件内容
5. 点击 "Commit new file"
6. 重复上述步骤上传其他文件

---

## 方法四：使用代理（推荐）

如果以上方法都失败，可以尝试设置代理：

### 设置Git代理
```bash
# 设置代理（替换为你的代理地址）
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890

# 推送
git push -u origin main

# 取消代理
git config --global --unset http.proxy
git config --global --unset https.proxy
```

---

## 上传成功后

1. 访问 https://github.com/lovez/doc_factory
2. 确认文件已上传
3. 访问 https://railway.app 部署
4. 获得公网地址

---

## 需要帮助？

如果以上方法都无法解决，你可以：
1. 使用U盘将 `doc-factory` 文件夹复制到其他电脑
2. 在其他网络环境下推送
3. 或者使用其他Git托管平台（Gitee、GitLab等）

---

## 快速检查清单

- [ ] 文件已上传到GitHub
- [ ] 可以在GitHub网页看到代码
- [ ] Railway已连接GitHub仓库
- [ ] 部署成功并获得公网地址

祝上传顺利！🚀

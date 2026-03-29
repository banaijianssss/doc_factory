# 智能文档工厂 v2.1

> 批量证书生成工具 - 一键生成，高效便捷

## 功能特性

- ✅ **6种内置模板**：荣誉证书、结业证书、参赛证明、志愿者证书、聘书、奖学金证书
- ✅ **自定义模板**：支持上传自己的Word模板
- ✅ **批量生成**：Excel导入或手动输入，一键生成所有证书
- ✅ **Web界面**：现代化UI，操作简单直观
- ✅ **数据安全**：本地处理，不上传云端

## 快速开始

### 方式一：直接运行（推荐）

```bash
# 安装依赖
pip install -r requirements.txt

# 启动服务
python app_v2.py

# 浏览器访问 http://localhost:5000
```

### 方式二：打包成可执行文件

```bash
# 安装PyInstaller
pip install pyinstaller

# 运行打包脚本
python build_exe.py

# 输出在"发布版本"文件夹中
```

## 使用说明

### 1. 选择模板
- 从6种内置模板中选择
- 或上传自定义Word模板

### 2. 输入数据
**手动输入：**
- 每行输入一个姓名
- 填写活动名称、颁发单位、日期

**Excel导入：**
- 准备Excel文件，包含列：姓名、活动、颁发单位、日期
- 上传文件即可

### 3. 生成证书
- 点击"生成证书"按钮
- 自动下载证书压缩包

## 自定义模板

在Word中设计证书，使用以下占位符：
- `{name}` - 姓名
- `{event}` - 活动名称
- `{organization}` - 颁发单位
- `{date}` - 日期

## 项目结构

```
doc-factory/
├── app_v2.py              # Web应用主程序（6种模板）
├── app.py                 # Web应用v1.0（4种模板）
├── generator.py           # 命令行版本
├── build_exe.py           # 打包脚本
├── requirements.txt       # Python依赖
├── templates/
│   ├── index_v2.html      # Web界面v2.0
│   └── index.html         # Web界面v1.0
├── uploads/               # 上传文件目录
├── output/                # 输出生成目录
├── custom_templates/      # 自定义模板目录
└── 发布版本/               # 打包后的可执行文件
```

## 技术栈

- **后端**: Python + Flask
- **文档处理**: python-docx
- **数据处理**: pandas + openpyxl
- **前端**: HTML5 + CSS3 + JavaScript

## 盈利模式

### 1. 接单服务
- **闲鱼/淘宝**: 发布"批量证书制作"服务
- **定价参考**:
  - 50人以内：¥30-50
  - 50-200人：¥50-100
  - 200人以上：¥100-200

### 2. 软件销售
- 打包成可执行文件
- 一次性销售或订阅制

## 许可证

MIT License

---

智能文档工厂 © 2026

# 智能文档工厂 - Docker部署配置
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    gcc \
    libxml2-dev \
    libxslt1-dev \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件
COPY requirements.txt .

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY app_v2.py .
COPY templates/ templates/

# 创建上传目录
RUN mkdir -p uploads output custom_templates

# 暴露端口
EXPOSE 5000

# 启动命令
CMD ["python", "app_v2.py"]

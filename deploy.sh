#!/bin/bash
# 智能文档工厂 - 部署脚本
# 支持：Docker部署、云服务器部署

echo "================================"
echo "智能文档工厂 - 部署工具"
echo "================================"
echo ""

# 检查Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker未安装，请先安装Docker"
    exit 1
fi

echo "[1/4] 正在构建Docker镜像..."
docker build -t doc-factory:latest .

echo ""
echo "[2/4] 停止旧容器..."
docker stop doc-factory 2>/dev/null || true
docker rm doc-factory 2>/dev/null || true

echo ""
echo "[3/4] 启动新容器..."
docker run -d \
    --name doc-factory \
    -p 5000:5000 \
    -v $(pwd)/uploads:/app/uploads \
    -v $(pwd)/output:/app/output \
    -v $(pwd)/custom_templates:/app/custom_templates \
    --restart unless-stopped \
    doc-factory:latest

echo ""
echo "[4/4] 检查服务状态..."
sleep 3
if docker ps | grep -q doc-factory; then
    echo "✅ 部署成功！"
    echo ""
    echo "访问地址:"
    echo "  - 本机: http://localhost:5000"
    echo "  - 局域网: http://$(hostname -I | awk '{print $1}'):5000"
else
    echo "❌ 部署失败，请检查日志:"
    echo "  docker logs doc-factory"
fi

echo ""
echo "================================"
echo "常用命令:"
echo "  查看日志: docker logs -f doc-factory"
echo "  停止服务: docker stop doc-factory"
echo "  重启服务: docker restart doc-factory"
echo "================================"

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
智能文档工厂 - 部署状态检查
"""

import os
import sys

def check_files():
    """检查必要文件是否存在"""
    print("="*50)
    print("智能文档工厂 - 部署前检查")
    print("="*50)
    print()
    
    required_files = [
        ('app_v2.py', '主程序'),
        ('requirements.txt', '依赖列表'),
        ('Procfile', '启动配置'),
        ('railway.json', 'Railway配置'),
        ('nixpacks.toml', '构建配置'),
        ('templates/index_v2.html', '网页模板'),
    ]
    
    all_ok = True
    for filename, desc in required_files:
        exists = os.path.exists(filename)
        status = "OK" if exists else "MISSING"
        symbol = "[OK]" if exists else "[MISSING]"
        print(f"{symbol} {desc}: {filename} - {status}")
        if not exists:
            all_ok = False
    
    print()
    
    # 检查Git状态
    print("Git状态:")
    if os.path.exists('.git'):
        print("[OK] Git仓库已初始化")
        
        # 检查远程仓库
        if os.path.exists('.git/config'):
            with open('.git/config', 'r') as f:
                config = f.read()
                if 'github.com' in config:
                    print("[OK] 远程仓库已配置")
                else:
                    print("[MISSING] 远程仓库未配置")
                    all_ok = False
    else:
        print("[MISSING] Git仓库未初始化")
        all_ok = False
    
    print()
    print("="*50)
    
    if all_ok:
        print("[OK] 所有检查通过，可以部署！")
        print()
        print("部署步骤:")
        print("1. 推送代码到GitHub:")
        print("   git push -u origin main")
        print()
        print("2. 访问Railway部署:")
        print("   https://railway.app")
        print()
        print("3. 获得公网地址后分享给客户！")
    else:
        print("[MISSING] 部分检查未通过，请查看上述提示")
        print()
        print("帮助文档:")
        print("- GITHUB_PUSH_GUIDE.md - GitHub推送指南")
        print("- RAILWAY_DEPLOY.md - Railway部署指南")
    
    print("="*50)
    return all_ok

if __name__ == '__main__':
    success = check_files()
    sys.exit(0 if success else 1)

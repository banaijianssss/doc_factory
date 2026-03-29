#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
智能文档工厂 - 打包脚本
功能：将Web应用打包成独立可执行文件
"""

import PyInstaller.__main__
import os
import shutil

def build():
    """打包应用"""
    print("=" * 50)
    print("智能文档工厂 - 打包工具")
    print("=" * 50)
    
    # 清理旧文件
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    if os.path.exists('build'):
        shutil.rmtree('build')
    
    print("\n[1/3] 正在打包应用...")
    
    # PyInstaller参数
    args = [
        'app_v2.py',  # 主程序
        '--name=智能文档工厂',  # 应用名称
        '--onefile',  # 打包成单个文件
        '--windowed',  # 无控制台窗口
        '--icon=NONE',  # 图标
        '--add-data=templates;templates',  # 包含模板文件夹
        '--hidden-import=flask',
        '--hidden-import=pandas',
        '--hidden-import=docx',
        '--hidden-import=openpyxl',
    ]
    
    PyInstaller.__main__.run(args)
    
    print("\n[2/3] 复制额外文件...")
    
    # 创建输出目录
    output_dir = '发布版本'
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    
    # 复制可执行文件
    exe_name = '智能文档工厂.exe'
    if os.path.exists(f'dist/{exe_name}'):
        shutil.copy(f'dist/{exe_name}', output_dir)
        print(f"  ✓ 复制 {exe_name}")
    
    # 复制说明文档
    with open(f'{output_dir}/使用说明.txt', 'w', encoding='utf-8') as f:
        f.write("""智能文档工厂 v2.0 - 使用说明
================================

【系统要求】
- Windows 7/8/10/11
- 无需安装Python或其他依赖

【使用方法】
1. 双击运行"智能文档工厂.exe"
2. 等待程序启动（约5-10秒）
3. 浏览器会自动打开 http://localhost:5000
4. 如果浏览器未自动打开，请手动访问该地址

【功能说明】
1. 选择证书模板（4种内置模板可选）
2. 输入获奖人员姓名（每行一个）
3. 填写活动名称、颁发单位、日期
4. 点击"生成证书"按钮
5. 下载生成的证书压缩包

【Excel批量导入】
1. 准备Excel文件，包含以下列：
   - 姓名（或name）
   - 活动（或event）
   - 颁发单位（或organization）
   - 日期（或date，可选）
2. 点击"上传Excel"标签
3. 选择Excel文件
4. 点击"上传并生成"

【自定义模板】
1. 在Word中设计证书模板
2. 使用以下占位符：
   - {name} - 姓名
   - {event} - 活动名称
   - {organization} - 颁发单位
   - {date} - 日期
3. 保存为.docx格式
4. 在网页中上传自定义模板

【技术支持】
如有问题，请联系开发者

================================
智能文档工厂 © 2026
""")
    
    # 创建示例Excel
    import pandas as pd
    sample_data = {
        '姓名': ['张三', '李四', '王五'],
        '活动': ['2026年度优秀员工评选'],
        '颁发单位': ['XX科技有限公司'],
        '日期': ['2026年03月29日']
    }
    df = pd.DataFrame(sample_data)
    df.to_excel(f'{output_dir}/示例数据.xlsx', index=False)
    print("  ✓ 创建示例数据文件")
    
    print("\n[3/3] 清理临时文件...")
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    if os.path.exists('build'):
        shutil.rmtree('build')
    if os.path.exists('智能文档工厂.spec'):
        os.remove('智能文档工厂.spec')
    
    print("\n" + "=" * 50)
    print("打包完成！")
    print(f"输出目录: {os.path.abspath(output_dir)}")
    print("=" * 50)


if __name__ == '__main__':
    build()

import os
import sys
# 项目名称标记
FLAG = "ELF"

def config_for_import():
    """添加系统导入路径"""
    subs = ['src_py', 'build/elf', 'build/elfgames/go']
    current = os.path.abspath(__file__)
    root = os.path.join(current.split(FLAG)[0], FLAG)
    for item in subs:
        py_path = os.path.join(root, item)
        # print(py_path)
        sys.path.append(py_path)

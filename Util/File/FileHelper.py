#encoding:utf-8
import os
import re
from Util.File import Dir
import TestCases

# 获取目录下所有的文件
def dir_file_list(dir_path):
    return [os.path.join(parent_dir,file_name) for parent_dir, dir_names, file_names in os.walk(dir_path) for file_name in file_names]



# 获取目录下所有的python文件，且不包括__init__文件
def py_module_file_list(dir_path):
    # 以.py文件为后缀
    pattern_str = r"\.py$" 
    return [file_name for file_name in dir_file_list(dir_path) 
                if re.search(pattern_str, file_name) and "__init__" not in file_name]
    
    

# 将相对路径转换成模块导入的方式
def file_path_to_module(file_path):
    # -3是为了去掉“.py”这3个字符
    # 实例： a/b/c/d转化成a.b.c.d 或  a\b\c\d转化成a.b.c.d
    if "\\" + Dir.PROJECT_NAME  in file_path:
        file_path = file_path[file_path.find(Dir.PROJECT_NAME) + len(Dir.PROJECT_NAME) + 1:]
    return file_path.replace("\\", ".")[:-3].replace("/", ".")



# 获取指定目录下的所有模块的导入路径（不包括import关键字）
def module_import_lst(dir_path):
    return [file_path_to_module(module_path) for module_path in py_module_file_list(dir_path)]



# 获取指定模块（字符串格式）下所有的测试方法（过滤[Tt]est开头的用例）
def module_test_names(module_name):
    exec("import {0}".format(module_name))
    return ["{0}:{1}".format(module_name, func_name) for func_name in dir(eval(module_name)) 
                if re.search("^[Tt]est", func_name, re.I)]



# 根据路径获取及正则表达式来过滤用例
def tests_filter_from_dir(module_dir, pattern_str="", priority=""):
    func_names = []
    for module_name in module_import_lst(module_dir):
        func_names.extend(module_test_names(module_name))
    
    # 过滤正则表达式内容，只支持*符号
    if len(pattern_str):
        pattern_str = pattern_str.replace(".", "\.").replace("*", ".*")
        func_names = [func_name for func_name in func_names
                        if re.search(pattern_str, func_name, re.I)
                            or re.search(pattern_str, func_name.replace(":", "\."), re.I)]
    
    # 过滤用例等级，默认为空，不过滤
    if len(priority):
        for func_name in func_names[::-1]:
            if "priority" in eval(func_name.replace(":", ".")+".__dict__"):
                if eval(func_name.replace(":", ".")+".__dict__")["priority"] not in priority.split(","):
                    func_names.remove(func_name)
    return func_names


    
if __name__ == "__main__":
    print tests_filter_from_dir("D:\\wy_auto\\TestCases\\")
    
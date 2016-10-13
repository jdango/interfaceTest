#encoding:utf-8
import sys
import os
import re

# 该项目的工程名
PROJECT_NAME = "wy_auto"



# 获取自动化工程的根路径
def project_root_dir():
    cur_path = os.path.abspath(sys.argv[0])
    # 在使用nosetests命令时，sys.argv[0]就不是wy_auto.py的路径了
    if "nosetests-script" in cur_path:
        # 如果使用了nosetests命令时，使用执行文件的当前路径来替换sys.argv[0]
        cur_path = os.getcwdu()
    if re.search(PROJECT_NAME + "$", cur_path):
        # 执行路径在根目录下
        return cur_path + "\\"
    else:
        # 在非根目录下执行
        #return cur_path[:cur_path.find(PROJECT_NAME)+len(PROJECT_NAME) + 1]
        return "D:\\wy_auto\\"


# 获取自动化用例的根目录
def testcases_root_dir(ab=True):
    if ab:
        return project_root_dir() + "TestCases\\"
    else:
        return "TestCases\\"



# 获取配置文件的根目录
def config_root_dir(ab=True):
    if ab:
        return project_root_dir() + "Config\\"
    else:
        return "Config\\"

 
# 获取日记打印配置的路径
def log_config_path():
    return project_root_dir() + "Config\\logging.conf"


 
# 获取Nose执行报告路径
def nose_result_path():
    return project_root_dir() + "_Output\\report\\"

     

if __name__ == "__main__":
    print testcases_root_dir()
    print config_root_dir()
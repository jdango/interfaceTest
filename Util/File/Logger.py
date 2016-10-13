#encoding:utf-8
'''
@note: 该文件用于对logging进行统一配置
@author: eason.sun
@organization: csb
@copyright: weiyao
'''
import logging.config
import re
from Util.File import Dir
import sys
reload(sys)
sys.setdefaultencoding("utf-8");



# 修改日记配置文件为绝对路径
def init():
    # 修改日志配置文件的路径
    f = open(Dir.log_config_path())
    tag = "'.*_Output/log/wy_autotest\.log'"
    t_str = "_Output/log/wy_autotest.log'"
    content = f.read()
    f.close()
    f = open(Dir.log_config_path(), "w+")
    content = re.sub(tag, "'" + Dir.project_root_dir().replace("\\", '/' ) + t_str, content)
    f.write(content)
    f.close()
    
    # 加载日志配置文件
    logging.config.fileConfig(Dir.log_config_path())
    


def debug(msg):
    if "decode" in dir(msg):
        msg = msg.decode("utf-8")
    logger = logging.getLogger("main")
    logger.debug(msg)

    

def info(msg):
    if "decode" in dir(msg):
        msg = msg.decode("utf-8")
    logger = logging.getLogger("main")
    logger.info(msg)
    


def warn(msg):
    if "decode" in dir(msg):
        msg = msg.decode("utf-8")
    logger = logging.getLogger("main")
    logger.warn(msg)



def error(msg):
    if "decode" in dir(msg):
        msg = msg.decode("utf-8")
    logger = logging.getLogger("main")
    logger.error(msg)
    raise Exception(msg)



def critical(msg):
    if "decode" in dir(msg):
        msg = msg.decode("utf-8")
    logger = logging.getLogger("main")
    logger.critical(msg)
    raise Exception(msg)



def nose(msg):
    if "decode" in dir(msg):
        msg = msg.decode("utf-8")
    print msg
    print "<br/>"
    logger = logging.getLogger("main")
    logger.info(msg)



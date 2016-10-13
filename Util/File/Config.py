#encoding:utf-8
from Util.File import Xml
from Util.File import Dir
import ConfigParser


# 加载默认配置项
def DefaultConfig():
    file_path = Dir.config_root_dir() + "Default.xml"
    return Xml.xml2dict(file_path)



# 加载Web配置项
def WebConfig():
    file_path = Dir.config_root_dir() + "WebConfig.xml"
    return Xml.xml2dict(file_path)



# 加载APP配置项
def AppConfig():
    file_path = Dir.config_root_dir() + "AppConfig.xml"
    return Xml.xml2dict(file_path)



# 加载API配置项
def ApiConfig():
    file_path = Dir.config_root_dir() + "ApiConfig.xml"
    return Xml.xml2dict(file_path)



# 加载HTTP配置项
def HttpConfig():
    file_path = Dir.config_root_dir() + "HttpConfig.xml"
    return Xml.xml2dict(file_path)

# 加载HTTP_mall配置项
def HttpConfig_mall():
    file_path = Dir.config_root_dir() + "HttpConfig_mall.xml"
    return Xml.xml2dict(file_path)

# 加载HTTP_cashmall配置项
def HttpConfig_cashmall():
    file_path = Dir.config_root_dir() + "HttpConfig_cashmall.xml"
    return Xml.xml2dict(file_path)

#加载HTTP_ronghe3配置项
def HttpConfig_ronghe3():
    file_path = Dir.config_root_dir() + "HttpConfig_ronghe3.xml"
    return Xml.xml2dict(file_path)



# 加载Thrift配置项
def ThriftConfig():
    file_path = Dir.config_root_dir() + "ThriftConfig.xml"
    return Xml.xml2dict(file_path)



# 加载Perf配置项
def PerfConfig():
    file_path = Dir.config_root_dir() + "PerfConfig.xml"
    return Xml.xml2dict(file_path)



# 加载时间配置项
def TimeConfig():
    file_path = Dir.config_root_dir() + "TimeConfig.xml"
    return Xml.xml2dict(file_path)


# 修改NOSE CFG的配置文件
def nose_set(key, value):
    nose_cfg_path = Dir.project_root_dir() + "nose.cfg"
    cf = ConfigParser.ConfigParser()
    cf.read(nose_cfg_path)
    cf.set("nosetests", key, value)
    cf.write(open(nose_cfg_path, "w"))


# 返回NOSE执行的命令
def nose_cmd():
    nose_cfg_path = Dir.project_root_dir() + "nose.cfg"
    cf = ConfigParser.ConfigParser()
    cf.read(nose_cfg_path)
    return cf.items("nosetests")


if __name__ == "__main__":
    print DefaultConfig()
    print ApiConfig().URL

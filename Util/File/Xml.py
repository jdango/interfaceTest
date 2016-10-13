#encoding:utf-8
from Model.File.XmlDict import Xml2Dict


# 将XML文件转换成字典数据类型
def xml2dict(file_path):
    xml = Xml2Dict()
    _dict = xml.parse(file_path)
    return _dict["config"]



if __name__ == "__main__":
    pass
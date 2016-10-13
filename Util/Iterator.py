#encoding:utf-8
from Util.File import Logger

# 比较两个字典是否相等
# 键以参数dict_src为主
def cmp_dict(dict_src, dict_dst):
    if len(dict_src) == 0 or len(dict_dst) == 0 and (not len(dict_src) == len(dict_dst)):
        #logger.iLogger在比对字典内容为空")
        return False
    for key in dict_src:
        logger.info("Logger = %s" % key)
        logger.info("SLogger = %s" % (key, dict_src[key]))
        logger.info("DLogger = %s" % (key, dict_dst[key]))
        if key == 'version':
            continue
        if key == 'viewnums':
            continue
        if type(dict_src[key]) == list:
            for index,value in enumerate(dict_src[key]):
                if type(value) == dict:
                    cmp_dict(value, dict_dst[key][index])
                elif value == dict_dst[key][index]:
                    continue
                else:
                    print key
                    src = dict_src[key]
                    dst = dict_dst[key]
                    print src, type(src)
                    print dst, type(dst)
                    return False
                
        if type(dict_src[key]) == dict:
            if not cmp_dict(dict_src[key], dict_dst[key]):
                return False
            continue
        if dict_src[key] != dict_dst[key]:
            src = dict_src[key]
            dst = dict_dst[key]
            if src == dst:
                continue
            print key
            print src, type(src)
            print dst, type(dst)
            return False
    return True
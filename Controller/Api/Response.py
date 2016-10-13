#encoding:utf-8
"""
@note:该文件主要用于对用例返回数据的比较实现
@autor: eason.sun
@organization: csb
@copyright: weiyao
"""
from Util.File import Config
from Util.File import Logger


def api_response_result_null(resp_dict):
    """
    @author: eason.sun
    @resp_dict: 待比对的字典集和
    @return: 对API返回的数据进行空值校验 True/False
    @summary: 比较字典内容是否为空，以下为接口返回数据：version/action/errCode/allRows/data
    """
    if not resp_dict.has_key(Config.ApiConfig().ResponseStruct.VersionKey) :
        return False
    Logger.info("API接口数据中有版本信息")
    if not resp_dict.has_key(Config.ApiConfig().ResponseStruct.ActionKey):
        return False
    Logger.info("API接口数据中有Action信息")
    if not resp_dict.has_key(Config.ApiConfig().ResponseStruct.ErrorCodeKey):
        return False
    Logger.info("API接口数据中有错误码信息")
    if not resp_dict.has_key(Config.ApiConfig().ResponseStruct.AllRowsKey):
        return False
    Logger.info("API接口数据中有行数信息")
    if not resp_dict.has_key(Config.ApiConfig().ResponseStruct.DataKey):
        return False
    Logger.info("API接口数据中有数据信息")
    return True



def api_response_result_data(resp_dict):
    """
    @author: june.chen
    @resp_dict: 待比对的字典集和
    @return: data空值校验 True/False
    @summary: 返回的data是否为空
    """
    Logger.info("检查返回的data是否为空")
    if resp_dict.has_key(Config.ApiConfig().ResponseStruct.ErrorCodeKey):
        if resp_dict[Config.ApiConfig().ResponseStruct.ErrorCodeKey] != 0:
            Logger.info("API接口数据返回的错误码errorCode不等于0")
            return False
    else:
        Logger.info("API接口数据中不存在错误码")
        return False
    
    if resp_dict.has_key(Config.ApiConfig().ResponseStruct.DataKey) :
        data = Config.ApiConfig().ResponseStruct.DataKey
        if resp_dict[data] == [] or resp_dict[data] == '' or resp_dict[data] == {} or resp_dict[data] == None:
            Logger.info("API接口数据中data为空")
            return False
        else:
            Logger.info("API接口数据中data不为空")
            return True
    else :
        Logger.info("API接口数据没有查询数据返回")
        return False



def api_result_basic_info_cmp(src_dict, dst_dict):
    """
    @author: june.chen
    @resp_dict: 源字典集合
    @dst_dict: 目的字典集合
    @return: True/False
    @summary: 数据基础数据比较：version/action/errorCode/allRows
    """
    Logger.info("检查基础内容")
    if src_dict[Config.ApiConfig().ResponseStruct.VersionKey] != dst_dict[Config.ApiConfig().ResponseStruct.VersionKey]:
        Logger.info("版本号比对失败")
        Logger.info(src_dict[Config.ApiConfig().ResponseStruct.VersionKey])
        Logger.info(dst_dict[Config.ApiConfig().ResponseStruct.VersionKey])
        return False
    if src_dict[Config.ApiConfig().ResponseStruct.ActionKey] != dst_dict[Config.ApiConfig().ResponseStruct.ActionKey]:
        Logger.info("action方法比对失败")
        Logger.info(src_dict[Config.ApiConfig().ResponseStruct.ActionKey])
        Logger.info(dst_dict[Config.ApiConfig().ResponseStruct.ActionKey])
        return False
    if src_dict[Config.ApiConfig().ResponseStruct.ErrorCodeKey] != dst_dict[Config.ApiConfig().ResponseStruct.ErrorCodeKey]:
        Logger.info("错误码比对失败")
        Logger.info(src_dict[Config.ApiConfig().ResponseStruct.ErrorCodeKey])
        Logger.info(dst_dict[Config.ApiConfig().ResponseStruct.ErrorCodeKey])
        return False
    if src_dict[Config.ApiConfig().ResponseStruct.AllRowsKey] != dst_dict[Config.ApiConfig().ResponseStruct.AllRowsKey]:
        Logger.info("行数比对失败")
        Logger.info(src_dict[Config.ApiConfig().ResponseStruct.AllRowsKey])
        Logger.info(dst_dict[Config.ApiConfig().ResponseStruct.AllRowsKey])
        return False
    return True


    
def dicts_default_check(dic, default_dic):
    '''
    @author: june.chen
    @resp_dict: 源字典集合
    @dst_dict: 目的字典集合
    @return: True/False
    @summary: 默认值校验
    '''
    tmd = dic.copy()
    del tmd['data']
    del tmd['allRows']
    Logger.info("检查默认结果")
    if tmd == default_dic:
        Logger.info("默认值结果正确")
    else:
        Logger.error("默认值结果不正确")

def http_code_check(resp_data, result):
    '''
    @author: eason.sun
    @resp_data: 待验证的返回值
    @return: True/False
    @summary: 校验返回数据正确
    '''
    assert resp_data in str(result)
    Logger.info("校验返回值成功")
    return True
  

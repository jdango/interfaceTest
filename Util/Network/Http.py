#encoding:utf-8
'''
@note:该文件用于对HTTP操作的统一方法
@author: eason.sun
@organization: csb
@copyright: weiyao
'''
import urllib2
import requests
import re
from Libs.poster.encode import multipart_encode
from Libs.poster.streaminghttp import register_openers
from Util.File  import Logger
from Util.File import Config


def post_request_result(param_dict, host):
    """
    @author: eason.sun
    @param_dict: POST请求的数据（字典类型）
    @host: POST请求的URL
    @return: 以字典的形式返回POST的响应数据
    @summary: 使用urllib2发送POST请求来获取响应数据
    """
    register_openers()
    datagen, headers = multipart_encode(param_dict)
    request = urllib2.Request(host, datagen, headers)
    try:
        response = urllib2.urlopen(request)
        return response
    except urllib2.HTTPError, e:
        Logger.info("POST请求出现错误！")
        Logger.info("POST请求返回码：{0}".format(e.code))
        Logger.info("POST请求结果：{0}".format(e.read()))
        return None
    


def api_request_result(params_dict, host = ""):
    """
    @author: eason.sun
    @param_dict: API请求的数据（字典类型）
    @host: API请求的URL
    @return: 返回处理后的POST请求结果
    @summary: 获取API响应结果后，将数据进行格式化
    """    
    if not len(host):
        host = Config.ApiConfig().URL
    # 获取POST请求返回的结果
    post_response = post_request_result(params_dict, host)
    # 将部分null值的返回值设置为空字符串
    post_response = post_response.read().replace("null", '""')
    # false替换为False，true替换为True
    post_response = post_response.replace("false", "False").replace("true", "True")
    # 以字典集返回结果
    dict_post = eval(post_response)
    # API定义所有返回结果都保存在data键中
    post_data = dict_post["data"]
    if type(post_data) == dict: # 返回data的类型为dict，则结果为单条记录
        result_escape(post_data)
    elif type(post_data) == list: # 返回data的类型为list，则结果为多条记录
        post_data = [result_escape(post_item) for post_item in post_data]
    return dict_post



def http_request_result(params_dict, host = ""):
    """
    @author: eason.sun
    @param_dict: http请求的数据（字典类型）
    @host: http请求的URL
    @return: 返回处理后的POST请求结果
    @summary: 获取HTTP响应结果后，将数据进行格式化
    """    
    if not len(host):
        host = Config.HttpConfig().URL
    # 获取POST请求返回的结果
    post_response = post_request_result(params_dict, host)
    # 将部分null值的返回值设置为空字符串
    post_response = post_response.read().replace("null", '""')
    # false替换为False，true替换为True
    post_response = post_response.replace("false", "False").replace("true", "True")
    # 以字典集返回结果
    dict_post = eval(post_response)
    # API定义所有返回结果都保存在data键中
    post_data = dict_post["data"]
    if type(post_data) == dict: # 返回data的类型为dict，则结果为单条记录
        result_escape(post_data)
    elif type(post_data) == list: # 返回data的类型为list，则结果为多条记录
        post_data = [result_escape(post_item) for post_item in post_data]
    return dict_post



def result_escape(result):
    """
    @author: eason.sun
    @result: POST/GET请求的响应数据
    @return: 以Unicode Escape的形式返回响应数据
    @summary: 由于POST和GET请求回来的数据与代码的编码格式不一致，对所有响应数据进行编码
    """
    if type(result) is list or type(result) is dict:
        for result_key in result:
            if type(result[result_key]) is dict:
                result[result_key] = result_escape(result[result_key])
            if type(result[result_key]) is str:
                result[result_key] = result[result_key].decode("unicode_escape")
    return result




def get_request_result(visit_url):
    try:
        response = urllib2.urlopen(visit_url).read()
        tup_res = re.compile('.*\((.*)\)').search(response).groups()
        dict_res = tup_res.json()
        return dict_res
    except urllib2.HTTPError, e:
        Logger.info("GET请求出现错误！")
        Logger.info("GET请求返回码：{0}".format(e.code))
        Logger.info("GET请求结果：{0}".format(e.read()))
        return None

def get_request_result2(url, data):
    """
    @author: eason.sun
    @result: POST/GET请求的响应数据
    @return: 以requests.get返回的数据
    @summary: 由于GET返回的数据requests无法解析为json只能输出为str
    """
    response = requests.get(url, data).content
    str_res = re.compile('.*\((.*)\)').search(response).group()
    '''
    re_str = '.*\((.*)\)'
    re_pat = re.compile(re_str)
    dict_ret = re_pat.search(response)
    if dict_res:
        dict_res.groups()
    return dict_res
    '''
    return str_res

def get_http_code(url, data):
    """
    @author: eason.sun
    @result: POST/GET请求的响应数据
    @return: 以requests.get返回的数据
    @summary: 由于GET返回的数据requests无法解析为json只能输出为str
    """
    response = requests.get(url, data)
    http_code = response.status_code
    return http_code




if __name__ == "__main__":
    params = {"model":"company",
              "action":"register",
              "version":"2.5",
              "companyId":"470907"}
    api_result = api_request_result(params)
    print api_result
    
    

#encoding:utf-8
'''
@note:实现通用APP接口自动化测试时用例关键字的具体实现
@author: eason.sun
@organization: csb
@copyright: weiyao
'''

from Util.Network import Http
from Util.File import Logger
from Util.File import Config
import requests
import re


def revoke_api_request(params):
    """
    @author: eason.sun
    @params: API请求参数（字典类型）
    @return: 以字典的形式返回API响应数据
    """
    Logger.info("发起API请求，发送参数为：%s" % params)
    # 获取接口数据
    dict_api = Http.api_request_result(params)
    Logger.info("API接口返回数据为： %s" % dict_api)
    return dict_api


def revoke_http_request(params):
    """
    @author: eason.sun
    @params: HTTP请求参数（字典类型）
    @return: 以字典的形式返回HTTP响应数据
    """
    Logger.info("发起HTTP请求，发送参数为：%s" % params)
    # 获取接口数据
    dict_http = Http.http_request_result(params)
    Logger.info("API接口返回数据为： %s" % dict_http)
    return dict_http


def revoke_get_request(url, data):
    """
    @author: eason.sun
    @url: 请求的url
    @data：请求的参数
    @return: 以str的形式返回HTTP响应数据
    """
    Logger.info("发起HTTP请求，发送链接为： %s" % url)
    Logger.info("发起HTTP请求，发送参数为： %s" % data)
    #获取接口数据
    response= requests.get(url, data = data).content
    str_res = re.compile('.*\((.*)\)').search(response).groups()
    Logger.info("HTTP接口返回数据为： %s" % str_res)
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

#encoding:utf-8
from nose.plugins.attrib import attr
from Util.File import Logger
from Util import Verify
from Controller.Api import Common
from Controller.Api import Response
from Util.File import Config
import requests


def setUp():
	Logger.info("开始-->融合平台base接口P0用例用例集")



def tearDown():
	Logger.info("结束-->融合平台base接口P0用例用例集")



@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获得频道信息：正常")
def test_get_Channel():
	Logger.info('-------------------开始执行用例：【获得频道信息：正常】--------------------')
	url = Config.HttpConfig().getChannel.url + '?' + Config.HttpConfig().getChannel.param1 + '&' + Config.HttpConfig().getChannel.param2
	data = {'callback':Config.HttpConfig().getChannel.param1,
        	'channelCode':Config.HttpConfig().getChannel.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().getChannel.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获得频道信息：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获得分享信息：正常")
def test_get_Shake():
	Logger.info('-------------------开始执行用例：【获得分享信息：正常】--------------------')
	url = Config.HttpConfig().getShare.url + '?' + Config.HttpConfig().getShare.param1 + '&' + Config.HttpConfig().getShare.param2 + '&' + Config.HttpConfig().getShare.param3
	data = {'callback':Config.HttpConfig().getShare.param1,
        	'channelCode':Config.HttpConfig().getShare.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().getShare.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获得分享信息：正常】--------------------')



@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获得首页背景的配置信息：正常")
def test_get_BKConfig():
	Logger.info('-------------------开始执行用例：【获得首页背景的配置信息：正常】--------------------')
	url = Config.HttpConfig().getBKConfig.url + '?' + Config.HttpConfig().getBKConfig.param1 + '&' + Config.HttpConfig().getBKConfig.param2
	data = {'callback':Config.HttpConfig().getBKConfig.param1,
        	'channelCode':Config.HttpConfig().getBKConfig.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().getBKConfig.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获得首页背景的配置信息：正常】--------------------')



@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获得节目单信息：正常")
def test_get_List():
	Logger.info('-------------------开始执行用例：【获得节目单信息：正常】--------------------')
	url = Config.HttpConfig().getListProgram.url + '?' + Config.HttpConfig().getListProgram.param1 + '&' + Config.HttpConfig().getListProgram.param2
	data = {'callback':Config.HttpConfig().getListProgram.param1,
        	'channelCode':Config.HttpConfig().getListProgram.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().getListProgram.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获得节目单信息：正常】--------------------')



@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获得橱窗信息：正常")
def test_get_showcase():
	Logger.info('-------------------开始执行用例：【获得橱窗信息：正常】--------------------')
	url = Config.HttpConfig().getListShowcase.url + '?' + Config.HttpConfig().getListShowcase.param1 + '&' + Config.HttpConfig().getListShowcase.param2
	data = {'callback':Config.HttpConfig().getListShowcase.param1,
        	'channelCode':Config.HttpConfig().getListShowcase.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().getListShowcase.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获得橱窗信息：正常】--------------------')



@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获得用户信息：正常")
def test_get_userinfo():
	Logger.info('-------------------开始执行用例：【获得用户信息：正常】--------------------')
	url = Config.HttpConfig().getUserInfo.url + '?' + Config.HttpConfig().getUserInfo.param1 + '&' + Config.HttpConfig().getUserInfo.param2
	data = {'callback':Config.HttpConfig().getUserInfo.param1,
        	'channelCode':Config.HttpConfig().getUserInfo.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().getUserInfo.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获得用户信息：正常】--------------------')



@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获得用户红包信息：正常")
def test_get_userredinfo():
	Logger.info('-------------------开始执行用例：【获得用户红包信息：正常】--------------------')
	url = Config.HttpConfig().getUserRedInfo.url + '?' + Config.HttpConfig().getUserRedInfo.param1 + '&' + Config.HttpConfig().getUserRedInfo.param2
	data = {'callback':Config.HttpConfig().getUserRedInfo.param1,
        	'channelCode':Config.HttpConfig().getUserRedInfo.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().getUserRedInfo.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获得用户红包信息：正常】--------------------')
	Logger.info('返回值暂时有问题')



@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获得用户卡券信息：正常")
def test_get_usercardlist():
	Logger.info('-------------------开始执行用例：【获得用户卡券信息：正常】--------------------')
	url = Config.HttpConfig().getUserCardList.url + '?' + Config.HttpConfig().getUserCardList.param1 + '&' + Config.HttpConfig().getUserRedInfo.param2
	data = {'callback':Config.HttpConfig().getUserCardList.param1,
        	'channelCode':Config.HttpConfig().getUserCardList.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().getUserCardList.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获得用户卡券信息：正常】--------------------')



@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获得广告信息：正常")
def test_get_ad():
	Logger.info('-------------------开始执行用例：【获得广告信息：正常】--------------------')
	url = Config.HttpConfig().getAdProgram.url + '?' + Config.HttpConfig().getAdProgram.param1 + '&' + Config.HttpConfig().getAdProgram.param2
	data = {'callback':Config.HttpConfig().getAdProgram.param1,
        	'channelCode':Config.HttpConfig().getAdProgram.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().getAdProgram.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获得广告信息：正常】--------------------')


'''
@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获得节目单详情信息：正常")
def test_get_infoprogram():
	Logger.info('-------------------开始执行用例：【获得节目单详情信息：正常】--------------------')
	url = Config.HttpConfig().getInfoProgram.url + '?' + Config.HttpConfig().getInfoProgram.param1 + '&' + Config.HttpConfig().getInfoProgram.param2
	data = {'callback':Config.HttpConfig().getInfoProgram.param1,
        	'channelCode':Config.HttpConfig().getInfoProgram.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().getInfoProgram.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获得节目单详情信息：正常】--------------------')
'''
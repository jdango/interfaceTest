#encoding:utf-8
from nose.plugins.attrib import attr
from Util.File import Logger
from Util import Verify
from Controller.Api import Common
from Controller.Api import Response
from Util.File import Config
import requests


def setUp():
	Logger.info("开始-->融合平台电视剧接口P0用例用例集")



def tearDown():
	Logger.info("结束-->融合平台电视剧接口P0用例用例集")



@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="电视剧初始化：正常")
def test_get_Tvinit():
	Logger.info('-------------------开始执行用例：【电视剧初始化：正常】--------------------')
	url = Config.HttpConfig().getTvInit.url + '?' + Config.HttpConfig().getTvInit.param1 + '&' + Config.HttpConfig().getTvInit.param2 + '&' + Config.HttpConfig().getTvInit.param3
	data = {'callback':Config.HttpConfig().getTvInit.param1,
        	'channelCode':Config.HttpConfig().getTvInit.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().getTvInit.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【电视剧初始化：正常】--------------------')



@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="电视剧答题：正常")
def test_get_Tvanswer():
	Logger.info('-------------------开始执行用例：【电视剧答题：正常】--------------------')
	url = Config.HttpConfig().getTvAnswer.url + '?' + Config.HttpConfig().getTvAnswer.param1 + '&' + Config.HttpConfig().getTvAnswer.param2 + '&' + Config.HttpConfig().getTvAnswer.param3 + '&' + Config.HttpConfig().getTvAnswer.param4 + '&' + Config.HttpConfig().getTvAnswer.param5
	data = {'callback':Config.HttpConfig().getTvAnswer.param1,
        	'channelCode':Config.HttpConfig().getTvAnswer.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().getTvAnswer.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【电视剧答题：正常】--------------------')



@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="电视剧切换答题：正常")
def test_get_NewTopic():
	Logger.info('-------------------开始执行用例：【电视剧切换答题：正常】--------------------')
	url = Config.HttpConfig().getNewTopic.url + '?' + Config.HttpConfig().getNewTopic.param1 + '&' + Config.HttpConfig().getNewTopic.param2 + '&' + Config.HttpConfig().getNewTopic.param3
	data = {'callback':Config.HttpConfig().getNewTopic.param1,
        	'channelCode':Config.HttpConfig().getNewTopic.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().getNewTopic.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【电视剧切换答题：正常】--------------------')



@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="电视剧心跳：正常")
def test_get_heartbeat():
	Logger.info('-------------------开始执行用例：【电视剧心跳：正常】--------------------')
	url = Config.HttpConfig().heartbeat.url + '?' + Config.HttpConfig().heartbeat.param1
	data = {'callback':Config.HttpConfig().heartbeat.param1}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().heartbeat.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【电视剧心跳：正常】--------------------')



@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="电视剧获取规则：正常")
def test_get_rule():
	Logger.info('-------------------开始执行用例：【电视剧获取规则：正常】--------------------')
	url = Config.HttpConfig().rule.url + '?' + Config.HttpConfig().rule.param1 + '&' + Config.HttpConfig().rule.param2
	data = {'callback':Config.HttpConfig().rule.param1,
        	'channelCode':Config.HttpConfig().rule.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().rule.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【电视剧获取规则：正常】--------------------')



@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="电视剧获取广告：正常")
def test_get_AdTv():
	Logger.info('-------------------开始执行用例：【电视剧获取广告：正常】--------------------')
	url = Config.HttpConfig().getAdTv.url + '?' + Config.HttpConfig().getAdTv.param1 + '&' + Config.HttpConfig().getAdTv.param2
	data = {'callback':Config.HttpConfig().getAdTv.param1,
        	'channelCode':Config.HttpConfig().getAdTv.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().getAdTv.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【电视剧获取广告：正常】--------------------')
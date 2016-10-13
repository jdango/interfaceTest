#encoding:utf-8
from nose.plugins.attrib import attr
from Util.File import Logger
from Util import Verify
from Controller.Api import Common
from Controller.Api import Response
from Util.File import Config
import requests


def setUp():
	Logger.info("开始-->融合平台新闻接口P0用例用例集")



def tearDown():
	Logger.info("结束-->融合平台新闻接口P0用例用例集")



@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获得主页面新闻列表：正常")
def test_get_Allnews():
	Logger.info('-------------------开始执行用例：【获得主页面新闻列表：正常】--------------------')
	url = Config.HttpConfig().getAllNews.url + '?' + Config.HttpConfig().getAllNews.param1 + '&' + Config.HttpConfig().getAllNews.param2 + '&' + Config.HttpConfig().getAllNews.param3
	data = {'callback':Config.HttpConfig().getAllNews.param1,
        	'channelCode':Config.HttpConfig().getAllNews.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().getAllNews.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获得主页面新闻列表：正常】--------------------')



@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="每隔十秒拉取最新审核新闻的长度：正常")
def test_get_AudiNewsSize():
	Logger.info('-------------------开始执行用例：【每隔十秒拉取最新审核新闻的长度：正常】--------------------')
	url = Config.HttpConfig().getAuditNewsSize.url + '?' + Config.HttpConfig().getAuditNewsSize.param1 + '&' + Config.HttpConfig().getAuditNewsSize.param2
	data = {'callback':Config.HttpConfig().getAuditNewsSize.param1,
        	'channelCode':Config.HttpConfig().getAuditNewsSize.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().getAuditNewsSize.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【每隔十秒拉取最新审核新闻的长度：正常】--------------------')



@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="点赞：正常")
def test_get_zanAdd():
	Logger.info('-------------------开始执行用例：【点赞：正常】--------------------')
	url = Config.HttpConfig().zanAdd.url + '?' + Config.HttpConfig().zanAdd.param1 + '&' + Config.HttpConfig().zanAdd.param2 + '&' + Config.HttpConfig().zanAdd.param3
	data = {'callback':Config.HttpConfig().zanAdd.param1,
        	'channelCode':Config.HttpConfig().zanAdd.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	#Response.http_code_check(Config.HttpConfig().zanAdd.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【点赞：正常】--------------------')



@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="单个新闻：正常")
def test_get_SingleNews():
	Logger.info('-------------------开始执行用例：【单个新闻：正常】--------------------')
	url = Config.HttpConfig().getSingleNews.url + '?' + Config.HttpConfig().getSingleNews.param1 + '&' + Config.HttpConfig().getSingleNews.param2 + '&' + Config.HttpConfig().getSingleNews.param3 + '&' + Config.HttpConfig().getSingleNews.param4
	data = {'callback':Config.HttpConfig().getSingleNews.param1,
        	'channelCode':Config.HttpConfig().getSingleNews.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().getSingleNews.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【单个新闻：正常】--------------------')


'''
@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="单个新闻下的评论：正常")
def test_get_Comments():
	Logger.info('-------------------开始执行用例：【单个新闻下的评论：正常】--------------------')
	url = Config.HttpConfig().getComments.url + '?' + Config.HttpConfig().getComments.param1 + '&' + Config.HttpConfig().getComments.param2 + '&' + Config.HttpConfig().getComments.param3 + '&' + Config.HttpConfig().getComments.param4
	data = {'callback':Config.HttpConfig().getComments.param1,
        	'channelCode':Config.HttpConfig().getComments.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().getComments.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【单个新闻下的评论：正常】--------------------')
'''



@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="发表评论：正常")
def test_get_commentA():
	Logger.info('-------------------开始执行用例：【发表评论：正常】--------------------')
	url = Config.HttpConfig().comment.url + '?' + Config.HttpConfig().comment.param1 + '&' + Config.HttpConfig().comment.param2 + '&' + Config.HttpConfig().comment.param3 + '&' + Config.HttpConfig().comment.param4 + '&' + Config.HttpConfig().comment.param5 + '&' + Config.HttpConfig().comment.param6
	data = {'callback':"",
        	'channelCode':""}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().comment.resp, common_itemconfig_result)
	#Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【发表评论：正常】--------------------')



@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="投票：正常")
def test_get_voteA():
	Logger.info('-------------------开始执行用例：【投票：正常】--------------------')
	url = Config.HttpConfig().voteA.url + '?' + Config.HttpConfig().voteA.param1 + '&' + Config.HttpConfig().voteA.param2 + '&' + Config.HttpConfig().voteA.param3 + '&' + Config.HttpConfig().voteA.param4 + '&' + Config.HttpConfig().voteA.param5
	data = {'callback':"",
        	'channelCode':""}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().voteA.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【投票：正常】--------------------')
#encoding:utf-8
from nose.plugins.attrib import attr
from Util.File import Logger
from Util import Verify
from Controller.Api import Common
from Controller.Api import Response
from Util.File import Config
import requests


def setUp():
	Logger.info("开始-->融合平台新版新闻接口P0用例用例集")



def tearDown():
	Logger.info("结束-->融合平台新版新闻接口P0用例用例集")



@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="新版新闻投票：正常")
def test_get_new_vote():
	Logger.info('-------------------开始执行用例：【新版新闻投票：正常】--------------------')
	url = Config.HttpConfig().vote.url + '?' + Config.HttpConfig().vote.param1 + '&' + Config.HttpConfig().vote.param2 + '&' + Config.HttpConfig().vote.param3 + '&' +Config.HttpConfig().vote.param4
	data = {'callback':Config.HttpConfig().vote.param1,
        	'channelCode':Config.HttpConfig().vote.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().vote.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【新版新闻投票：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="新版新闻获取投票：正常")
def test_get_TopicDetail():
	Logger.info('-------------------开始执行用例：【新版新闻获取投票：正常】--------------------')
	url = Config.HttpConfig().getTopicDetail.url + '?' + Config.HttpConfig().getTopicDetail.param1 + '&' + Config.HttpConfig().getTopicDetail.param2 + '&' + Config.HttpConfig().getTopicDetail.param3
	data = {'callback':Config.HttpConfig().getTopicDetail.param1,
        	'channelCode':Config.HttpConfig().getTopicDetail.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().getTopicDetail.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【新版新闻获取投票：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="新版新闻评论：正常")
def test_get_saveComment():
	Logger.info('-------------------开始执行用例：【新版新闻评论：正常】--------------------')
	url = Config.HttpConfig().saveComment.url + '?' + Config.HttpConfig().saveComment.param1 + '&' + Config.HttpConfig().saveComment.param2 + '&' + Config.HttpConfig().saveComment.param3 + '&' + Config.HttpConfig().saveComment.param4 + '&' + Config.HttpConfig().saveComment.param5 + '&' + Config.HttpConfig().saveComment.param6
	data = {'callback':Config.HttpConfig().saveComment.param1,
        	'channelCode':Config.HttpConfig().saveComment.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().saveComment.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【新版新闻评论：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="新版新闻页面摇一摇：正常")
def test_get_Schedule():
	Logger.info('-------------------开始执行用例：【新版新闻页面摇一摇：正常】--------------------')
	url = Config.HttpConfig().getSchedule.url + '?' + Config.HttpConfig().getSchedule.param1 + '&' + Config.HttpConfig().getSchedule.param2 + '&' + Config.HttpConfig().getSchedule.param3
	data = {'callback':Config.HttpConfig().getSchedule.param1,
        	'channelCode':Config.HttpConfig().getSchedule.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().getSchedule.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【新版新闻页面摇一摇：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="新版新闻获取评论列表：正常")
def test_get_CommentList():
	Logger.info('-------------------开始执行用例：【新版新闻获取评论列表：正常】--------------------')
	url = Config.HttpConfig().getCommentList.url + '?' + Config.HttpConfig().getCommentList.param1 + '&' + Config.HttpConfig().getCommentList.param2 + '&' + Config.HttpConfig().getCommentList.param3 + '&' + Config.HttpConfig().getCommentList.param4 + '&' + Config.HttpConfig().getCommentList.param5
	data = {'callback':Config.HttpConfig().getCommentList.param1,
        	'channelCode':Config.HttpConfig().getCommentList.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().getCommentList.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【新版新闻获取评论列表：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="判断新版新闻版式（节目单调用）：正常")
def test_get_TopicA():
	Logger.info('-------------------开始执行用例：【判断新版新闻版式（节目单调用）：正常】--------------------')
	url = Config.HttpConfig().getTopicA.url + '?' + Config.HttpConfig().getTopicA.param1 + '&' + Config.HttpConfig().getTopicA.param2
	data = {'callback':Config.HttpConfig().getTopicA.param1,
        	'channelCode':Config.HttpConfig().getTopicA.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().getTopicA.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【判断新版新闻版式（节目单调用）：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="判断爆料设置 ：正常")
def test_get_TipoffSetting():
	Logger.info('-------------------开始执行用例：【判断爆料设置 ：正常】--------------------')
	url = Config.HttpConfig().getTipoffSetting.url + '?' + Config.HttpConfig().getTipoffSetting.param1 + '&' + Config.HttpConfig().getTipoffSetting.param2
	data = {'callback':Config.HttpConfig().getTipoffSetting.param1,
        	'channelCode':Config.HttpConfig().getTipoffSetting.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().getTipoffSetting.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【判断爆料设置 ：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="新版新闻页面分享 ：正常")
def test_get_ShareNew():
	Logger.info('-------------------开始执行用例：【新版新闻页面分享 ：正常】--------------------')
	url = Config.HttpConfig().getShareNew.url + '?' + Config.HttpConfig().getShareNew.param1 + '&' + Config.HttpConfig().getShareNew.param2 + '&' + Config.HttpConfig().getShareNew.param3
	data = {'callback':Config.HttpConfig().getShareNew.param1,
        	'channelCode':Config.HttpConfig().getShareNew.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().getShareNew.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【新版新闻页面分享 ：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="提交爆料：正常")
def test_get_saveTipoff():
	Logger.info('-------------------开始执行用例：【提交爆料：正常】--------------------')
	url = Config.HttpConfig().saveTipoff.url + '?' + Config.HttpConfig().saveTipoff.param1 + '&' + Config.HttpConfig().saveTipoff.param2 + '&' + Config.HttpConfig().saveTipoff.param3 + '&' + Config.HttpConfig().saveTipoff.param4 + '&' + Config.HttpConfig().saveTipoff.param5 + '&' + Config.HttpConfig().saveTipoff.param6 + '&' + Config.HttpConfig().saveTipoff.param7 + '&' + Config.HttpConfig().saveTipoff.param8 + '&' + Config.HttpConfig().saveTipoff.param9
	data = {'callback':Config.HttpConfig().saveTipoff.param1,
        	'channelCode':Config.HttpConfig().saveTipoff.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig().saveTipoff.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig().REQ_CODE)
	Logger.info('-------------------结束执行用例：【提交爆料：正常】--------------------')


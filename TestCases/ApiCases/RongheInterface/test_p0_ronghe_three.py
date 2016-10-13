#encoding:utf-8
from nose.plugins.attrib import attr
from Util.File import Logger
from Util import Verify
from Controller.Api import Common
from Controller.Api import Response
from Util.File import Config
import requests

def setUp():
    Logger.info("开始-->微摇融合平台3接口P0用例用例集")


def tearDown():
    Logger.info("结束-->微摇融合平台3接口P0用例用例集")


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取频道信息(话题版)：正常")
def test_get_ChannelInfo3_topic():
	Logger.info('-------------------开始执行用例：【获取频道信息：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getChannelInfo3.path + '?' + Config.HttpConfig_ronghe3().getChannelInfo3.param1 + '&' + Config.HttpConfig_ronghe3().getChannelInfo3.param2
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getChannelInfo3.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取频道信息：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取摇奖时段信息(话题版)：正常")
def test_get_Timer_topic():
	Logger.info('-------------------开始执行用例：【获取摇奖时段信息：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getTimer.path + '?' + Config.HttpConfig_ronghe3().getTimer.param1 + '&' + Config.HttpConfig_ronghe3().getTimer.param2
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getTimer.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取摇奖时段信息：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取banner列表信息(话题版)：正常")
def test_get_BannerList_topic():
	Logger.info('-------------------开始执行用例：【获取banner列表信息：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getBannerList.path + '?' + Config.HttpConfig_ronghe3().getBannerList.param1 + '&' + Config.HttpConfig_ronghe3().getBannerList.param2 + '&' + Config.HttpConfig_ronghe3().getBannerList.param3 + '&' + Config.HttpConfig_ronghe3().getBannerList.param4
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getBannerList.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取banner列表信息：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取朋友圈分享配置(话题版)：正常")
def test_get_Share_topic():
	Logger.info('-------------------开始执行用例：【获取朋友圈分享配置：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getShare.path + '?' + Config.HttpConfig_ronghe3().getShare.param1 + '&' + Config.HttpConfig_ronghe3().getShare.param2
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getShare.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取朋友圈分享配置：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="显示设置（是否显示理财、电影、精彩推荐等）(话题版)：正常")
def test_get_ChannelConfigByType_topic():
	Logger.info('-------------------开始执行用例：【显示设置（是否显示理财、电影、精彩推荐等）：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getChannelConfigByType.path + '?' + Config.HttpConfig_ronghe3().getChannelConfigByType.param1 + '&' + Config.HttpConfig_ronghe3().getChannelConfigByType.param2 + '&' + Config.HttpConfig_ronghe3().getChannelConfigByType.param3
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getChannelConfigByType.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【显示设置（是否显示理财、电影、精彩推荐等）：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取节目单信息(话题版) ：正常")
def test_get_List3_topic():
	Logger.info('-------------------开始执行用例：【获取节目单信息 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URLHTTP + Config.HttpConfig_ronghe3().getList.path + '?' + Config.HttpConfig_ronghe3().getList.param1 + '&' + Config.HttpConfig_ronghe3().getList.param2
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getList.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取节目单信息 ：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取热门节目(话题版) ：正常")
def test_get_HotList_topic():
	Logger.info('-------------------开始执行用例：【获取热门节目 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getHotList.path + '?' + Config.HttpConfig_ronghe3().getHotList.param1 + '&' + Config.HttpConfig_ronghe3().getHotList.param2
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getHotList.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取热门节目 ：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取某热门节目下的话题(话题版) ：正常")
def test_get_ProgramTopicListByPage_topic():
	Logger.info('-------------------开始执行用例：【获取某热门节目下的话题 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getProgramTopicListByPage.path + '?' + Config.HttpConfig_ronghe3().getProgramTopicListByPage.param1 + '&' + Config.HttpConfig_ronghe3().getProgramTopicListByPage.param2 + '&' + Config.HttpConfig_ronghe3().getProgramTopicListByPage.param3
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getProgramTopicListByPage.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取某热门节目下的话题 ：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取我发表过的话题(话题版) ：正常")
def test_get_MyTopicList_topic():
	Logger.info('-------------------开始执行用例：【获取我发表过的话题 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getMyTopicList.path + '?' + Config.HttpConfig_ronghe3().getMyTopicList.param1 + '&' + Config.HttpConfig_ronghe3().getMyTopicList.param2 + '&' + Config.HttpConfig_ronghe3().getMyTopicList.param3
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getMyTopicList.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取我发表过的话题 ：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取用户信息(话题版) ：正常")
def test_get_UserInfo3_topic():
	Logger.info('-------------------开始执行用例：【获取用户信息 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getUserInfo.path + '?' + Config.HttpConfig_ronghe3().getUserInfo.param1 + '&' + Config.HttpConfig_ronghe3().getUserInfo.param2
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getUserInfo.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取用户信息 ：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取用户积分信息(话题版) ：正常")
def test_get_UserIntegral_topic():
	Logger.info('-------------------开始执行用例：【获取用户积分信息 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getUserIntegral.path + '?' + Config.HttpConfig_ronghe3().getUserIntegral.param1 + '&' + Config.HttpConfig_ronghe3().getUserIntegral.param2 + '&' + Config.HttpConfig_ronghe3().getUserIntegral.param3
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getUserIntegral.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取用户积分信息 ：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取用户金币信息(话题版) ：正常")
def test_get_UserWealth_topic():
	Logger.info('-------------------开始执行用例：【获取用户金币信息 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getUserWealth.path + '?' + Config.HttpConfig_ronghe3().getUserWealth.param1 + '&' + Config.HttpConfig_ronghe3().getUserWealth.param2
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getUserWealth.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取用户金币信息 ：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="发表话题(话题版) ：正常")
def test_save_ProgramTopic_topic():
	Logger.info('-------------------开始执行用例：【发表话题 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().saveProgramTopic.path + '?' + Config.HttpConfig_ronghe3().saveProgramTopic.param1 + '&' + Config.HttpConfig_ronghe3().saveProgramTopic.param2 + '&' + Config.HttpConfig_ronghe3().saveProgramTopic.param3 + '&' + Config.HttpConfig_ronghe3().saveProgramTopic.param4 + '&' + Config.HttpConfig_ronghe3().saveProgramTopic.param5 + '&' + Config.HttpConfig_ronghe3().saveProgramTopic.param6
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().saveProgramTopic.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【发表话题 ：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="发表评论(话题版) ：正常")
def test_save_Comment_topic():
	Logger.info('-------------------开始执行用例：【发表评论 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().saveComment.path + '?' + Config.HttpConfig_ronghe3().saveComment.param1 + '&' + Config.HttpConfig_ronghe3().saveComment.param2 + '&' + Config.HttpConfig_ronghe3().saveComment.param3 + '&' + Config.HttpConfig_ronghe3().saveComment.param4 + '&' + Config.HttpConfig_ronghe3().saveComment.param5 + '&' + Config.HttpConfig_ronghe3().saveComment.param6
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().saveComment.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【发表评论 ：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="拉取评论(话题版) ：正常")
def test_get_CommentList_topic():
	Logger.info('-------------------开始执行用例：【拉取评论 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getCommentList.path + '?' + Config.HttpConfig_ronghe3().getCommentList.param1 + '&' + Config.HttpConfig_ronghe3().getCommentList.param2 + '&' + Config.HttpConfig_ronghe3().getCommentList.param3
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getCommentList.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【拉取评论 ：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取猜广告游戏的配置(话题版) ：正常")
def test_get_ActTimer_topic():
	Logger.info('-------------------开始执行用例：【获取猜广告游戏的配置 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getActTimer.path + '?' + Config.HttpConfig_ronghe3().getActTimer.param1 + '&' + Config.HttpConfig_ronghe3().getActTimer.param2 + '&' + Config.HttpConfig_ronghe3().getActTimer.param3 + '&' + Config.HttpConfig_ronghe3().getActTimer.param4
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getActTimer.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取猜广告游戏的配置 ：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="提交猜广告结果(话题版) ：正常")
def test_save_UserResult_topic():
	Logger.info('-------------------开始执行用例：【提交猜广告结果 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().saveUserResult.path + '?' + Config.HttpConfig_ronghe3().saveUserResult.param1 + '&' + Config.HttpConfig_ronghe3().saveUserResult.param2 + '&' + Config.HttpConfig_ronghe3().saveUserResult.param3 + '&' + Config.HttpConfig_ronghe3().saveUserResult.param4
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().saveUserResult.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【提交猜广告结果 ：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取已参与猜广告的用户信息(话题版) ：正常")
def test_get_ActUsersAnswered_topic():
	Logger.info('-------------------开始执行用例：【获取已参与猜广告的用户信息 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getActUsersAnswered.path + '?' + Config.HttpConfig_ronghe3().getActUsersAnswered.param1 + '&' + Config.HttpConfig_ronghe3().getActUsersAnswered.param2 + '&' + Config.HttpConfig_ronghe3().getActUsersAnswered.param3
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getActUsersAnswered.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取已参与猜广告的用户信息 ：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取中奖信息(话题版) ：正常")
def test_get_UserResult_topic():
	Logger.info('-------------------开始执行用例：【获取中奖信息 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getUserResult.path + '?' + Config.HttpConfig_ronghe3().getUserResult.param1 + '&' + Config.HttpConfig_ronghe3().getUserResult.param2 + '&' + Config.HttpConfig_ronghe3().getUserResult.param3 + '&' + Config.HttpConfig_ronghe3().getUserResult.param4
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getUserResult.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取中奖信息 ：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取热门电视下的话题数量和评论数量(话题版) ：正常")
def test_get_ProgramStatisticsNum_topic():
	Logger.info('-------------------开始执行用例：【获取热门电视下的话题数量和评论数量 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getProgramStatisticsNum.path + '?' + Config.HttpConfig_ronghe3().getProgramStatisticsNum.param1 + '&' + Config.HttpConfig_ronghe3().getProgramStatisticsNum.param2
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getProgramStatisticsNum.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取热门电视下的话题数量和评论数量 ：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取热门电视下的滚屏话题(话题版) ：正常")
def test_get_ScreenList_topic():
	Logger.info('-------------------开始执行用例：【获取热门电视下的滚屏话题 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getScreenList.path + '?' + Config.HttpConfig_ronghe3().getScreenList.param1 + '&' + Config.HttpConfig_ronghe3().getScreenList.param2
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getScreenList.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取热门电视下的滚屏话题 ：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取频道信息(摇奖版) ：正常")
def test_get_ChannelConfig_shake():
	Logger.info('-------------------开始执行用例：【获取频道信息（进入按钮图片enterBtnImg、互动背景图actBgImg、摇宝图片yaoBaoImg） ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getChannelConfigShake.path + '?' + Config.HttpConfig_ronghe3().getChannelConfigShake.param1 + '&' + Config.HttpConfig_ronghe3().getChannelConfigShake.param2 + '&' + Config.HttpConfig_ronghe3().getChannelConfigShake.param3
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getChannelConfigShake.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取频道信息（进入按钮图片enterBtnImg、互动背景图actBgImg、摇宝图片yaoBaoImg） ：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取首页背景图片(摇奖版) ：正常")
def test_get_IndexBgImg_shake():
	Logger.info('-------------------开始执行用例：【获取首页背景图片 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getIndexBgImgShake.path + '?' + Config.HttpConfig_ronghe3().getIndexBgImgShake.param1 + '&' + Config.HttpConfig_ronghe3().getIndexBgImgShake.param2
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getIndexBgImgShake.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取首页背景图片 ：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取频道信息(摇奖版) ：正常")
def test_get_ChannelInfo_shake():
	Logger.info('-------------------开始执行用例：【获取频道信息 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getChannelInfoShake.path + '?' + Config.HttpConfig_ronghe3().getChannelInfoShake.param1 + '&' + Config.HttpConfig_ronghe3().getChannelInfoShake.param2
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getChannelInfoShake.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取频道信息 ：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="登陆(摇奖版) ：正常")
def test_login_ByAct_shake():
	Logger.info('-------------------开始执行用例：【登陆 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().loginByAct.path + '?' + Config.HttpConfig_ronghe3().loginByAct.param1 + '&' + Config.HttpConfig_ronghe3().loginByAct.param2
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().loginByAct.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【登陆 ：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取登录用户信息(摇奖版) ：正常")
def test_get_OlByAct_shake():
	Logger.info('-------------------开始执行用例：【获取登录用户信息 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getOlByAct.path + '?' + Config.HttpConfig_ronghe3().getOlByAct.param1 + '&' + Config.HttpConfig_ronghe3().getOlByAct.param2
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getOlByAct.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取登录用户信息 ：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取摇奖时段信息(摇奖版) ：正常")
def test_get_Timer_shake():
	Logger.info('-------------------开始执行用例：【获取摇奖时段信息 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getTimerShake.path + '?' + Config.HttpConfig_ronghe3().getTimerShake.param1 + '&' + Config.HttpConfig_ronghe3().getTimerShake.param2
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getTimerShake.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取摇奖时段信息 ：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取banner列表信息(摇奖版) ：正常")
def test_get_BannerList_shake():
	Logger.info('-------------------开始执行用例：【获取banner列表信息 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getBannerListShake.path + '?' + Config.HttpConfig_ronghe3().getBannerListShake.param1 + '&' + Config.HttpConfig_ronghe3().getBannerListShake.param2
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getBannerListShake.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取banner列表信息 ：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取朋友圈分享配置(摇奖版) ：正常")
def test_get_Share_shake():
	Logger.info('-------------------开始执行用例：【获取朋友圈分享配置 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getShareShake.path + '?' + Config.HttpConfig_ronghe3().getShareShake.param1 + '&' + Config.HttpConfig_ronghe3().getShareShake.param2
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getShareShake.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取朋友圈分享配置 ：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取二维码图片(摇奖版) ：正常")
def test_get_Qcode_shake():
	Logger.info('-------------------开始执行用例：【获取二维码图片 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getQcode.path + '?' + Config.HttpConfig_ronghe3().getQcode.param1 + '&' + Config.HttpConfig_ronghe3().getQcode.param2
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getQcode.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取二维码图片 ：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取中奖用户信息(摇奖版) ：正常")
def test_get_UserRewardsByAct_shake():
	Logger.info('-------------------开始执行用例：【获取中奖用户信息 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getUserRewardsByAct.path + '?' + Config.HttpConfig_ronghe3().getUserRewardsByAct.param1 + '&' + Config.HttpConfig_ronghe3().getUserRewardsByAct.param2 + '&' + Config.HttpConfig_ronghe3().getUserRewardsByAct.param3
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getUserRewardsByAct.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取中奖用户信息 ：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取中奖用户信息(摇奖版) ：正常")
def test_get_UserRewardsByAct_shake():
	Logger.info('-------------------开始执行用例：【获取中奖用户信息 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getUserRewardsByAct.path + '?' + Config.HttpConfig_ronghe3().getUserRewardsByAct.param1 + '&' + Config.HttpConfig_ronghe3().getUserRewardsByAct.param2 + '&' + Config.HttpConfig_ronghe3().getUserRewardsByAct.param3
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getUserRewardsByAct.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取中奖用户信息 ：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取摇动时的广告图片(摇奖版) ：正常")
def test_get_ActMaterial_shake():
	Logger.info('-------------------开始执行用例：【获取摇动时的广告图片 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getActMaterial.path + '?' + Config.HttpConfig_ronghe3().getActMaterial.param1 + '&' + Config.HttpConfig_ronghe3().getActMaterial.param2
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getActMaterial.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取摇动时的广告图片 ：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取主题背景图片(摇奖版) ：正常")
def test_get_ActImg_shake():
	Logger.info('-------------------开始执行用例：【获取主题背景图片 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getActImg.path + '?' + Config.HttpConfig_ronghe3().getActImg.param1 + '&' + Config.HttpConfig_ronghe3().getActImg.param2
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getActImg.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取主题背景图片 ：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取主题相关配置(摇奖版) ：正常")
def test_get_ChannelConfigByType_shake():
	Logger.info('-------------------开始执行用例：【获取主题相关配置（未中奖提示、未中奖图片等等） ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().getChannelConfigByTypeShake.path + '?' + Config.HttpConfig_ronghe3().getChannelConfigByTypeShake.param1 + '&' + Config.HttpConfig_ronghe3().getChannelConfigByTypeShake.param2 + '&' + Config.HttpConfig_ronghe3().getChannelConfigByTypeShake.param3
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().getChannelConfigByTypeShake.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取主题相关配置（未中奖提示、未中奖图片等等） ：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="摇动抽奖(摇奖版) ：正常")
def test_get_lottery_shake():
	Logger.info('-------------------开始执行用例：【摇动抽奖 ：正常】--------------------')
	url = Config.HttpConfig_ronghe3().URL + Config.HttpConfig_ronghe3().lotteryShake.path + '?' + Config.HttpConfig_ronghe3().lotteryShake.param1 + '&' + Config.HttpConfig_ronghe3().lotteryShake.param2 + '&' + Config.HttpConfig_ronghe3().lotteryShake.param3
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_ronghe3().lotteryShake.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_ronghe3().REQ_CODE)
	Logger.info('-------------------结束执行用例：【摇动抽奖 ：正常】--------------------')

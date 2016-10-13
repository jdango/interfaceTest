#encoding:utf-8
from nose.plugins.attrib import attr
from Util.File import Logger
from Util import Verify
from Controller.Api import Common
from Controller.Api import Response
from Util.File import Config
import requests

def setUp():
    Logger.info("开始-->微摇商城平台base接口P0用例用例集")


def tearDown():
    Logger.info("结束-->微摇商城平台base接口用例用例集")

'''
@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="查询用户总积分：正常")
def test_get_TotalIntegral():
	Logger.info('-------------------开始执行用例：【查询用户总积分：正常】--------------------')
	url = Config.HttpConfig_mall().URL + Config.HttpConfig_mall().getTotalIntegral.path + '?' + Config.HttpConfig_mall().getTotalIntegral.param1 + '&' + Config.HttpConfig_mall().getTotalIntegral.param2 + '&' + Config.HttpConfig_mall().getTotalIntegral.param3
	data = {'callback':Config.HttpConfig_mall().getTotalIntegral.param1,
        	'channelCode':Config.HttpConfig_mall().getTotalIntegral.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_mall().getTotalIntegral.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_mall().REQ_CODE)
	Logger.info('-------------------结束执行用例：【查询用户总积分：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="根据页面code查询页面所有类型元素列表：正常")
def test_get_PageConfigByPageCode():
	Logger.info('-------------------开始执行用例：【根据页面code查询页面所有类型元素列表：正常】--------------------')
	url = Config.HttpConfig_mall().URL + Config.HttpConfig_mall().getPageConfigByPageCode.path + '?' + Config.HttpConfig_mall().getPageConfigByPageCode.param1 + '&' + Config.HttpConfig_mall().getPageConfigByPageCode.param2
	data = {'callback':Config.HttpConfig_mall().getPageConfigByPageCode.param1,
        	'channelCode':Config.HttpConfig_mall().getPageConfigByPageCode.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_mall().getPageConfigByPageCode.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_mall().REQ_CODE)
	Logger.info('-------------------结束执行用例：【根据页面code查询页面所有类型元素列表：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="分页查询产品图片描述等信息：正常")
def test_get_ListForProductDetail():
	Logger.info('-------------------开始执行用例：【分页查询产品图片描述等信息：正常】--------------------')
	url = Config.HttpConfig_mall().URL + Config.HttpConfig_mall().getListForProductDetail.path + '?' + Config.HttpConfig_mall().getListForProductDetail.param1 + '&' + Config.HttpConfig_mall().getListForProductDetail.param2
	data = {'callback':Config.HttpConfig_mall().getListForProductDetail.param1,
        	'channelCode':Config.HttpConfig_mall().getListForProductDetail.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_mall().getListForProductDetail.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_mall().REQ_CODE)
	Logger.info('-------------------结束执行用例：【分页查询产品图片描述等信息：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="根据产品code查询规格属性：正常")
def test_get_SkuAttributteShow():
	Logger.info('-------------------开始执行用例：【根据产品code查询规格属性：正常】--------------------')
	url = Config.HttpConfig_mall().URL + Config.HttpConfig_mall().getSkuAttributeShow.path + '?' + Config.HttpConfig_mall().getSkuAttributeShow.param1 + '&' + Config.HttpConfig_mall().getSkuAttributeShow.param2 + '&' + Config.HttpConfig_mall().getSkuAttributeShow.param3
	data = {'callback':Config.HttpConfig_mall().getSkuAttributeShow.param1,
        	'channelCode':Config.HttpConfig_mall().getSkuAttributeShow.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_mall().getSkuAttributeShow.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_mall().REQ_CODE)
	Logger.info('-------------------结束执行用例：【根据产品code查询规格属性：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="根据SSKUID查询sku，product产品图片等相关信息：正常")
def test_get_ConfirmOrderInfo():
	Logger.info('-------------------开始执行用例：【根据SSKUID查询sku，product产品图片等相关信息：正常】--------------------')
	url = Config.HttpConfig_mall().URL + Config.HttpConfig_mall().getConfirmOrderInfo.path + '?' + Config.HttpConfig_mall().getConfirmOrderInfo.param1 + '&' + Config.HttpConfig_mall().getConfirmOrderInfo.param2
	data = {'callback':Config.HttpConfig_mall().getConfirmOrderInfo.param1,
        	'channelCode':Config.HttpConfig_mall().getConfirmOrderInfo.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_mall().getConfirmOrderInfo.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_mall().REQ_CODE)
	Logger.info('-------------------结束执行用例：【根据SSKUID查询sku，product产品图片等相关信息：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="积分及金币兑换：正常")
def test_do_Exchange():
	Logger.info('-------------------开始执行用例：【积分及金币兑换：正常】--------------------')
	url = Config.HttpConfig_mall().URL + Config.HttpConfig_mall().doExchange.path + '?' + Config.HttpConfig_mall().doExchange.param1 + '&' + Config.HttpConfig_mall().doExchange.param2 + '&' + Config.HttpConfig_mall().doExchange.param3 + '&' + Config.HttpConfig_mall().doExchange.param4 + '&' + Config.HttpConfig_mall().doExchange.param5 + '&' + Config.HttpConfig_mall().doExchange.param6
	data = {'callback':Config.HttpConfig_mall().doExchange.param1,
        	'channelCode':Config.HttpConfig_mall().doExchange.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_mall().doExchange.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_mall().REQ_CODE)
	Logger.info('-------------------结束执行用例：【积分及金币兑换：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="根据频道code查询频道信息：正常")
def test_get_ChannelInfoByCode():
	Logger.info('-------------------开始执行用例：【根据频道code查询频道信息：正常】--------------------')
	url = Config.HttpConfig_mall().URL + Config.HttpConfig_mall().getChannelInfoByCode.path + '?' + Config.HttpConfig_mall().getChannelInfoByCode.param1 + '&' + Config.HttpConfig_mall().getChannelInfoByCode.param2
	data = {'callback':Config.HttpConfig_mall().getChannelInfoByCode.param1,
        	'channelCode':Config.HttpConfig_mall().getChannelInfoByCode.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_mall().getChannelInfoByCode.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_mall().REQ_CODE)
	Logger.info('-------------------结束执行用例：【根据频道code查询频道信息：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="分页获取用户金币：正常")
def test_get_UserGoldlowByPage():
	Logger.info('-------------------开始执行用例：【分页获取用户金币：正常】--------------------')
	url = Config.HttpConfig_mall().URL + Config.HttpConfig_mall().getUserGoldFlowByPage.path + '?' + Config.HttpConfig_mall().getUserGoldFlowByPage.param1 + '&' + Config.HttpConfig_mall().getUserGoldFlowByPage.param2 + '&' + Config.HttpConfig_mall().getUserGoldFlowByPage.param3
	data = {'callback':Config.HttpConfig_mall().getUserGoldFlowByPage.param1,
        	'channelCode':Config.HttpConfig_mall().getUserGoldFlowByPage.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_mall().getUserGoldFlowByPage.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_mall().REQ_CODE)
	Logger.info('-------------------结束执行用例：【分页获取用户金币：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="分页查询兑换记录：正常")
def test_get_ExchangeList():
	Logger.info('-------------------开始执行用例：【分页查询兑换记录：正常】--------------------')
	url = Config.HttpConfig_mall().URL + Config.HttpConfig_mall().getExchangeList.path + '?' + Config.HttpConfig_mall().getExchangeList.param1 + '&' + Config.HttpConfig_mall().getExchangeList.param2 + '&' + Config.HttpConfig_mall().getExchangeList.param3
	data = {'callback':Config.HttpConfig_mall().getExchangeList.param1,
        	'channelCode':Config.HttpConfig_mall().getExchangeList.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_mall().getExchangeList.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_mall().REQ_CODE)
	Logger.info('-------------------结束执行用例：【分页查询兑换记录：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="根据页面code及元素类型查询某种元素的配置信息：正常")
def test_get_ElmentConfig():
	Logger.info('-------------------开始执行用例：【根据页面code及元素类型查询某种元素的配置信息：正常】--------------------')
	url = Config.HttpConfig_mall().URL + Config.HttpConfig_mall().getElementConfig.path + '?' + Config.HttpConfig_mall().getElementConfig.param1 + '&' + Config.HttpConfig_mall().getElementConfig.param2 + '&' + Config.HttpConfig_mall().getElementConfig.param3
	data = {'callback':Config.HttpConfig_mall().getElementConfig.param1,
        	'channelCode':Config.HttpConfig_mall().getElementConfig.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_mall().getElementConfig.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_mall().REQ_CODE)
	Logger.info('-------------------结束执行用例：【根据页面code及元素类型查询某种元素的配置信息：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="根据产品code查询产品池信息：正常")
def test_get_CmsProductByCode():
	Logger.info('-------------------开始执行用例：【根据产品code查询产品池信息：正常】--------------------')
	url = Config.HttpConfig_mall().URL + Config.HttpConfig_mall().getCmsProductByCode.path + '?' + Config.HttpConfig_mall().getCmsProductByCode.param1 + '&' + Config.HttpConfig_mall().getCmsProductByCode.param2
	data = {'callback':Config.HttpConfig_mall().getCmsProductByCode.param1,
        	'channelCode':Config.HttpConfig_mall().getCmsProductByCode.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_mall().getCmsProductByCode.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_mall().REQ_CODE)
	Logger.info('-------------------结束执行用例：【根据产品code查询产品池信息：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="根据产品code查询产品池信息：正常")
def test_get_Address():
	Logger.info('-------------------开始执行用例：【根据产品code查询产品池信息：正常】--------------------')
	url = Config.HttpConfig_mall().URL + Config.HttpConfig_mall().getAddress.path + '?' + Config.HttpConfig_mall().getAddress.param1 + '&' + Config.HttpConfig_mall().getAddress.param2
	data = {'callback':Config.HttpConfig_mall().getAddress.param1,
        	'channelCode':Config.HttpConfig_mall().getAddress.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_mall().getAddress.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_mall().REQ_CODE)
	Logger.info('-------------------结束执行用例：【根据产品code查询产品池信息：正常】--------------------')

@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="插入或更新地址信息：正常")
def test_insertOrupdate_Address():
	Logger.info('-------------------开始执行用例：【插入或更新地址信息：正常】--------------------')
	url = Config.HttpConfig_mall().URL + Config.HttpConfig_mall().insertOrUpdateAddress.path + '?' + Config.HttpConfig_mall().insertOrUpdateAddress.param1 + '&' + Config.HttpConfig_mall().insertOrUpdateAddress.param2 + '&' + Config.HttpConfig_mall().insertOrUpdateAddress.param3 + '&' + Config.HttpConfig_mall().insertOrUpdateAddress.param4 + '&' + Config.HttpConfig_mall().insertOrUpdateAddress.param5 + '&' + Config.HttpConfig_mall().insertOrUpdateAddress.param6
	data = {'callback':Config.HttpConfig_mall().insertOrUpdateAddress.param1,
        	'channelCode':Config.HttpConfig_mall().insertOrUpdateAddress.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_mall().insertOrUpdateAddress.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_mall().REQ_CODE)
	Logger.info('-------------------结束执行用例：【插入或更新地址信息：正常】--------------------')

'''
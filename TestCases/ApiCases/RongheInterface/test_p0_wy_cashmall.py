#encoding:utf-8
from nose.plugins.attrib import attr
from Util.File import Logger
from Util import Verify
from Controller.Api import Common
from Controller.Api import Response
from Util.File import Config
import requests

def setUp():
    Logger.info("开始-->微摇现金商城平台base接口P0用例用例集")


def tearDown():
    Logger.info("结束-->微摇现金商城平台base接口用例用例集")


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="根据code获取频道（现金商城）：正常")
def test_get_ChannelInfoByCode_cash():
	Logger.info('-------------------开始执行用例：【根据code获取频道：正常】--------------------')
	url = Config.HttpConfig_cashmall().URL + Config.HttpConfig_cashmall().getChannelInfoByCode.path + '?' + Config.HttpConfig_cashmall().getChannelInfoByCode.param1 + '&' + Config.HttpConfig_cashmall().getChannelInfoByCode.param2
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_cashmall().getChannelInfoByCode.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_cashmall().REQ_CODE)
	Logger.info('-------------------结束执行用例：【根据code获取频道：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取banner（现金商城）：正常")
def test_get_BannerPool():
	Logger.info('-------------------开始执行用例：【获取banner：正常】--------------------')
	url = Config.HttpConfig_cashmall().URL + Config.HttpConfig_cashmall().getBannerPool.path + '?' + Config.HttpConfig_cashmall().getBannerPool.param1 + '&' + Config.HttpConfig_cashmall().getBannerPool.param2 + '&' + Config.HttpConfig_cashmall().getBannerPool.param3
	data = {'callback':Config.HttpConfig_cashmall().getBannerPool.param1,
        	'channelCode':Config.HttpConfig_cashmall().getBannerPool.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_cashmall().getBannerPool.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_cashmall().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取banner：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取首页商品展示（现金商城）：正常")
def test_get_GoodsPool():
	Logger.info('-------------------开始执行用例：【获取首页商品展示：正常】--------------------')
	url = Config.HttpConfig_cashmall().URL + Config.HttpConfig_cashmall().getGoodsPool.path + '?' + Config.HttpConfig_cashmall().getGoodsPool.param1 + '&' + Config.HttpConfig_cashmall().getGoodsPool.param2
	data = {'callback':Config.HttpConfig_cashmall().getGoodsPool.param1,
        	'channelCode':Config.HttpConfig_cashmall().getGoodsPool.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_cashmall().getGoodsPool.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_cashmall().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取首页商品展示：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取全部商品（现金商城）：正常")
def test_get_ProductList():
	Logger.info('-------------------开始执行用例：【获取全部商品：正常】--------------------')
	url = Config.HttpConfig_cashmall().URL + Config.HttpConfig_cashmall().getProductList.path + '?' + Config.HttpConfig_cashmall().getProductList.param1 + '&' + Config.HttpConfig_cashmall().getProductList.param2 + '&' + Config.HttpConfig_cashmall().getProductList.param3 + '&' + Config.HttpConfig_cashmall().getProductList.param4 + '&' + Config.HttpConfig_cashmall().getProductList.param5 + '&' + Config.HttpConfig_cashmall().getProductList.param6 + '&' + Config.HttpConfig_cashmall().getProductList.param7
	data = {'callback':Config.HttpConfig_cashmall().getProductList.param1,
        	'channelCode':Config.HttpConfig_cashmall().getProductList.param2}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	#Response.http_code_check(Config.HttpConfig_cashmall().getProductList.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_cashmall().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取全部商品：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取商品详情（现金商城）：正常")
def test_get_ProductDetail():
	Logger.info('-------------------开始执行用例：【获取商品详情：正常】--------------------')
	url = Config.HttpConfig_cashmall().URL + Config.HttpConfig_cashmall().getProductDetail.path + '?' + Config.HttpConfig_cashmall().getProductDetail.param1 + '&' + Config.HttpConfig_cashmall().getProductDetail.param2 + '&' + Config.HttpConfig_cashmall().getProductDetail.param3 + '&' + Config.HttpConfig_cashmall().getProductDetail.param4
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_cashmall().getProductDetail.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_cashmall().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取商品详情：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取sku详情（现金商城）：正常")
def test_get_SkuDetail():
	Logger.info('-------------------开始执行用例：【获取sku详情：正常】--------------------')
	url = Config.HttpConfig_cashmall().URL + Config.HttpConfig_cashmall().getSkuDetail.path + '?' + Config.HttpConfig_cashmall().getSkuDetail.param1 + '&' + Config.HttpConfig_cashmall().getSkuDetail.param2 + '&' + Config.HttpConfig_cashmall().getSkuDetail.param3
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_cashmall().getSkuDetail.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_cashmall().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取sku详情：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取确认订单信息（现金商城）：正常")
def test_get_ConfirmOrderInfo_cash():
	Logger.info('-------------------开始执行用例：【获取确认订单信息：正常】--------------------')
	url = Config.HttpConfig_cashmall().URL + Config.HttpConfig_cashmall().getConfirmOrderInfo.path + '?' + Config.HttpConfig_cashmall().getConfirmOrderInfo.param1 + '&' + Config.HttpConfig_cashmall().getConfirmOrderInfo.param2
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_cashmall().getConfirmOrderInfo.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_cashmall().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取确认订单信息：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取地址（现金商城）：正常")
def test_get_Address_cash():
	Logger.info('-------------------开始执行用例：【获取地址：正常】--------------------')
	url = Config.HttpConfig_cashmall().URL + Config.HttpConfig_cashmall().getAddress.path + '?' + Config.HttpConfig_cashmall().getAddress.param1 + '&' + Config.HttpConfig_cashmall().getAddress.param2
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_cashmall().getAddress.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_cashmall().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取地址：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="更改地址（现金商城）：正常")
def test_insertOrUpdate_Address_cash():
	Logger.info('-------------------开始执行用例：【更改地址：正常】--------------------')
	url = Config.HttpConfig_cashmall().URL + Config.HttpConfig_cashmall().insertOrUpdateAddress.path + '?' + Config.HttpConfig_cashmall().insertOrUpdateAddress.param1 + '&' + Config.HttpConfig_cashmall().insertOrUpdateAddress.param2 + '&' + Config.HttpConfig_cashmall().insertOrUpdateAddress.param3 + '&' + Config.HttpConfig_cashmall().insertOrUpdateAddress.param4 + '&' + Config.HttpConfig_cashmall().insertOrUpdateAddress.param5 + '&' + Config.HttpConfig_cashmall().insertOrUpdateAddress.param6
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_cashmall().insertOrUpdateAddress.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_cashmall().REQ_CODE)
	Logger.info('-------------------结束执行用例：【更改地址：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取全部订单（现金商城）：正常")
def test_get_UserOrderList():
	Logger.info('-------------------开始执行用例：【获取全部订单：正常】--------------------')
	url = Config.HttpConfig_cashmall().URL + Config.HttpConfig_cashmall().getUserOrderList.path + '?' + Config.HttpConfig_cashmall().getUserOrderList.param1 + '&' + Config.HttpConfig_cashmall().getUserOrderList.param2 + '&' + Config.HttpConfig_cashmall().getUserOrderList.param3 + '&' + Config.HttpConfig_cashmall().getUserOrderList.param4
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_cashmall().getUserOrderList.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_cashmall().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取全部订单：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="获取订单详情（现金商城）：正常")
def test_get_OrderDetail():
	Logger.info('-------------------开始执行用例：【获取订单详情：正常】--------------------')
	url = Config.HttpConfig_cashmall().URL + Config.HttpConfig_cashmall().getOrderDetail.path + '?' + Config.HttpConfig_cashmall().getOrderDetail.param1 + '&' + Config.HttpConfig_cashmall().getOrderDetail.param2 + '&' + Config.HttpConfig_cashmall().getOrderDetail.param3
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_cashmall().getOrderDetail.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_cashmall().REQ_CODE)
	Logger.info('-------------------结束执行用例：【获取订单详情：正常】--------------------')


@attr(priority='0')
@attr(owner="eason.sun")
@attr(description="申请售后（现金商城）：正常")
def test_get_appealOrder():
	Logger.info('-------------------开始执行用例：【申请售后：正常】--------------------')
	url = Config.HttpConfig_cashmall().URL + Config.HttpConfig_cashmall().appealOrder.path + '?' + Config.HttpConfig_cashmall().appealOrder.param1 + '&' + Config.HttpConfig_cashmall().appealOrder.param2 + '&' + Config.HttpConfig_cashmall().appealOrder.param3 + '&' + Config.HttpConfig_cashmall().appealOrder.param4 + '&' + Config.HttpConfig_cashmall().appealOrder.param5 + '&' + Config.HttpConfig_cashmall().appealOrder.param6 + '&' + Config.HttpConfig_cashmall().appealOrder.param7
	data = {}
	common_itemconfig_result = Common.revoke_get_request(url, data)
	Response.http_code_check(Config.HttpConfig_cashmall().appealOrder.resp, common_itemconfig_result)
	Verify.IsTrue(Common.get_http_code(url, data) == requests.codes.ok, Config.HttpConfig_cashmall().REQ_CODE)
	Logger.info('-------------------结束执行用例：【申请售后：正常】--------------------')

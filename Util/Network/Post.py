#encoding:utf-8
import urllib2
import cookielib
import logging.config
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
from const.post_parameter import *
from util.sql.sql_helper import *
from Util.File import Logger
from Libs.beautifulsoup import BeautifulSoup
import time


# 让Poster携带Cookie以便模拟登陆
def poster_cookie():
    #opener = register_openers()
    #opener.add_handler(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    pass

def post_operate(post_params, url):
    datagen, headers = multipart_encode(post_params)
    request = urllib2.Request(url, datagen, headers)
    response = urllib2.urlopen(request)
    return response.read()

# 业主发标操作
def yz_zb(username, passwd):
    poster_cookie()
    yz_login_p['val'] = username
    yz_login_p['password'] = passwd
    sql = SqlHelper()
    result = sql.connection.get_yz_id(username)
    yz_id =  result[0]['uid']
    logger.info(u"查询结果为：%d" % yz_id)
    logger.info(u'【数据库查询业主id完成】')
    # 登陆操作
    post_operate(yz_login_p, ye_login_url)
    logger.info(u'【登录to8to完成】')
    i = 0
    while True:
        i += 1      
        # 发标操作
        print post_operate(ye_zb_p, ye_zb_url)
        #数据库查询项目id
        sql = SqlHelper()
        result = sql.connection.get_yid_by_phone_nick(phone, nickname)
        print result
        if result !=():
            break
        if i > 10:
            break
        time.sleep(10)
        logger.info(u'【发标失败】')
    logger.info(u'【发标完成】')
    logger.info(u"查询结果为：%s" % result[0])    
    yid =  result[0]['yid']
    logger.info(u"【项目id】：%d" % yid) 
    logger.info(u'【数据库查询项目完成】')
    return yid, yz_id
    
    
# CRM审标
def crm_shenbiao(yid):
    #poster_cookie()
    # CRM后台管理员登录
    post_operate(crm_superlogin_p, crm_login_url)
    logger.info(u'【crm审标登录完成】')
    #审标操作
    sb_url = 'http://weiyao/trdn/yuyue_apply_mdf.php?yid=' + str(yid) +'&qxtype=apply'
    print post_operate(sb_p, sb_url)
    logger.info(u'【审标完成】')


# CRM放标
def crm_fangbiao(yid):
    poster_cookie()
    # CRM后台管理员登录
    post_operate(crm_superlogin_p, crm_login_url)
    logger.info(u'【crm放标登录完成】')
    #放标操作
    fb_url = 'http://weiyao/trdn/yuyue_apply_zxb_ji_chuli.php?yid=' + str(yid) + '&cityid=1130'
    urllib2.urlopen(fb_url)
    logger.info(u'【放标完成】')
    

# CRM提交中标
def crm_zhongbiao(yid, yz_id):
    # CRM后台管理员登录
    post_operate(crm_superlogin_p, crm_login_url)
    logger.info(u'【crm中标登录完成】')
    #提交中标
    tjzb_url = 'http://weiyao/trdn/jj_month_zb_p_add.php?flag=pro_gl&ispass=1&record=&pro_yid=' + str(yid)
    response = urllib2.urlopen(tjzb_url)
    html = response.read()
    soup = BeautifulSoup.BeautifulSoup(html)
    cuid = soup.find('input', {'id':'cuid_0'}).get("value")
    tjzb_p['yid'] = yid
    tjzb_p['cuid'] = cuid
    tjzb_p['uid'] = cuid
    tjzb_p['yz_id'] = yz_id
    print post_operate(tjzb_p, tjzb_url)
    logger.info(u'【提交中标完成】')
    #处理中标
    jl_id_url = 'http://weiyao/trdn/jj_month_zb_p.php?f_arr=6&f_value=' + str(yid)
    response = urllib2.urlopen(jl_id_url)
    html = response.read()
    soup = BeautifulSoup.BeautifulSoup(html)
    table = soup.find('table',{'class':'table yewu'})
    td = table.contents[3].contents[1]
    jl_id = td.contents[0]
    clzb_url = 'http://weiyao/trdn/jj_smt_zb_chuli.php?id=' + jl_id + '&n=1'
    print post_operate(clzb_p, clzb_url)
    logger.info(u'【处理中标完成】')
    return cuid, jl_id


# CRM财务审核
def crm_caiwu_shenhe(yid, yz_id, cuid, jl_id):
    #业主提交汇款信息
    tjhk_p['yid'] = yid
    post_operate(tjhk_p, tjhk_url)
    logger.info(u'【提交汇款信息完成】')
    #修改财务密码
    post_operate(xg_cwpasd_p, xg_cwpasd_url)
    logger.info(u'【修改财务密码完成】')
    #财务登录
    post_operate(crm_cwlogin_p, crm_login_url)
    logger.info(u'【财务登录完成】')
    #查询财务记录id
    sql = SqlHelper()
    result = sql.connection.get_cwjl_id_by_fcom_id_adder_id(cuid, yz_id)
    cwjl_id =  result[0]['id']
    logger.info(u"查询结果为：%s" % result[0])
    logger.info(u'【数据库查询财务记录id完成】')
    cw_bj_url = 'http://weiyao/trdn/zxgs_caiwu_admin_add.php?id=' + str(cwjl_id) + '&ispass=5'
    urllib2.urlopen(cw_bj_url)
    #财务编辑
    cw_bj_p['fcom_id'] = cuid
    demo = '业主申请为中标记录ID是' + str(jl_id) + '的项目交纳装修保:2000元，所在城市深圳，<br>汇款方式:，<br>汇款时间：2015-01-08 20:41,<br>付款方户名：123'
    cw_bj_p['demo'] = demo
    cw_bj_p['zid[]'] =jl_id
    post_operate(cw_bj_p, cw_bj_url)
    logger.info(u'【财务编辑完成】')
    #财务审核
    cw_sh_p['id'] = cwjl_id
    post_operate(cw_sh_p, cw_sh_url)
    logger.info(u'【财务审核完成】')



# CRM根据ID修改装修公司密码
def crm_modify_cmp_pwd():
    pass


# CRM根据ID修改业主密码
def crm_modify_yz_pwd():
    pass
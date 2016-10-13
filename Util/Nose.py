#encoding:utf-8
import os
from Util.File import Logger
from Util.Time import Datetime
from Util.File import FileHelper
from Util.File import Dir
from Util.File import Result
from Util.Network import Mail
from Util.File import Config

def nose_run(parser):
    Config.nose_set("verbosity", parser.verbosity)
    Config.nose_set("logging-config", Dir.log_config_path())
    # 通过关键字筛选出来的用例列表
    tests = FileHelper.tests_filter_from_dir(Dir.testcases_root_dir(), 
                                             parser.select, 
                                             parser.priority)
    Config.nose_set("where", Dir.testcases_root_dir())
    if len(tests):
        for i in xrange(parser.loop):
            # 生成的报表每个名称都不一样，以时间为区分
            nosexml = Dir.nose_result_path() + "wy_autotest_" + Datetime.now_str() + ".xml"
            Config.nose_set("tests", ",".join(tests))
            Config.nose_set("xunit-file", nosexml)
            Logger.info("正在第{0}/{1}次进行Nose测试".format(i+1, parser.loop))
            Logger.info("执行Nose命令：{0}".format(Config.nose_cmd()))
            # 切换当前路径为工程根目录
            os.chdir(Dir.project_root_dir())
            os.system("nosetests")
            #发送邮件
            result_summary = Result.test_result_summary(nosexml)
            result_detail = Result.test_result_detail(nosexml)
            rev_addr_lst = ["eason.sun@wxshake.com","anny.song@wxshake.com","fenyunwang@wxshake.com"]
            Mail.send_email_with_attachment(result_summary + result_detail, 
                                            Config.DefaultConfig().Email.Subject, 
                                            nosexml, 
                                            rev_addr_lst)
            Logger.info("完成第{0}/{1}次进行Nose测试".format(i+1, parser.loop))
    else:
        Logger.info("抱歉，没有符合条件的执行测试用例！")
    
    
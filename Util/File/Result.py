#encoding:utf-8
from lxml import etree
import string
import string
from Util.File import Logger


# 获取用例执行结果概述
def test_result_summary(file_path):
    suites = etree.iterparse(file_path, tag="testsuite")
    for suite_item in suites:
        suite_name = suite_item[1].get("name")
        tests_num = int(suite_item[1].get("tests"))
        err_num = int(suite_item[1].get("errors"))
        fail_num = int(suite_item[1].get("failures"))
        skip_num = int(suite_item[1].get("skip"))
    summary = "\n"
    summary += "测试项目：{0}<br/>".format(suite_name)
    #summary += "测试项目：wy_auto_test<br/>".format(suite_name)
    summary += "测试用例数总数：{0}<br/>".format(tests_num)
    summary += "测试用例错误数：{0}<br/>".format(err_num)
    summary += "测试用例失败数：{0}<br/>".format(fail_num)
    summary += "测试用例成功数：{0}<br/>".format(tests_num - err_num - fail_num)
    return summary



# 根据用例执行结果，对各个用例的执行情况进行统计
def test_result_detail(file_path):
    doc = etree.iterparse(file_path, tag="testcase")
    result_detail = "<br/><br/>"
    fail_tests = ["<b style='color:#ff0000'>", "<br/>失败用例汇总"]
    for doc_item in doc:
    	if len(doc_item[1].getchildren()):
    		if doc_item[1].getchildren()[0].tag == 'error' or doc_item[1].getchildren()[0].tag == 'failure':
    			result_flag = False
    		else:
    			result_flag = True
    	else:
    		result_flag = True
        exe_result = "成功" if result_flag else "失败"
        casename = doc_item[1].get("name")
        
        if len(doc_item[1].getchildren()) > 0:
            if not result_flag:
                casename_fail = "【%s】" % casename
                fail_tests.append(casename_fail)
        result_detail += "<br/>测试用例名称：{0}<br/>".format(casename)
        result_detail += "测试结果：{0}<br/>".format(exe_result)
        result_detail += "-" * 80
    if len(fail_tests) > 2:
        fail_tests.append("</b>")
        result_detail = "<br/>".join(fail_tests) + result_detail
    
    return result_detail


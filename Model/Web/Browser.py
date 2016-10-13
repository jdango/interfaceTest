#encoding:utf-8
'''
@note:实现通用Web的操作方法
@author: eason.sun
@organization: csb
@copyright: weiyao

PerformanceTiming参考：
http://www.cnblogs.com/_franky/archive/2011/11/07/2238980.html
http://www.biaodianfu.com/html5-performance.html
http://www.th7.cn/web/html-css/201311/14802.shtml
http://www.51testing.com/html/24/n-861524.html
'''
from selenium import webdriver
from Util.File import Config
from Util.File import Logger
from selenium.webdriver.common.action_chains import ActionChains
import time
import os


class Browser():
	

	def __init__(self, btype="chrome"):
		self.btype = btype.lower()
		self.driver = self.create_browser(btype)
		self.init_time = 0			# 页面起始耗时时间
		self.redirect_time = 0 		# 重定向时间
		self.dns_time = 0			# dns查找时间
		self.tcp_time = 0			# tcp链接耗时
		self.request_time = 0		# 发送请求耗时
		self.response_time = 0		# 服务器响应时间
		self.processing_time = 0	# 处理时间
		self.onload_time = 0		# 浏览器处理时间
		self.appcache_time = 0		# App Cache耗时
		self.total_time = 0			# 页面加载总耗时
		self.timing_str = "window.performance.timing"


	# 页面跳转，并计算各个阶段的时间
	def navigate(self, n_url):
		Logger.info("浏览器正在跳转页面：%s" % n_url)
		self.driver.get(n_url)
		if not self.wait_until_complete():
			return False
		self.init_time = self.timing(Config.WebConfig().Timing.InitTime)
		self.redirect_time = self.timing(Config.WebConfig().Timing.RedirectTime)
		self.appcache_time = self.timing(Config.WebConfig().Timing.AppCacheTime)
		self.dns_time = self.timing(Config.WebConfig().Timing.DnsTime)
		self.tcp_time = self.timing(Config.WebConfig().Timing.TcpTime)
		self.request_time = self.timing(Config.WebConfig().Timing.RequestTime)
		self.response_time = self.timing(Config.WebConfig().Timing.ResponseTime)
		self.processing_time = self.timing(Config.WebConfig().Timing.ProcessingTime)
		self.onload_time = self.timing(Config.WebConfig().Timing.OnloadTime)
		self.total_time = self.timing(Config.WebConfig().Timing.TotalTime)
		self.timing_detail()
		return True



	# 鼠标悬浮
	def mouse_hover(self, xpath):
	    pass



	# 页面元素点击
	def click(self, xpath):
		if not self.wait_until_display(xpath):
			Logger.info("元素【{0}】不可见".format(xpath))
			return False
		element = self.driver.find_element_by_xpath(xpath)
		#ActionChains(self.driver)
		element.click()



	# 页面元素双击
	def double_click(self, xpath):
		if not self.wait_until_display(xpath):
			Logger.info("元素【{0}】不可见".format(xpath))
			return False
		element = self.driver.find_element_by_xpath(xpath)
		ActionChains(self.driver).double_click(element).perform()
		return True



	# 页面元素右键点击
	def right_click(self, xpath):
		if not self.wait_until_display(xpath):
			Logger.info("元素【{0}】不可见".format(xpath))
			return False
		element = self.driver.find_elements_by_xpath(xpath)
		ActionChains(self.driver).context_click(element).perform()
		return True



	# 输入内容
	def set_text(self, content, xpath):
		if not self.wait_until_display(xpath):
			Logger.info("元素【{0}】不可见".format(xpath))
			return False
		# 判断类型是否为输入框
		# TODO
		element = self.driver.find_elements_by_xpath(xpath)
		element.clear()
		element.send_keys(content)
		return True



	# 设置checkbox的状态
	def set_checkbox(self, state, xpath):
		if not self.wait_until_display(xpath):
			Logger.info("元素【{0}】不可见".format(xpath))
			return False
		# 判断该元素是否为checkbox
		# TODO
		element = self.driver.find_elements_by_xpath(xpath)
		# 判断当前状态是否和state一致
		# 如果一致就不点击，不一致才做点击



	# 等待页面元素可见
	def wait_until_display(self, xpath, timeout=10000):
		# 先等待页面完成加载
		if not self.wait_until_complete():
			return False
		# 查找元素
		if not self.wait_uitl_exists(xpath):
			Logger.info("元素【{0}】不存在".format(xpath))
			return False
		# 循环
		return self.driver.find_elements_by_xpath(xpath).is_displayed()



	# 等待页面元素存在
	def wait_uitl_exists(self, xpath):
		# 先等待页面完成加载
		if not self.wait_until_complete():
			return False
		# 查找元素
		# Todo



	# 等待页面加载完成
	def wait_until_complete(self, interval = 500, timeout = 10000):
	    complete_js = 'return document.readyState == "complete"'

	    start = 0
	    while start < timeout:
	    	# 等待DOM状态为Complete且页面总耗时大于0
	        state = self.driver.execute_script(complete_js) and self.timing(Config.WebConfig().Timing.TotalTime) > 0
	        if state:
	            time.sleep(interval/1000.0)
	            return True
	        start += interval
	        time.sleep(interval/1000.0)
	    return False



	# 检查元素的可见性
	def element_visible(self, xpath):
		if not self.wait_uitl_exists(xpath):
			Logger.info("元素【{0}】不存在".format(xpath))
			return False
		return self.driver.find_elements_by_xpath(xpath).is_displayed()



	# 下拉滚动条
	def scroll_down(self, step = 10000):
		scroll_js = "var q=document.documentElement.scrollTop={0}".format(step)
		self.driver.execute_script(scroll_js)
		return True



	# 上拉滚动条
	def scroll_up(self, step = 0):
	    	scroll_js = "var q=document.documentElement.scrollTop={0}".format(step)
		self.driver.execute_script(scroll_js)
		return True


	
	# 关闭浏览器
	def close(self):

		Logger.info("正在关闭浏览器")
		self.driver.quit()
		print u'关闭进程'
		# 杀死进程
		# if self.btype == "chrome":
		# 	Logger.info("杀死进程：chromedriver.exe")
		# 	os.system("taskkill /F /IM chromedriver.exe")
		# elif self.btype == "ie":
		# 	Logger.info("杀死进程：IEDriverServer.exe")
		# 	os.system("taskkill /F /IM IEDriverServer.exe")



	# 生成浏览器对象
	def create_browser(self, btype):
		# 根据不同浏览器的类型创建浏览器对象
		if btype.lower() == "ie":
			driver = webdriver.Ie()
		elif btype.lower() == "firefox":
			driver = webdriver.Firefox()
		else :
			options = webdriver.ChromeOptions()
			options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
			driver = webdriver.Chrome(chrome_options = options)
		return driver



	# 计算浏览器的加载时间
	def timing(self, interval_str):
		end, start = interval_str.split("-")
		end_js = "return %s.%s;" % (self.timing_str, end)
		start_js = "return %s.%s;" % (self.timing_str, start)
		
		if not self.driver:
			return False
		start_time = self.driver.execute_script(start_js)
		end_time = self.driver.execute_script(end_js)

		# 计算两个节点的时间差
		return end_time - start_time



	# 打印各个阶段的加载时间
	def timing_detail(self):
		t_d = "页面耗时统计如下：<br/>"
		t_d += "页面起始耗时：%s <br/>" % self.init_time
		t_d += "页面重定向耗时：%s <br/>" % self.redirect_time
		t_d += "App Cache耗时：%s <br/>" % self.appcache_time
		t_d += "页面DNS查找耗时：%s <br/>" % self.dns_time
		t_d += "页面TCP连接耗时：%s <br/>" % self.tcp_time
		t_d += "页面发送请求耗时：%s <br/>" % self.request_time
		t_d += "请求页面服务器响应时间：%s <br/>" % self.response_time
		t_d += "页面处理耗时：%s <br/>" % self.processing_time
		t_d += "页面onLoad处理耗时：%s <br/>" % self.onload_time
		t_d += "页面总耗时：%s <br/>" % self.total_time
		return t_d
		#Logger.info(t_d)



	# 各个阶段的加载时间的字典集合
	def timing_dict(self):
		t_d = {}
		t_d["init"] = self.init_time
		t_d["redirect"] = self.redirect_time
		t_d["appcache"] = self.appcache_time
		t_d["dns"] = self.dns_time
		t_d["tcp"] = self.tcp_time
		t_d["request"] = self.request_time
		t_d["response"] = self.response_time
		t_d["processing"] = self.processing_time
		t_d["onload"] = self.onload_time
		t_d["total"] = self.total_time
		return t_d




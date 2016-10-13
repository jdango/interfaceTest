#encoding:utf-8
import time
from Util.File import Logger



# 统计函数执行的时间
def exec_time(func, *args, **kwargs):
    Logger.info("函数 %s 开始执行" % func.__name__)
    start_time = time.time()
    func(*args, **kwargs) 
    
    end_time = time.time()
    Logger.info("函数 %s 执行完毕" % func.__name__)
    
    taken = end_time - start_time
    Logger.info("函数 %s 执行耗时：@%.3fs" % (func.__name__, taken))
    return taken

#coding=utf-8
'''
@note:该文件用于对时间的操作
@author: eason.sun
@organization: csb
@copyright: weiyao
'''

import time

def timestamp_to_time(timestamp):
    """
    @author: eason.sun
    @param timestamp:时间戳，即整数或小数
    @return:字符串格式返回时间    
    @summary:时间戳变换成年月日时分秒的日期格式
    """
    timestamp = int(timestamp)
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))



def time_to_timestamp(currtime):
    """
    @author: eason.sun
    @param timestamp:日期格式的字符串
    @return:时间戳    
    @summary:日期格式转换成时间戳
    """
    timeArray = time.strptime(currtime, "%Y-%m-%d %H:%M:%S")
    return int(time.mktime(timeArray))



def now_str():
    """
    对当前时间进行格式化返回
    """
    return time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))



def time_add_mins(currtime, mins):
    """
    @author: eason.sun
    @param timestamp:添加分钟数
    @return:时间戳    
    @summary:时间添加分钟
    """
    currTimeStamp = time_to_timestamp(currtime)
    addedTimeStamp = currTimeStamp + int(mins) * 60
    return timestamp_to_time(addedTimeStamp)



if __name__ == "__main__":
    print now_str()
    
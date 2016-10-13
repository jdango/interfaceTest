#encoding:utf-8
'''
@note:该文件主要用于对Python的断言进行统一操作
@author: eason.sun
@organization: csb
@copyright: weiyao
'''
from Util.File import Logger


def IsTrue(condition, msg):
	Logger.info(msg)
	assert condition, msg
    

	
def IsFalse(condition, msg):
	Logger.info(msg)
	assert not condition, msg
    


def IsNotNull(obj, msg):
	Logger.info(msg)
	assert obj is not None, msg
    


def IsNull(obj, msg):
	Logger.info(msg)
	assert obj is None, msg
    


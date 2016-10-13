#encoding:utf-8
from Util.File import Logger
import logging.config
from Util.File import Dir

logging.config.fileConfig(Dir.log_config_path())
logger = logging.getLogger("all_url_check")

handler = logging.FileHandler('D:/test.log', 'w')
fmt = '%(asctime)s[%(levelname)s] %(message)s'
formatter = logging.Formatter(fmt)   # 实例化formatter  
handler.setFormatter(formatter)
 
logger.addHandler(handler)

logger.info('qqj')
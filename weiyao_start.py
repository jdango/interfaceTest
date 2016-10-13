#encoding:utf-8
from Util import Nose
from Util.Args import Argparser
from Util.File import Logger


if __name__ == "__main__":
    # 日记配置初始化
    Logger.init()
    
    # 执行Nose
    parser = Argparser.setup_config_env()
    Nose.Nose_run(parser)

#encoding:utf-8
import argparse


def setup_default_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-verbosity', 
                                        help = u'是否打印冗余日志', 
                                        type = int,
                                        default = 2)
    
    parser.add_argument('-select', 
                                        help = u'选择要执行的用例名称', 
                                        default = "")
    
    parser.add_argument('-priority', 
                                        help = u'筛选执行测试用例的级别', 
                                        default = "0,1,2,3")
    
    parser.add_argument('-loop', 
                                        help = u'测试用例循环测试次数', 
                                        type = int,
                                        default = 1)
    return parser



def setup_config_env():
    parser = setup_default_args().parse_args()
    
    return parser



if __name__ == "__main__":
    setup_config_env()
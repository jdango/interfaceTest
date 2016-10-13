#encoding:utf-8
'''
@note:数学计算方法合集
@author: eason.sun
@organization: csb
@copyright: weiyao
'''
import math

# 地球半径
EARTH_RADIUS_METER = 6378137.0;

def deg2rad(d):
        return d*math.pi/180.0



def get_spherical_distance(from_p, to_p):
    """
    @author: eason.sun
    @param from_p:起点的经纬度，元组表示，如(纬度, 经度)
    @param to_p:终点的经纬度，元组表示，如(纬度, 经度)
    @return:返回两点的直线距离
    
    @summary:通过起点和终点的经纬度计算两点的直线距离
    """
    # 起点经度
    flon = deg2rad(from_p[1])
    # 起点纬度
    flat = deg2rad(from_p[0])
    # 终点经度
    tlon = deg2rad(to_p[1])
    # 终点纬度
    tlat = deg2rad(to_p[0])
    con = math.sin(flat)*math.sin(tlat)
    con += math.cos(flat)*math.cos(tlat)*math.cos(flon - tlon)
    return round(math.acos(con)*EARTH_RADIUS_METER/1000,4)



def get_dst_desc(from_p, to_p):
    """
    @author: eason.sun
    @param from_p:起点的经纬度，元组表示，如(纬度, 经度)
    @param param2:终点的经纬度，元组表示，如(纬度, 经度)
    @return:返回两点的距离描述
    
    @summary:通过起点和终点的经纬度计算两点的直线距离，然后根据距离返回描述内容
    """
    if from_p[0] == 0.0 or from_p[1] == 0.0 or to_p[0] == 0.0 or to_p[1] == 0.0:
        return ""
    dst = get_spherical_distance(from_p, to_p)
    if dst < 0.1:
        return "< 100m"
    dst = round(dst, 1)
    return "%skm" % dst


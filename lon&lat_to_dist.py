# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 09:42:55 2019

@author: kunkun_1230
"""


from math import *

def get_distance(origin, destination):
    # 根据经纬度计算两个点距离
    lon1 = radians(float(destination[0]))
    lon2 = radians(float(origin[0]))
    lat1 = radians(float(destination[1]))
    lat2 = radians(float(origin[1]))
    dlon = lon1 - lon2
    dlat = lat1 - lat2
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    dist = 2 * asin(sqrt(a))*6371*1000
    return dist

# -*- coding: utf-8 -*-
"""
Created on Tue May 15 09:46:22 2018

@author: kunkun_1230
"""

def isPointInPolygon(point,polyset):
    """
    输入数据：
        point=[x,y]为测试点的坐标
        polyset=[[x0,y0],[x1,y1],[x2,y2],[x3,y3],[x4,y4],……,[x0,y0]]为多边形顶点集合（按照顺时针或逆时针排列，且首尾为同一个点）
    输出：
        判断测试点是否在多边形内,在则返回1，否则返回0
    原理：
        从测试点向右侧引一条射线，计算和多边形交点的个数，如果个数为偶数个或者0，则点在多边形外；
        如果是奇数个，则在多边形内
    """
    flag=False   #线段在测试点右侧的数目为奇数个为True，否则为False
    if len(polyset)<4:
        return flag
     for i in range(len(polyset)-1):
        X0=polyset[i][0]
        Y0=polyset[i][1]
        X1=polyset[i+1][0]
        Y1=polyset[i+1][1]
        #测试点与多边形的某个顶点重合
        if(point[0]==X0 and point[1]==Y0)or(point[0]==X1 and point[1]==Y1):
            flag=True
            return flag
        #点在水平线段上
        elif Y0==Y1==point[1]:
            tmin=min(X0,X1)
            tmax=max(X0,X1)
            if tmin<point[0]<tmax:
                flag=True
                return flag
        #判断线段两端点是否在射线两侧
        elif(Y1<point[1] and Y0>=point[1])or(Y1>=point[1] and Y0<point[1]):
            temp=X1-(Y1-point[1])*(X1-X0)/(Y1-Y0)
            if(temp==point[0]):#测试点在线段上
                flag=True
                return flag
            elif(temp>point[0]):#线段在测试点右侧
                flag=not flag
   return flag

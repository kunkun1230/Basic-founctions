# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 09:42:55 2019

@author: kunkun_1230
"""

import folium

import pandas as pd

gps_log=pd.read_csv('E:/working_code/predict_work/route_deviation/gps_log_20190409.csv',header=0,sep=',')

m2 = folium.Map(location=[40.33444,116.644179],
              zoom_start=2,
              control_scale=True)
for i in range(20000,40000):
    folium.Circle(
            radius=100,
        location=[gps_log.iloc[i]['lat'], gps_log.iloc[i]['lon']],
        color='#3388ff',
        fill=True,
        fill_color='#FF66CC'
    ).add_to(m2)


m2.save('E:/working_code/predict_work/route_deviation/Heatmap5.html')




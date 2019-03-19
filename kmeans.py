#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 22:58:18 2019

@author: fan

K-means algorithm
"""

import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from __init__ import Dot
import pooling

        



# Initialize 100 dots
dots = list(range(90))
for i in range(90):
    dots[i] = Dot("none", [0,0])
i = 0
while i<90:
    if i<30:
        dots[i].position = [random.uniform(1.5, 2.5), random.uniform(4.5, 5.5)]
    if i<60 and i>=30:
        dots[i].position = [random.uniform(4, 6), random.uniform(1.5, 2.5)]
    if i<90 and i>=60:
        dots[i].position = [random.uniform(7.5, 9.5), random.uniform(7.5, 9.5)]
    i = i+1

# Initialize centroids
    colorList = ["red", "blue", "yellow", "green", "pink", "canyon"]
scale=[0.5,0.5]
thresh=0
cposition = pooling.preframe(dots, scale, thresh)
'''
cent = list(range(len(cposition)))
for i in range(len(cent)):
    cent[i].position = cposition[i]
    cent[i].color = colorList[i]

'''
#
#cent = [Dot("red", [2,5]), Dot("blue",[5,2] ), Dot("yellow", [8.5,8.5])]


'''
for k in range(1000):
    sumCluster = list(range(0,len(cent)))
    for i in range(len(cent)):
        sumCluster[i] = np.array([0,0])
    numCluster = list(range(0,len(cent)))
    for i in range(len(cent)):
        numCluster[i] = 0
    # assign each dot a color
    # and compute the mean of each cluster
    for v in dots:
        v.belong(cent)
        if v.color in colorList:
            sumCluster[colorList.index(v.color)] = sumCluster[colorList.index(v.color)] + np.array(v.position)
            numCluster[colorList.index(v.color)] = numCluster[colorList.index(v.color)] + 1

    for i in range(len(cent)):
        cent[i].position = (sumCluster[i]/numCluster[i]).tolist()
    

for v in cent:
    print(v.position, v.color)

for v in dots:
    plt.scatter(v.position[0], v.position[1], marker = 'x',color = v.color, s = 40)
#plt.scatter(x1, y1, marker = 'x',color = 'red', s = 40 ,label = 'First')
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:17:43 2019

max-out and pooling

@author: fan
"""

import math
from __init__ import Cell

def searchStein(cells, i, jset, L):
    if i not in jset:
        if cells[i].value>0 and (i not in jset):
            jset = jset | set([i])
            if i-L in list(range(len(cells))):
                a,_ = searchStein(cells, i-L, jset, L)
                jset = jset | a
            if i+L in list(range(len(cells))):
                a,_ = searchStein(cells, i+L, jset, L)
                jset = jset | a                
            if i+1 in list(range(len(cells))):
                a,_ = searchStein(cells, i+1, jset, L)
                jset = jset | a 
            if i-1 in list(range(len(cells))):
                a,_ = searchStein(cells, i-1, jset, L)
                jset = jset | a 
    return jset
A = Cell([1,1], 1)        

def preframe(dots, scale=[1,1],thresh=0):

    tmpXmin = 99999
    tmpXmax = 0
    tmpYmin = 99999
    tmpYmax = 0
    '''
    for v in dots:
        if tmpXmin>v.position[0]:
            tmpXmin = v.position[0]
        if tmpXmax<v.position[0]:
            tmpXmax = v.position[0]
        if tmpYmin>v.position[1]:
            tmpYmin = v.position[1]
        if tmpYmax < v.position[1]:
            tmpYmax = v.position[1]
    '''
    tmpXmin = 0
    tmpXmax = 10
    tmpYmin = 0
    tmpYmax = 10
    L = math.ceil((tmpXmax-tmpXmin)/scale[0])
    J = math.ceil((tmpYmax-tmpYmin)/scale[1])
    numCell = L*J 
    cells = list(range(numCell))

    for i in range(numCell):
        anchor = [i%L*scale[0], (i)/L*scale[1]]
        cells[i] = Cell(0, anchor)

    for d in dots:
        for i in range(len(cells)):
            if cells[i].anchor[0]<=d.position[0] \
            and cells[i].anchor[0]+scale[0]>d.position[0] \
            and cells[i].anchor[1]<=d.position[1] \
            and cells[i].anchor[1]+scale[1]>d.position[1]:
                cells[i].value += 1


    record = set()
    for i in range(numCell):
        if i not in record:
            record = record | set([i])
        
    record = set()
    core = []
    for i in range(numCell):
        if cells[i].value>0:
            core.append(i)
            searchStein(cells, i, record, L)


    ctroids = list(range(len(core)))
    for i in range(len(ctroids)):
        ctroids[i] = [i*scale[1], i/L*scale[0]]
    return ctroids
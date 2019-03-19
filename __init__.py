
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Tue Mar 19 15:29:36 2019
    
    @author: fan
    """

class Dot:
    def __init__(self, color="none", position=[0,0]):
        self.color = color
        self.position = position
    
    def belong(self, cent):
        length = len(self.position)
        tmp = [0]*len(cent)
        for j in range(len(cent)):
            for i in range(length):
                tmp[j] = tmp[j] + (self.position[i] - cent[j].position[i])**2
        c = tmp.index(min(tmp))
        self.color = cent[c].color

class Cell:
    def __init__(self, value=0, anchor=[0,0]):
        self.value = value
        self.anchor = anchor
        
    def search(self, dots):
        num = 0
        for v in dots:
            if v.position[0]>=anchor[0] and v.position[0]<anchor[0]+scale[0]:
                if v.position[1]>=anchor[1] and v.position[1]<anchor[1]+scale[1]:
                    num = num+1
        return num
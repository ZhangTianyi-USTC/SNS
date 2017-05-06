#!/usr/bin/env python
# encoding: utf-8

import numpy as np

# Parameters List
Nnet = 100      # Net size
Pnum = 100      # Number of persons
R_eff = 6       # "Six-degree relation"
R_th = 3        # "closest relation"
K = 0.27        # Movement factor
# K = 0.27 insures that two particles wouldn't cross each other if they are too close

# Class and implement
class Person:
    LatestID = 0    # record the latest ID
    def __init__(self,ID):
        self.ID = ID
        Person.LatestID += 1
    def merge(self,Prog_IDs):
        self.Prog_IDs = Prog_IDs
    def displace(self,Pos):
        '''
        type(Pos) = INT (or longlong)
        '''
        self.Pos = np.longlong(Pos)
    def gender(self,Sex):
        '''
        1: Male; 2: Female; 0: CP
        '''
        self.Sex = Sex
    def appeal(self,Weight):
        self.Weight = Weight
    def condition(self,Status):
        '''
        1: Stable; 2: unStable; 0: Single
        '''
        self.Status = Status

# Functions
def distance(P1, P2):
    deltaX, deltaY = P2.Pos - P1.Pos
    r = np.sqrt(deltaX**2 + deltaY**2)
    return r

def mapPosition(PList):
    for P in PList:
        Pos = P.Pos
        ID = P.ID
    '''
    作出以ID在坐标系中的二维分布图
    这个可以用来帮助圈定R_eff中的人际关系
    同时也能直观展示人际关系的演化情况
    同时实现FOF的功能
    '''

def findLover(P0, PList):
    def underScope(P1, P2):
        r = distance(P1, P2)
        if r <= R_eff:
            return True
        else:
            return False
    def inLove(P1, P2):
        r = distance(P1, P2)
        if r <= R_th:
            return True
        else:
            return False

def GravityField():
    def Gmove(P1, P2):
        '''
        P1's movement under P2's gravity pull
        '''
        r = distance(P1, P2)
        if r <= R_th:
            print "WTF?"
            return 0, 0
        W1, W2 = P1.Weight, P2.Weight
        F = W1*W2/(r**2)
        deltaR = K*F
        deltaX, deltaY = P2.Pos - P1.Pos
        deltaRx = deltaR*deltaX/r
        deltaRy = deltaR*deltaY/r
        return deltaRx, deltaRy




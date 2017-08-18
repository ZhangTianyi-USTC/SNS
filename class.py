#!/usr/bin/env python
# encoding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import random

# Parameters List
Nnet = 100      # Net size
Pnum = 100      # Number of persons
R_eff = 6       # "Six-degree relation"
R_th = 3        # "closest relation"
K = 0.27        # Movement factor
# K = 0.27 insures that two particles wouldn't cross each other if they are too close

# Class and implement
class Person:
    def __init__(self,ID,Sex):
        self.ID = ID    # ID > Pnum: Couples
        self.Sex = Sex  # 1: Male; 2: Female; 0: CP
    def couple(self,ProgIDs):
        '''
        type(ProgIDs) = Tuple
        '''
        self.ProgIDs = ProgIDs
    def locate(self,Pos):
        '''
        type(Pos) = Int (or longlong)
        '''
        self.Pos = np.longlong(Pos)
    def appeal(self,Weight):
        '''
        Apppealing weight: 0~10
        '''
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
def D2(P1, P2):
    deltaX, deltaY = P2.Pos - P1.Pos
    r2 = deltaX**2 + deltaY**2
    return r2

def FOF(PList):
    def underScope(P1, P2):
        r2 = D2(P1, P2)
        if r2 <= R_eff**2:
            return True
        else:
            return False
    def idPair(PList):
        Length = len(PList)
        pairIDList = []
        for ind in range(Length-1):
            for subind in range(ind+1,Length):
                P1 = PList[ind]
                P2 = PList[subind]
                if underScope(P1, P2):
                    pairIDList.append([ind,subind])
                else:
                    continue
        return pairIDList
    pairIDList = idPair(PList)
    pairLen = len(pairIDList)
    # No. of pairIDs
    pairNumList = range(pairLen)
    def match(pairID1, pairID2):
        for id1 in pairID1:
            for id2 in pairID2:
                if id1 == id2:
                    return True
        return False
    for ind in range(pairLen-1):
        for subind in range(ind+1,pairLen):
            pairID1 = pairIDList[ind]
            pairID2 = pairIDList[subind]
            if match(pairID1, pairID2):
                Num1 = pairNumList[ind]
                Num2 = pairNumList[subind]
                MinNum = min(Num1,Num2)
                pairNumList[ind] = MinNum
                pairNumList[subind] = MinNum
    # divided into groups
    GroupNumList = np.unique(pairNumList)
    pairIDList = np.longlong(pairIDList)
    GroupList = []
    for GroupNum in GroupNumList:
        indexs = np.where(np.longlong(pairNumList) == GroupNum)[0]
        personIDList = []
        for pairIDs in pairIDList[indexs]:
            personIDList += pairIDs.tolist()
        pIDs = np.unique(personIDList)
        subPList = []
        for pID in pIDs:
            subPList.append(PList[pID])
        GroupList.append(subPList)
    return GroupList

def findLover(P0, FoFList):
    def inLove(P1, P2):
        r2 = D2(P1, P2)
        if r2 == 0: # itself
            return False
        if r2 <= R_th**2:
            return True
        else:
            return False
    def competitor(P0, subPList):
        Winner = subPList[0]
        for subPerson in subPList:
            if Winner.Weight < subPerson.Weight:
                Winner = subPerson
            elif Winner.Weight == subPerson.Weight:
                Choice = random.randint(0,1)
                Winner = (Winner, subPerson)[Choice]
        return Winner
    subPList = []
    for Person in FoFList:
        if inLove(P0, Person):
            subPList.append(Person)
    Winner = competitor(P0, subPList)
    return Winner

def mapPosition(PList):
    XList = []
    YList = []
    for P in PList:
        # ID = P.ID
        Pos = P.Pos
        XList.append(Pos[0])
        YList.append(Pos[1])
    plt.clf()
    plt.plot(XList,YList)
    plt.show()

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




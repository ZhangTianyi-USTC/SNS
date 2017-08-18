#!/usr/bin/env python
# encoding: utf-8

import random
import function as func

# Parameters
Nnet = func.Nnet
Pnum = func.Pnum
R_eff = func.R_eff
R_th = func.R_th

# Sprinkle
PList = []
for ID in range(Pnum):
    Sex = random.randint(0,1)
    Weight = 5  # Const
    person = func.Person(ID,Sex)
    person.appeal(Weight)
    x = random.randint(0,Nnet-1)
    y = random.randint(0,Nnet-1)
    Pos = [x,y]
    person.locate(Pos)
    PList.append(person)

# FOF
GroupList = func.FOF(PList)
print "Num of Groups:", len(GroupList)
func.mapPosition(PList)
func.mapGroup(GroupList)

# find lover
Sum = 0
for Group in GroupList:
    for P0 in Group:
        Lover = func.findLover(P0,Group)
        if P0 != Lover:
            Sum += 1
print "Num of CPs:", Sum/2  # double

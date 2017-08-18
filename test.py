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
    person = func.Person(ID,Sex)
    x = random.randint(0,Nnet-1)
    y = random.randint(0,Nnet-1)
    Pos = [x,y]
    person.locate(Pos)
    PList.append(person)

# FOF
GroupList = func.FOF(PList)
print len(GroupList)
func.mapPosition(PList)
func.mapGroup(GroupList)

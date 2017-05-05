#!/usr/bin/env python
# encoding: utf-8

import numpy as np

class Person:
    def __init__(self,ID):
        self.ID = ID
    def merge(self,Prog_IDs):
        self.Prog_IDs = Prog_IDs
    def displace(self,Pos):
        self.Pos = Pos
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





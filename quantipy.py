#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 15:45:52 2017

@author: robertgeiger
"""

import ast
import inspect
import re
import math
import matplotlib.pylab as plt
from unitpy import *

plt.close('all')


'''

TODO:
    1) Create a complete list of reference units (u_ref)
    2) Implement RE for all possible combinations of unit names
    3) Create a function to parse 'unit' strings and convert them to Symbols
    3) Create a lookup function to determine 'name' of unit based on symbols

'''
    
class qty(object):
    _units = units()
    
    def __init__(self,v,u='',p = 16):
        self._p = p
        self._v = v
        self._u = u        
        self.o = str(self._v)+ ' ' + self._u
                    
    def __str__(self):
        return str(self._v) + " '" + self._u + "'"
    
    # u: unit
    @property
    def u(self):
        return self._u
    
    # v: value
    @property
    def v(self):
        return self._v

    # p: precision
    @property
    def p(self):
        return self._p
            
    @u.setter
    def u(self,u):
        
        try:                     
            # if the unit is changed, convert the value
            if u != self.u and self.u != '':             
                if not self._units.unitExists(u):
                    print('Unrecognized unit!')
                    return False
                
                if not self._units.unitMatch(self.u,u):
                    print('Units do not match!')
                    return False
       
                if type(self.v) == list:
                    tmp = []
                    try:
                        for i in self.v:
                            tmp.append(self._units.convert(i,self.u,u))
                        self._v = tmp
                    except:
                        print('Error in values!')
                        return False    
                else:
                    self.v = self._units.convert(self.v,self.u,u)

            # update unit
            self._u = u
            self.o = str(self._v)+ ' ' + self._u
            return True

        except:
            self._u = u
            return True
        
    @v.setter
    def v(self,v):
        if type(v) == list:
            tmp = []
            for i in v:
                if type(i) in [int,float]:    
                    tmp.append(round(i,self.p))
                elif type(i) == str:
                    # Attempt to determine the datatype within the string
                    val = self.getDataType(i)
                    if val == 'f':
                        tmp.append(round(float(i),self.p))
                    elif val == 'i':
                        tmp.append(round(int(i),self.p))
                    else:
                        self._v = 0
                        print('Unsupported input')
                        return False
                else:
                    print('Unsupported input')
                    return False
            self._v = tmp
            return True
        elif type(v) in [int, float]:
            self._v = round(v,self.p)
        elif type(v) == str:
            # Attempt to determine the datatype within the string
            val = self.getDataType(v)
            print(val)
            if val == 'f':
                self._v = round(float(v),self.p)
            elif val == 'i':
                self._v = round(int(v),self.p)
            else:
                self._v = 0
                print('Unsupported input')
                return False
        return True
    
    @p.setter
    def p(self,p):
        try:
            if p != self._p:
                self._p = p
                self._v = round(self._v,int(p))
            return True
        except:
            self._p = p
            return True
    
    # Math  
    '''
    General template used by all operations
    
    TODO: must match units... doesn't convert units to same units before vaildating comparison operations and possible other operations
    '''
    def __generalMath(self,other):  

        if isinstance(other,qty): 
            new_v = other.v
            func = inspect.getouterframes(inspect.currentframe(),2)[1][3]    
            if func in ['__add__','__sub__']:
                if self._units.unitMatch(self.u,other.u):
                    if self.u != other.u:
                        new_v = self._units.convert(other.v,other.u,self.u)
                    new_u = self.u
                else:
                    new_u = self.u + ' + ' + other.u
                    print('Check your units!')
            else:
                new_u = self.u

            return new_v,new_u
        
        if type(other) in [int, float]:        
            return other,self.u
        
        
    def __add__(self,other):
        try:
            v,u = self.__generalMath(other)
            return qty(self.v + v,u)
        except:
            return NotImplemented

    def __sub__(self,other):
        try:
            v,u = self.__generalMath(other)
            return qty(self.v - v,u)
        except:
            return NotImplemented
            
    def __mul__(self,other):
        try:
            v,u = self.__generalMath(other)
            return qty(self.v * v,u)
        except:
            return NotImplemented
            
    def __truediv__(self,other):
        try:
            v,u = self.__generalMath(other)
            return qty(self.v / v,u)
        except:
            return NotImplemented
            
    def __flowdiv__(self,other):
        try:
            v,u = self.__generalMath(other)
            return qty(self.v // v,u)
        except:
            return NotImplemented
            
    def __mod__(self,other):
        try:
            v,u = self.__generalMath(other)
            return qty(self.v % v,u)
        except:
            return NotImplemented

    def __pow__(self,other):
        try:
            v,u = self.__generalMath(other)
            return qty(self.v ** v,u)
        except:
            return NotImplemented
            
    # Compare
    def __lt__(self,other):
        try:
            v,u = self.__generalMath(other)
            return self.v < v
        except:
            return NotImplemented
        
    def __le__(self,other):
        try:
            v,u = self.__generalMath(other)
            return self.v <= v
        except:
            return NotImplemented

    def __eq__(self,other):
        try:
            v,u = self.__generalMath(other)
            return self.v == v
        except:
            return NotImplemented

    def __ne__(self,other):
        try:
            v,u = self.__generalMath(other)
            return self.v != v
        except:
            return NotImplemented

    def __gt__(self,other):
        try:
            v,u = self.__generalMath(other)
            return self.v > v
        except:
            return NotImplemented

    def __ge__(self,other):
        try:
            v,u = self.__generalMath(other)
            return self.v >= v
        except:
            return NotImplemented

    def __int__(self):
        return int(self.v)
    
    def __float__(self):
        return float(self.v)
    
    def __index__(self):
        pass
    
    def getDataType(self,s):
        #TODO: Perform Error Handling on Input
        '''
        s = string
        b = binary
        i = int
        f = float
        n = null
        
        '''
        s=s.strip()
        if len(s) == 0: return 'n'
        try:
            t=ast.literal_eval(s)
    
        except ValueError:
            return 's'
        except SyntaxError:
            return 's'
    
        else:
            if type(t) in [int, float, bool]:
                if t in set((True,False)) and type(t) != float:
                    return 'b'
                if type(t) is int:
                    return 'i'
                if type(t) is float:
                    return 'f'
            else:
                return 's' 

    def __str__(self):
        return str(self.v) + ' ' + str(self.u)
    
    def __repr__(self):
        return str(self.v) + ' ' + str(self.u)


if __name__ == "__main__":

    '''

    Test ground
    
    '''
    units  = units()
    A = qty(10,'ft')
    B = qty(10,'m')
    C = qty(1.225,'g')

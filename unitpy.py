#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 16:01:57 2017

@author: robertgeiger
"""

from sympy import Symbol

class units():
    baseunits = {
        'tempearture'       : {'symbol': Symbol('T'),'unit':['kelvin','k']},
        'length'            : {'symbol': Symbol('L'),'unit':['meter','m']},
        'mass'              : {'symbol': Symbol('M'),'unit':['gram','g']},
        'current'           : {'symbol': Symbol('I'),'unit':['ampere','a']},
        'amount'            : {'symbol': Symbol('N'),'unit':['mole','mol']},
        'time'              : {'symbol': Symbol('t'),'unit':['second','sec','s']},
        'intensity'         : {'symbol': Symbol('J'),'unit':['candela','cd']}
    }
    
    u_ref = {
    # Temperatures
        'f' :       { 'names' : ['f','fahrenheit','of','fo'], 'symbol' :  Symbol('T')},
        'c' :       { 'names' : ['c','celsius','oc','co'], 'symbol' :  Symbol('T')},
        'r' :       { 'names' : ['r','rankine','or','ro'], 'symbol' :  Symbol('T')},
        'k' :       { 'names' : ['k','kelvin','ok','ko'], 'symbol' :  Symbol('T')},
    # Pressure
        'psi' :     { 'names' : ['psi','lb/in2','lb/in^2','lb/in**2'], 'symbol' :  Symbol('M')/ Symbol('L')* Symbol('t')**2},
        'atm' :     { 'names' : ['atm'], 'symbol' : Symbol('M')/Symbol('L')*Symbol('t')**2},
    # Volume Flow Rates
        'scfh' :    { 'names' : ['scfh','ft3/hr','ft^3/hr','ft**3/hr'], 'symbol' : Symbol('L')**3/Symbol('t')},
        'scfm' :    { 'names' : ['scfm','ft3/min','ft^3/min','ft**3/min'], 'symbol' : Symbol('L')**3/Symbol('t')},
        'slph' :    { 'names' : ['slph','liter/hr','l/hr'], 'symbol' : Symbol('L')**3/Symbol('t')},
        'slpm' :    { 'names' : ['slpm','liter/min','l/min'], 'symbol' : Symbol('L')**3/Symbol('t')},

    # Density
        'g/l' :     {'names' : ['g/l','gram/liter','grams/liter','gram/litre','grams/litre'],'symbol' : Symbol('M')/Symbol('L')**3},
        'kg/m3' :   {'names' : ['kg/m3','kilogram/m3','kilograms/m3','kilogram/m^3','kilograms/m^3'],'symbol' : Symbol('M')/Symbol('L')**3}        
    }
    
    dimensionless = {
                 'radian'    :      {'factor'  : 1.0       , 'names' : ['radians']},
                 'steradian' :      {'factor'  : 1.0       , 'names' : ['sr', 'steradians']},
                 'degree'    :      {'factor'  : 0.01745329251994,   'names'  : ['deg', 'degrees']},
                 'arcminute' :      {'factor'  : 0.0002908882086657, 'names'  : ['arcmin', 'arcminutes', 'arc-minute', 'arc-minutes']},
                 'arcsecond' :      {'factor'  : 4.848136811095e-6,  'names'  : ['arcsec', 'arcseconds', 'arc-second', 'arc-seconds']},
                 'pi'        :      {'factor'  : 3.1415926535897931, 'names'  : []},
                 'unity'     :      {'factor'  : 1.0       , 'names' : []},
                 'zero'      :      {'factor'  : 0         , 'names' : []},
                 'one'       :      {'factor'  : 1         , 'names' : []},
                 'two'       :      {'factor'  : 2         , 'names' : []},
                 'three'     :      {'factor'  : 3         , 'names' : []},
                 'four'      :      {'factor'  : 4         , 'names' : []},
                 'five'      :      {'factor'  : 5         , 'names' : []},
                 'six'       :      {'factor'  : 6         , 'names' : []},
                 'seven'     :      {'factor'  : 7         , 'names' : []},
                 'eight'     :      {'factor'  : 8         , 'names' : []},
                 'nine'      :      {'factor'  : 9         , 'names' : []},
                 'dozen'     :      {'factor'  : 12.0      , 'names' : []},
                 'gross'     :      {'factor'  : 144.0     , 'names' : []},
                 'ten'       :      {'factor'  : 10.0      , 'names' : []},
                 'twenty'    :      {'factor'  : 20.0      , 'names' : []},
                 'thirty'    :      {'factor'  : 30.0      , 'names' : []},
                 'forty'     :      {'factor'  : 40.0      , 'names' : []},
                 'fifty'     :      {'factor'  : 50.0      , 'names' : []},
                 'sixty'     :      {'factor'  : 60.0      , 'names' : []},
                 'seventy'   :      {'factor'  : 70.0      , 'names' : []},
                 'eighty'    :      {'factor'  : 80.0      , 'names' : []},
                 'ninety'    :      {'factor'  : 90.0      , 'names' : []},
                 'hundred'   :      {'factor'  : 100.0     , 'names' : []},
                 'thousand'  :      {'factor'  : 1000.0    , 'names' : []},
                 'million'   :      {'factor'  : 1.0e6     , 'names' : []},
                 'billion'   :      {'factor'  : 1.0e9     , 'names' : []},
                 'trillion'  :      {'factor'  : 1.0e12    , 'names' : []},
                 'quadrillion' :    {'factor'  : 1.0e15    , 'names' : []},
                 'quintillion' :    {'factor'  : 1.0e18    , 'names' : []},
                 'percent'    :     {'factor'  : 0.01      , 'names' : ['%', 'percent']},
                 'tenth'      :     {'factor'  : 0.1       , 'names' : []},
                 'hundredth'  :     {'factor'  : 0.01      , 'names' : []},
                 'thousandth' :     {'factor'  : 0.001     , 'names' : []},
                 'millionth'  :     {'factor'  : 1.0e-6    , 'names' : []},
                 'billionth'  :     {'factor'  : 1.0e-9    , 'names' : []},
                 'trillionth' :     {'factor'  : 1.0e-12   , 'names' : []},
                 'quadrillionth':   {'factor'  : 1.0e-15   , 'names' : []},
                 'quintillionth':   {'factor'  : 1.0e-18   , 'names' : []},
             }

    prefix = {
                 'Y'        :     {'factor'  : 1.0e24    , 'names' : ['Y','yotta']},
                 'Z'        :     {'factor'  : 1.0e21    , 'names' : ['Z','zetta']},
                 'E'        :     {'factor'  : 1.0e18    , 'names' : ['E','exa']},
                 'P'        :     {'factor'  : 1.0e15    , 'names' : ['P', 'peta']},
                 'T'        :     {'factor'  : 1.0e12    , 'names' : ['T', 'tera']},
                 'G'        :     {'factor'  : 1.0e9     , 'names' : ['G', 'giga']},
                 'M'        :     {'factor'  : 1.0e6     , 'names' : ['M', 'mega']},
                 'k'        :     {'factor'  : 1000.0    , 'names' : ['k', 'kilo']},
                 'h'        :     {'factor'  : 100.0     , 'names' : ['h', 'hecto']},
                 'da'       :     {'factor'  : 10.0      , 'names' : ['da', 'deca', 'deka', 'deca']},
                 'd'        :     {'factor'  : 0.1       , 'names' : ['d', 'deci']},
                 'c'        :     {'factor'  : 0.01      , 'names' : ['c', 'centi']},
                 'm'        :     {'factor'  : 0.001     , 'names' : ['m', 'milli']},
                 'u'        :     {'factor'  : 1.0e-6    , 'names' : ['u', 'micro']},
                 'n'        :     {'factor'  : 1.0e-9    , 'names' : ['n', 'nano']},
                 'p'        :     {'factor'  : 1.0e-12   , 'names' : ['p', 'pico']},
                 'f'        :     {'factor'  : 1.0e-15   , 'names' : ['f', 'femto']},
                 'a'        :     {'factor'  : 1.0e-18   , 'names' : ['a', 'atto']},
                 'z'        :     {'factor'  : 1.0e-21   , 'names' : ['z', 'zepto']},
                 'y'        :     {'factor'  : 1.0e-24   , 'names' : ['y', 'yocto']}
        }
            
    simpleunits = {
        'length' : {
                 'm'        :    {'factor'  : 1.0      ,  'names' : ['m', 'meters','meter', 'metres','metre']},
                 'angs'     :    {'factor'  : 1.0e-10  ,  'names' : ['ang', 'angstroms']},
                 'ft'       :    {'factor'  : 0.3048   ,  'names' : ['ft', 'feet']},
                 'in'       :    {'factor'  : 0.0254   ,  'names' : ['in', 'inches']},
                 'mi'       :    {'factor'  : 1609.344 ,  'names' : ['mi', 'miles']},
                 'nautical-mile' : {'factor'  : 1852.0   ,  'names' : ['nm', 'nauticalmiles', 'nauticalmile', 'nautical-miles']},
                 'astronomical-unit' : {'factor'  :  1.49598e11 , 'names' : ['au']},
                 'ly'         :    {'factor'  : 9.46e15    , 'names' : ['ly', 'light-years', 'lightyear', 'lightyears']},
                 'parsec'     :    {'factor'  : 3.083e16   , 'names' : ['parsecs']},
                 'fathom'     :    {'factor'  : 1.8054     , 'names' : ['fathoms']},
                 'yard'       :    {'factor'  : 0.9144     , 'names' : ['yd', 'yards']},
                 'rod'        :    {'factor'  : 5.0292     , 'names' : ['rods']},
                 'mil'        :    {'factor'  : 0.0000254  , 'names' : ['mils']},
                 'furlong'    :    {'factor'  : 201.168    , 'names' : ['furlongs']}
                },
        
        'mass' : {
                'kg'        :   {'factor'  : 1.0           , 'names' : ['kg', 'kilograms']},
                'hg'        :   {'factor'  : 0.1           , 'names' : ['hg', 'hectograms']},
                'dag'       :   {'factor'  : 0.01          , 'names' : ['dag', 'dekagrams', 'decagram', 'decagrams']},
                'g'         :   {'factor'  : 0.001         , 'names' : ['gm', 'grams']},
                'dg'        :   {'factor'  : 0.0001        , 'names' : ['dg', 'decigrams']},
                'cg'        :   {'factor'  : 0.00001       , 'names' : ['cg', 'centigrams']},
                'mg'        :   {'factor'  : 1.0e-6        , 'names' : ['mg', 'milligrams']},
                'ug'        :   {'factor'  : 1.0e-9        , 'names' : ['ug', 'micrograms']},
                'metric-ton'  :   {'factor'  : 1000.0        , 'names' : ['metric-tons', 'tonne', 'tonnes']},
                'pound'       :   {'factor'  : 0.45359237    , 'names' : ['lb', 'lbs','pound', 'pounds']},
                'slug'        :   {'factor'  : 14.593902937  , 'names' : ['slugs']},
                'atomic-mass-unit' :     {'factor'  : 1.6605402e-27 , 'names' : ['amu', 'atomic-mass-units']},
                },
        'time' : {
               's'          :   {'factor'  : 1.0   ,     'names' : ['s','sec','secs','second','seconds']},
               'min'        :   {'factor'  : 60    ,     'names' : ['min', 'minutes']},
               'hr'         :   {'factor'  : 3600  ,     'names' : ['hr', 'hours']},
               'day'        :   {'factor'  : 86400 ,     'names' : ['days']},
               'wk'         :   {'factor'  : 604800,     'names' : ['wk', 'weeks']},
               'fortnight'  :   {'factor'  : 1209600,    'names' : ['fortnights']},
               'month'      :   {'factor'  : 2629728,    'names' : ['mon', 'months']},
               'yr'         :   {'factor'  : 31556736,   'names' : ['yr', 'years']},
               'century'    :   {'factor'  : 3155673600, 'names' : ['century','centuries']}
                },
        'current' : {
                'amp'      :   {'factor'  : 1.0, 'names' : ['A','a','amp','amps','ampere','amperes']}          
                },
        'temperature' : {
                'k'      :   {'factor'  : 1.0, 'names' : ['k','K','kelvin','kelvins']},
                'r'     :   {'factor'  : 5/9, 'names' : ['r','R','rankine','rankines']}             
                },
        'luminosity' : {
                'cd'     :   {'factor'  : 1.0, 'names' : ['cd','candela','candelas']}
                },
        'amount' : {
                'mol'        :   {'factor'  : 1.0, 'names' : ['mol','mole','moles']}
                },
        'money' : {
                '$'      :   {'factor'  : 1.0, 'names' : ['dollar','dollars','$', 'buck','bucks']}
                } 
    }
    

    derivedunits = {
        'frequency' : {
                'hz'    : {'factor'     : 1/simpleunits['time']['s']['factor'], 'names' : ['hz','Hz','1/s','hertz']}  
                },
        'area' : {
                
                },
        'volume' : {
                'l'     : {'factor'     : 1000, 'names' : ['l','liter','liters','litre','litres']}
                
                },
        'volumetric flow rate' : {
                
                },
            }
    
    unit_list = []
    for k,v in simpleunits.items():
        for k2,v2 in v.items():
            unit_list.append(v2['names'])
    unit_list = [j for i in unit_list for j in i]
    unit_list.sort()
    
    def __init__(self,u=''):
        for k,v in self.baseunits.items():
            if u.lower() in v['unit']:
                print('Base Unit')

        '''
        Use utility functions to add units to list
        '''
        self.simpleunits['length'].update(self.addPrefix('m',self.simpleunits['length']['m']['factor'],self.simpleunits['length']['m']['names']))
        self.simpleunits['time'].update(self.addPrefix('s',self.simpleunits['time']['s']['factor'],self.simpleunits['time']['s']['names']))
        self.simpleunits['current'].update(self.addPrefix('amp',self.simpleunits['current']['amp']['factor'],self.simpleunits['current']['amp']['names']))
        self.simpleunits['amount'].update(self.addPrefix('mol',self.simpleunits['amount']['mol']['factor'],self.simpleunits['amount']['mol']['names']))
    
        self.derivedunits['frequency'].update(self.addPrefix('hz',self.derivedunits['frequency']['hz']['factor'],self.derivedunits['frequency']['hz']['names']))
        self.derivedunits['area'].update(self.contProd('length'))
        self.derivedunits['volume'].update(self.addPrefix('l',self.derivedunits['volume']['l']['factor'],self.derivedunits['volume']['l']['names']))
        self.derivedunits['volume'].update(self.contProd('length',3))
    
    '''
    
    Utility Functions
    
    '''
    def addPrefix(self,unit,factor=1,basename=''):
        if basename == '':
            basename = unit
            
        d = {}
        for k,v in self.prefix.items():
            d[k+unit] = {'factor' : v['factor']*factor,'names':[x1+x2 for x1 in v['names'] for x2 in basename]}
        return d
    
    #Function for multiplying simpleunits
    def contProd(self,base,num=2):
        
        try:
            d = {}
            for k,v in self.simpleunits[base].items():            
                d[k+str(num)] = {'factor': v['factor']**num,'names':[k+str(num),k+'^'+str(num),k+'**'+str(num)]}
            return d
        except:
            print('Base not found.')
            return 0
    
    def prod(self, b1, b2):
        pass
    
    def factor(self,unit):
        if type(unit) in [float, int]:
            return unit
        
        # Check if it is a simple unit
        match = {}
        for k,v in self.simpleunits.items():
            for k2,v2 in v.items():
                if unit in v2['names']:
                    match[unit]=v2

        # Check if it is a derived unit
        for k,v in self.derivedunits.items():
            for k2,v2 in v.items():
                if unit in v2['names']:
                    match[unit]=v2

        if len(match) == 0:
            print('Unit not found')
            return 0
        if len(match) == 1:
            return match[unit]['factor']
        elif len(match) > 1:
            print('Multiple units found')
            return 0

        return 0
                

        
    '''
    Can accept
    convert(qty1,qty2)
    convert(qty1,to)
    convert(x,from,to)
    '''
    def convert(self,*args):
        # Input flexibility... pull out value,from, and to
        if len(args) == 3:
            x = args[0]
            f = args[1]
            t = args[2]
        elif len(args) == 2:
            if isinstance(args[0],qty):
                x = args[0].v
                f = args[0].u
                if isinstance(args[1],qty):
                    t = args[1].u
                elif type(args[1]) == str:
                    t = args[1]
                else:      
                    print('Invalid type to convert to!')                      
                    t = '' # default
            else:
                print('Invalid type to convert from!')
                return 0
        else:
            print('Invalid Input!')
            return 0

        # Handle Temperature Conversion
        celsius     = ['c','C','celsius']
        kelvin      = ['k','K','kelvin','kelvins']
        fahr        = ['f','F','fahrenheit','Fahrenheit']
        rankine     = ['r','R','rankine','Rankine']
        if f in fahr:
            if t in rankine:
                return x+459.67
            elif t in celsius:
                return (x-32)*5/9
            elif t in kelvin:
                return (x+459.67)*5/9
            else:
                print('Unknown "To" Unit')
                return x        
        
        if f in celsius:
            if t in fahr:
                return (x*9/5)+32
            elif t in kelvin:
                return x+273.15
            elif t in rankine:
                return (x+273.15)*9/5
            else:
                print('Unknown "To" Unit')
            return x        
                
        if f in kelvin:
            if t in rankine:
                return x*9/5
            elif t in fahr:
                return x*9/5-459.67
            elif t in celsius:
                return x-273.15
            else:
                print('Unknown "To" Unit')
            return x        
                
        if f in rankine:
            if t in celsius:
                return (x-491.67)*5/9
            elif t in fahr:
                return x-459.67
            elif t in kelvin:
                return x*5/9
            else:
                print('Unknown "To" Unit')
            return x        
                                
             
        ff = self.factor(f)
        ft = self.factor(t)
        try:
            f = ff/ft
        except:
            print('error converting units: ',ff,ft)
            f = 1 

        return x*f
    
        '''
        {
        # Temperature Conversion
            'f->r' : x+459.67,
            'f->c' : (x-32)*5/9.,
            'f->k' : (x+459.67)*5/9.,
            'c->f' : (x*9/5.)+32,
            'c->k' : x+273.15,
            'c->r' : (x+273.15)*9/5,
            'k->r' : x*9/5.,
            'k->f' : x*9/5.-459.67,
            'k->c' : x-273.15,
            'r->c' : (x-491.67)*5/9.,
            'r->f' : x-459.67,
            'r->k' : x*5/9.,
        #Pressure
            'psi->atm' : x/14.7,
            'atm->psi' : x*14.7,
        # Volume Flow Rates Conversion
            'scfh->scfm' : x/60.,
            'scfh->slph' : x*28.32,
            'scfh->slpm' : x*28.32/60,
            'scfm->scfh' : x*60.,
            'scfm->slpm' : x*28.32,
            'scfm->slph' : x*28.32*60.,
            'slpm->scfh' : x/28.32*60.,
            'slpm->scfm' : x/28.32,
            'slpm->slph' : x*60.,
            'slph->slpm' : x/60.,
            'slph->scfh' : x/28.32,
            'slph->scfm' : x/28.32/60,   
        # Density
            'g/l->kg/m3' : x,
            'kg/m3->g/l' : x,
        # Default
            '' : x
        }[f+'->'+t]
        '''
        
    def unitExists(self,u):
        if u in self.unit_list:
            return True
        return False
    
    def unitMatch(self,a,b):
        # This is poor... make it better
        for k1,v1 in self.simpleunits.items():
            for k,v in v1.items():
                if a in v['names']:
                    s_a = k1
                if b in v['names']:
                    s_b = k1
            try:
                if s_a == s_b:
                    return True
                return False
            except:
                print('Unrecognized unit!')
                return False                
    
    def strToSymbols(self,s):
        pass
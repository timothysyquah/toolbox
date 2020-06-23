#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 23:53:05 2020

@author: tquah
"""

import os
IDIR = os.getcwd()
components = IDIR.split('/')
path_to_tools = '/'+components[1]+'/'+components[2]+'/.timtools'
op = open(path_to_tools,'r')
chainpath =op.read()+'/geninput/'
op.close()
import sys
sys.path.append(chainpath)

from Chains import Lazy_Input_Generator
#from string import 
    
#Bottlebrush Build

chain_label = 'AB-Bottlebrush'
backbone_composition = [0.5,0.5]
backbone_species = [1,2]
backbone_length = 5
backbone_statistics = 'DGC'

backbone_list = [backbone_statistics,backbone_length,backbone_species,\
                 backbone_composition]

sidearm_composition = [1.0]
sidearm_species = [1]
sidearm_length = 5.0
sidearm_statistics = backbone_statistics
sidearm_coverage1 = 0.5
spacing = 1
sidechain_1_list = [sidearm_statistics,sidearm_length,sidearm_species,\
                 sidearm_composition,sidearm_coverage1,spacing]

sidearm_composition = [1.0]
sidearm_species = [2]
sidearm_length = sidearm_length
sidearm_statistics = backbone_statistics
sidearm_coverage = 1-sidearm_coverage1
sidechain_2_list = [sidearm_statistics,sidearm_length,sidearm_species,\
                 sidearm_composition,sidearm_coverage,spacing]

chain_list = [backbone_list,sidechain_1_list,sidechain_2_list]

#dynamic parameters
dt = 0.002
stress_scale = 0.001
force_scale = [1.0,0.02]
#parameters 
field = './fields.in'
test_file = './LAM.in'
dS = 1
d = 1
initial_box = 20
npw = 1024
chiN = [1.0]
# Make Input File
Lazy_Input_Generator(test_file,field,chain_list,chiN,dS,npw,dt,\
                         initial_box,stress_scale,force_scale,d,chain_label,\
                         diffuser_method='SOS',Nref=1,invzeta=0.1,\
                         kuhn_length=[1.0],stress_tol=1e-5,\
                         force_tol=5e-5)

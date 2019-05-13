# -*- coding: utf-8 -*-
"""
Created on Mon May 13 20:13:08 2019

@author: YS15101711
"""

import numpy as np
import pylab as pl
from matplotlib import collections  as mc

from devolve3 import Generation
from prime import createDict


N = 10
initDict = createDict(N)
gen0 = Generation(initDict)
gen0parents = gen0.getParentDict()

nextGen = 1
prevGen = 0
lines = []
for key, val in gen0parents.items():
    if -1 not in val:
        line = []
        for v in val:
            relations = [(key, nextGen), (v, prevGen)]
            lines.append(relations)

        
lc = mc.LineCollection(lines, linewidths=2)
fig, ax = pl.subplots()
ax.add_collection(lc)
ax.autoscale()
ax.margins(0.1)

N = 10
initDict = createDict(N)
currentGen = Generation(initDict)
numGen = 4
allLines = []
for i in range(numGen):
    nextGen = i + 1
    prevGen = i
    lines = []
    parentDict = currentGen.getParentDict()
    for key, val in parentDict.items():
        if -1 not in val:
            line = []
            for v in val:
                relations = [(key, nextGen), (v, prevGen)]
                lines.append(relations)
    allLines.append(lines)
    currentGen = Generation(parentDict)
    
fig, ax = pl.subplots()
for line in allLines:
    print(line)
    lc = mc.LineCollection(line, linewidths=2)
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins()
    
    
    








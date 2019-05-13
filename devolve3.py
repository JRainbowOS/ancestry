# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:20:11 2019

@author: YS15101711
"""

from prime import isPrime, firstNPrimes
from prime import timing, createDict
from visualize import cleanDict, plotSurvivors, barrenIdx

import numpy as np

def devolve(startingGen, numGen):
    currentGen = startingGen
    i = 0
    if numGen < 1:
        return currentGen
    else:
        while i < numGen:
#            print('{} generations ago.'.format(i))
            prevGen = Generation(currentGen.getParentDict())
#            print(prevGen.progenyDict)
            currentGen = prevGen
            i += 1
    return prevGen
    
    

class Generation:
    
    def __init__(self, progenyDict):
        self.progenyDict = progenyDict
        self.progeny = progenyDict.values()
        self.size = len(progenyDict)
        self.ids_ = np.arange(len(progenyDict))
        self.parentArr = self.getParentArr()
            
    def getIDs(self):
        return self.ids_
    
    def getParentArr(self):
#        TODO: get seed working  
#        TODO: generate this from self.parentDict
#        TODO: shouldn't start with a 2
        result_array = np.empty((2), int)
        for i in range(self.size):
            result = np.random.choice(self.size, 2, replace=False)
            result_array = np.append(result_array, result, axis=0)
        return result_array[2: ]
            
    def getParentDict(self):
#        TODO: FIX THIS! appending to numpy array / list issue
        parentArr = self.parentArr
        parentDict = {}
        progenyDict = self.progenyDict
        for i in range(self.size):
            alreadyRelated = progenyDict[i]
            idxs = np.where(parentArr == i)[0]
            if len(idxs) == 0:
                childrenID = [-1]
                alreadyRelated = [-1]
                newRelated = [-1]
            elif len(idxs) == 1:
                childrenID = (idxs / 2).astype(np.int32)
                newRelated = np.append(alreadyRelated, childrenID)
            else:
                childrenID = (idxs / 2).astype(np.int32)
                newRelated = np.append(alreadyRelated, childrenID)
            # de-dupe
            newRelated = np.array(list(set(newRelated)))
            parentDict[i] = newRelated
            if np.isin(-1, parentDict[i]):
#                kill off individuals who have no surviving progeny
                parentDict[i] = np.array([-1])
        return parentDict      
            

def main():
    N = 6
    initDict = createDict(N)
    
    
    presentGen = Generation(initDict)
    M = 10
    backMGens = devolve(presentGen, M)
    
    k, v = cleanDict(backMGens.progenyDict)
    plotSurvivors(k, v)
    
    barren = barrenIdx(v)
#    print(barren)

if __name__ == '__main__':    
    main()





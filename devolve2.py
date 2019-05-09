# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:20:11 2019

@author: YS15101711
"""

from prime import isPrime, firstNPrimes
from prime import timing
import numpy as np

def devolve(startingGen, numGen):
    currentGen = startingGen
    i = 0
    if numGen < 1:
        return currentGen
    else:
        while i < numGen:
            prevGen = Generation(currentGen.getParentID())
            currentGen = prevGen
            i += 1
    return prevGen
    
    

class Generation:
    
    def __init__(self, ids_):
        self.ids_ = ids_
        self.size = len(ids_)
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
        parentArr = self.parentArr
        parentDict = {}
        for i in range(self.size):
            idxs = np.where(parentArr == i)[0]
            if len(idxs) > 0:
                children = (idxs / 2).astype(np.uint8)
#                print(i, children)
                childrenID = [self.ids_[child] for child in children]
#                print(childrenID)
            else:
                childrenID = [0]
            parentDict[i] = childrenID
            
        return parentDict
    
    def getParentID(self):
        parentDict = self.getParentDict()
        parentID = []
        for k in parentDict.keys():
            factors = parentDict[k]
            if len(factors) == 1:
                ID = factors[0]
            else:
                ID = 1
                for f in factors:
                    ID *= f
            parentID.append(ID)
        return np.array(parentID)
    
    def getParentFactors(self):
        parentDict = self.getParentDict()
        parentID = []
        for k in parentDict.keys():
            factors = parentDict[k]
            if len(factors) == 1:
                ID = factors[0]
            else:
                ID = factors
            parentID.append(ID)
        return np.array(parentID)        
            
            
    

def main():
    N = 6
    firstN = firstNPrimes(N)
    presentGen = Generation(firstN)
    
    print(presentGen.getParentFactors())
    
#    M = 3
#    backMGens = devolve(presentGen, M)
#    print(backMGens.getIDs())
    
#    ids = presentGeneration.getIDs()
#    print(ids)
#    print(presentGeneration.parentArr)
#    print(presentGeneration.getParentDict())
#    print(presentGeneration.getParentID())
    
main()





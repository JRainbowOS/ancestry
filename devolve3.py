# -*- coding: utf-8 -*-
"""
Created on Wed May  8 21:06:47 2019

@author: YS15101711
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:20:11 2019

@author: YS15101711
"""

from prime import isPrime, firstNPrimes
from prime import timing, creatDict
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
#            print(i)
#            print('progeny dict: {}'.format(self.progenyDict))
            alreadyRelated = progenyDict[i]
#            print("already related: {} \n **".format(alreadyRelated))
            idxs = np.where(parentArr == i)[0]
            if len(idxs) == 0:
#                print('here1')
                childrenID = [-1]
                alreadyRelated = [-1]
                newRelated = [-1]
#                print(childrenID)
            elif len(idxs) == 1:
#                print('here2')
                childrenID = (idxs / 2).astype(np.int32)
#                print(childrenID)
                newRelated = np.append(alreadyRelated, childrenID)
            else:
#                print('here3')
                childrenID = (idxs / 2).astype(np.int32)
#                print(childrenID)
                newRelated = np.append(alreadyRelated, childrenID)
#            print(alreadyRelated)
            
            # remove -1 <- tidy this
            if newRelated[-1] == -1:
                rewRelated = -1
            
            # de-dupe
            newRelated = list(set(newRelated))
#            print(newRelated)
            parentDict[i] = newRelated           
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
    N = 50
    initDict = creatDict(N)
    print(initDict)
    
    presentGen = Generation(initDict)
    M = 100
    backMGens = devolve(presentGen, M)
    print(backMGens.progenyDict)
    
main()





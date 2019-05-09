# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:03:34 2019

@author: YS15101711
"""

def devolve(parentDict):
    previousPopulation = Population(len(parentDict))
    return previousPopulation 

def livingDescendants():
    pass

class Population:
    import numpy as np
    
    SEED = 149
    SIZE = 10
    
    def __init__(self, genBeforePresent):
        self.size = Population.SIZE
        self.genBeforePresent = genBeforePresent
        self.__seed = Population.SEED
        self.parentDict = self.ParentDict()
        
    def getParentArr(self):
#        TODO: get seed working  
#        TODO: generate this from self.parentDict
        result_array = np.empty((2), int)
        for i in range(self.size):
            result = np.random.choice(self.size, 2, replace=False)
            result_array = np.append(result_array, result, axis=0)
        return result_array
    
    def ParentDict(self):
        result_dict = {}
        for i in range(self.size):
            result_dict[i] = np.random.choice(self.size, 2, replace=False)
        return result_dict
    
    def getParentDict(self):
        return self.ParentDict()
    
    def getChildrenDict(self):
        assert self.genBeforePresent > 0, 'no children from this generation'
        
        parentArr = self.getParentArr()
        childDict = {}
        for i in range(self.size):
            idxs = np.where(parentArr == i)
            if len(idxs[0]) > 0:
                children = (idxs[0] / 2).astype(np.uint8)
                childDict[i] = children
            else:
                childDict[i] = np.empty((1), int)

        return childDict                
        
    
def main():
    
    firstGen = Population(10)
    parents = firstGen.getParentDict()
    print('parent dictionary: {}'.format(parents))
    print('\n ***************** \n')
    children = firstGen.getChildrenDict()
    print('children dictionary: {}'.format(children))
    
main()







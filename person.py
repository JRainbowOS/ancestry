class Person:

    GENERATION_SIZE = 10

    def __init__(self, id_, genBeforePresent):
        self.id_ = id_
        self.genBeforePresent = genBeforePresent

    def getParents(self, id_):
        # ultimately this may be normally distributed about id
        '''
        Returns the id of Person's parents, assuming previous generation was the same size
        TODO: sensibly distribute this (not equally likely)
        '''
        import numpy as np
        parentsID = np.random.choice(Person.GENERATION_SIZE, 2, replace=False)
        return parentsID
    
    
    
def devolve(currentPopulation):
    '''
    Creates the previous generation out of the input generation
    '''
    pass

def getLivingDescendants(population):
    ''' 
    Returns the instances of living descendents of each member of an input generation
    '''
    pass

def backProp(child)
    
    
class Population:
    
    SIZE = 10
    
    def __init__(self, genBeforePresent):
        self.genBeforePresent = genBeforePresent
        self.size = Population.SIZE
        
    def getParents(self):
        import numpy as np
        
        parentDict = {}
        for i in range(self.size):
            parents = np.random.choice(self.size, 2, replace=False)
            parentDict[i] = parents
        return parentDict
              

def main():
#    presentGen = []
#    for i in range(10):
#        p = Person(i, 0)
#        presentGen.append(p)
#    for i, p in enumerate(presentGen):
#        print("parents of {} are: {}".format(i, p.getParents(i)))
        
    populations = []
    for i in range(5):
        p = Population(i)
        print("Generation {} parents: {}\n".format(i, p.getParents()))
        populations.append(p)
        
#    parents = currentPopulation.getParents()
#    print(parents)
        
        

main()




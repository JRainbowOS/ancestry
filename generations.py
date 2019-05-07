# -*- coding: utf-8 -*-
"""
Created on Tue May  7 19:21:09 2019

@author: YS15101711
"""


class Generation:
    
    def __init__(self, people):
        self.people = people
        
    def getGenerationCount(self):
        return self.people

def main():
    myGeneration = Generation(10)
    num = myGeneration.getGenerationCount()
    print(num)
    
main()


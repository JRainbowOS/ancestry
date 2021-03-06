# -*- coding: utf-8 -*-
"""
Created on Fri May 10 17:37:53 2019

@author: YS15101711
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import array

def cleanDict(outDict):
    keys = []
    values = []
    for k, v in outDict.items():
        if np.isin(-1, v):
            keys.append(k)
            values.append(0)
        else:
            keys.append(k)
            values.append(len(v))
    assert (len(keys) == len(values)), 'values and keys not the same length'
    return keys, values

def plotSurvivors(keys, values):
    fig, ax = plt.subplots(1,1, figsize=(4,4))
    ax.plot(keys, values)
    plt.xlabel('Members of bygone population')
    plt.ylabel('Number of surviving progeny')
    return None 

def barrenIdx(values):
    barren = 0
    for v in values:
        if v == 0:
            barren += 1
    result = barren / len(values)
    print('{:.1f}% of individuals have no surviving progeny'.format(100 * result))
    return result
    

#def familyTree(progenyDict):
    
        










## tests:
#eg1 = {0: array([0, 1, 4, 6, 7, 8, 9]), 1: array([-1]), 2: array([-1]), 3: array([-1]), 4: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 5: array([0, 2, 4, 5, 7, 8, 9]), 6: array([-1]), 7: array([-1]), 8: array([-1]), 9: array([-1])}
#eg2 = {0: array([0, 2, 3, 4, 5, 6, 7]), 1: array([-1]), 2: array([0, 1, 2, 3, 4, 6, 7, 9]), 3: array([1, 2, 3, 4, 6, 7, 8]), 4: array([0, 2, 3, 4, 5, 6, 8]), 5: array([-1]), 6: array([0, 2, 5, 6, 7, 8]), 7: array([0, 1, 2, 3, 4, 5, 7, 8, 9]), 8: array([-1]), 9: array([0, 4, 5, 6, 7, 8, 9])}
#eg3 = {0: array([ 0, 97, 66, 98, 36,  6, 72, 73, 42, 45, 47, 81, 51, 57, 90, 63]), 1: array([ 1,  2, 98, 70,  7, 73, 10, 44, 53, 55, 56]), 2: array([-1]), 3: array([ 3, 36, 11, 13, 52, 85, 88, 57, 58, 28, 29]), 4: array([64, 33,  4, 68, 14, 78, 30, 23, 89, 62]), 5: array([66,  5,  6, 37, 11, 79, 49, 51, 53, 87, 23, 88, 92]), 6: array([ 3, 67,  6, 16, 48, 84, 20, 22, 25, 58, 60, 95]), 7: array([96,  7, 41, 76, 45, 13, 47, 15, 44, 53, 55, 94, 58, 30]), 8: array([32, 34, 66, 69,  8,  9, 56, 26, 91, 28, 94]), 9: array([ 5,  9, 41, 13, 80, 22, 88, 58]), 10: array([32, 97, 98,  7, 10, 42, 76, 12, 45, 55, 57]), 11: array([-1]), 12: array([-1]), 13: array([-1]), 14: array([36, 37, 68, 41, 14, 19, 52, 84, 55, 23, 20, 58, 95, 31]), 15: array([-1]), 16: array([-1]), 17: array([-1]), 18: array([-1]), 19: array([64, 65, 34, 99, 36, 97, 58, 70, 15, 19, 90, 61]), 20: array([ 0,  5,  7, 71, 42, 16, 49, 20, 87, 57, 60, 61]), 21: array([-1]), 22: array([-1]), 23: array([-1]), 24: array([-1]), 25: array([-1]), 26: array([ 2, 11, 75, 76, 77, 80, 50, 20, 21, 52, 84, 26, 61]), 27: array([35, 71, 80, 18, 55, 23, 27, 92]), 28: array([-1]), 29: array([-1]), 30: array([33, 44, 77, 15, 80, 51, 52, 21, 88, 60, 30, 31]), 31: array([-1]), 32: array([-1]), 33: array([-1]), 34: array([-1]), 35: array([66, 35,  7, 14, 16, 81, 29, 51, 53, 24, 26, 93, 31]), 36: array([36,  4,  6, 39, 73, 44, 14, 51, 83, 85, 91]), 37: array([-1]), 38: array([67, 37, 38, 10, 43, 76, 16, 81, 18, 49, 52, 51, 25, 58, 27, 60, 95]), 39: array([65, 34,  3,  4, 37, 39, 48, 87, 91, 62]), 40: array([ 1, 70, 40, 42, 74, 82, 24, 91, 93]), 41: array([33,  2, 35, 38, 71,  8, 41,  9, 75, 40, 78, 19, 52, 85, 89, 91, 63]), 42: array([65, 38,  7, 10, 11, 42, 28, 21, 85, 23, 92]), 43: array([97, 99, 73, 42, 43, 45, 19, 54, 31, 95]), 44: array([97,  2, 35, 36, 70, 39,  8, 72, 44, 47, 90, 95]), 45: array([-1]), 46: array([-1]), 47: array([-1]), 48: array([-1]), 49: array([-1]), 50: array([-1]), 51: array([32, 65, 34,  3, 67, 11, 13, 81, 51, 54, 22, 88, 93, 62]), 52: array([96, 68, 71, 75, 77, 16, 49, 52, 21, 90]), 53: array([97,  1, 41, 44, 46, 14, 19, 20, 53]), 54: array([34, 98, 68,  4,  6, 35, 48, 81, 19, 61, 93, 54, 23, 86, 59, 29, 62]), 55: array([96, 97, 69, 70, 13, 77, 14, 47, 17, 85, 22, 55, 58, 27, 29]), 56: array([96, 98, 67,  5, 69, 10, 75, 20, 56, 57, 27, 31]), 57: array([32, 34,  6, 41, 73, 74, 45, 15, 49, 82, 55, 56, 57, 90, 60]), 58: array([64, 37, 69, 77, 52, 24, 58, 27, 29, 30, 63]), 59: array([-1]), 60: array([65, 33, 98,  3, 39, 74, 43, 46, 47, 48, 92, 82, 50, 87, 59, 60, 61]), 61: array([-1]), 62: array([-1]), 63: array([-1]), 64: array([64, 70, 38, 43, 16, 50, 87, 91]), 65: array([65, 98,  3, 68, 33, 70, 99, 42, 44, 13, 50, 89, 28, 62]), 66: array([-1]), 67: array([64, 33, 32, 67, 38, 75, 12, 80, 49, 82, 17, 94]), 68: array([-1]), 69: array([-1]), 70: array([33,  4, 70, 13, 46, 47, 48, 28, 17, 84, 85, 90, 60, 94]), 71: array([-1]), 72: array([96, 66,  4, 38, 71, 72, 77, 14, 54, 23, 88, 28, 61, 62]), 73: array([-1]), 74: array([-1]), 75: array([ 1, 35,  3, 75, 12, 76, 79, 84, 56, 57, 27]), 76: array([-1]), 77: array([-1]), 78: array([-1]), 79: array([-1]), 80: array([99, 70,  9, 42, 74, 14, 80, 20, 54, 22, 26, 93]), 81: array([-1]), 82: array([-1]), 83: array([-1]), 84: array([-1]), 85: array([-1]), 86: array([-1]), 87: array([34, 35, 98,  6,  8, 83, 21, 87, 89, 90, 92]), 88: array([-1]), 89: array([96, 32, 66, 67, 37, 69, 41, 10, 12, 18, 84, 89, 59]), 90: array([32, 70, 12, 76, 80, 81, 51, 24, 90, 59, 29]), 91: array([65, 68,  5, 41, 78, 79, 82, 18, 84, 55, 91, 93, 30]), 92: array([ 0, 38,  7, 74, 43, 76, 45, 13, 50, 86, 26, 59, 92, 29]), 93: array([-1]), 94: array([ 0, 96, 64, 40, 14, 15, 17, 18, 94]), 95: array([-1]), 96: array([96, 74, 46, 81, 82, 55, 26, 27, 62]), 97: array([-1]), 98: array([ 0, 98, 66,  4, 99, 42, 44, 78, 79, 51, 24, 62]), 99: array([-1])}
#
#keys, values = cleanDict(eg3)
#print(keys)
#print(values)
#
#plotSurvivors(keys, values)
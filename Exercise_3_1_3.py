# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:18:57 2018

@author: mzbor
"""
import random

proportionMasked=(2/3.0)

f = open('trialList.txt', 'w+')  #possibly use 'with open...'


def repetition(blocks, numberBeforeSwitch, numRepetitions):
    trials=[]
    for i in range(numRepetitions):
        for m in range(1, blocks+1):
            for n in range(numberBeforeSwitch):
                if n+1 <= proportionMasked * numberBeforeSwitch:
                    mask = 'masked'
                if n+1 > proportionMasked * numberBeforeSwitch:
                    mask = 'nonmasked'
                if n % 2 == 0:
                    hand='right'
                if n % 2 != 0:
                    hand='left'
                
                output = str(m),mask,hand 
                result = list(output) #turn trial into string to allow join with just comma
                resultSplit=','.join(result)
                trials.append(resultSplit+'\n')
    print type(trials)
    random.shuffle(trials)
    trials=''.join(map(str, trials))
    print type(trials)
    f.write(trials)
    print trials

    
    f.close()

            
                
repetition(5, 6, 1)
                
#              
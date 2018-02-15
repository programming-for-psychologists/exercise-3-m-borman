# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 20:51:00 2018

@author: mzbor
"""

import random

proportionMasked=(2/3.0)

f = open('trialList.txt', 'w+')  #possibly use 'with open...'


def repetition(blockNumber, trialsPerBlock, numRepetitions):
    trials=[]
    for i in range(numRepetitions):
        for m in range(1, blockNumber+1):
            block=[]
            for n in range(trialsPerBlock):
                if n+1 <= proportionMasked * trialsPerBlock:
                    mask = 'masked'
                if n+1 > proportionMasked * trialsPerBlock:
                    mask = 'nonmasked'
                if n % 2 == 0:
                    hand='right'
                if n % 2 != 0:
                    hand='left'
                
                output = str(m),mask,hand+'\n'
                result = list(output) #turn trial into string to allow join with just comma
                resultSplit=','.join(result)
                block.append(resultSplit)
            random.shuffle(block)
            block=''.join(map(str, block))
            trials.append(block)
            f.write(trials[-1])
        
        

    
    f.close()

            
                
repetition(5, 6, 1)
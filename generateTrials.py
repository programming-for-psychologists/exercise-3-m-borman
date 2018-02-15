# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:18:57 2018

@author: mzbor
"""
import random
proportionMasked=(2/3.0)


#with open('trialList.txt', 'w+') as f:
f = open('trialList.txt', 'w+')


def repetition(blocks, numberBeforeSwitch, numRepetitions):
#    if letters!=int:
#        lettersLen=len(letters)
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
                
                output = str(m),mask,hand+'\n'
                result = list(output)
                resultSplit=','.join(result)
#                    resultSplit=resultSplit.replace
#                for resultSplit in trials:
#                    trials.write(' '.join(str(resultSplit) for resultSplit in item))
                trials.append(resultSplit)

    random.shuffle(trials)
    trials=''.join(map(str, trials))
    f.write(trials)
    print trials
#    random.shuffle(trials)
#    f.write(trials)
                
#                        read_data = f.read()
    
    f.close()

            
                
repetition(5, 6, 1)
                
#              
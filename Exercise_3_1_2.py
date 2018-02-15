# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:18:57 2018

@author: mzbor
"""

proportionMasked=(2/3.0)



f = open('trialList.txt', 'w+')


def repetition(blocks, numberBeforeSwitch, numRepetitions):
#    if letters!=int:
#        lettersLen=len(letters)

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
                result = list(output)
                resultSplit=','.join(map(str, result))
#                print resultSplit
                f.write(resultSplit+'\n')
    f.close()

            
                
repetition(5, 6, 1)
                
                
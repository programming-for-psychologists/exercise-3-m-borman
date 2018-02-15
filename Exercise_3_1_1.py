

def repetition(letters, numberBeforeSwitch, numRepetitions):
    lettersLen=len(letters)
    for i in range(numRepetitions):
        for m in range(lettersLen):
            for n in range(numberBeforeSwitch):
                print letters[m]
        
repetition(['a', 'b', 'c'],3,3)

import random #we need to import random module

def computerguess(x):
    upper = x
    lower=1
    clue=" "
    while clue!="c":
        guessNumber = random.randint(lower,upper)#randit function generates random numbers between the given parameters
        clue=input(f'the{guessNumber}is too high (h) ,if too low (l),if correct (c)').lower()
        if clue=="h":
            upper=guessNumber-1
        elif clue=="l":
            lower=guessNumber+1
    print(f'yes {guessNumber} is correct ')

computerguess(10)#inside the bracket you need to enter your guess number
import random

while True:
    try:
        lvlrange = int(input('Level: '))
    
        if lvlrange > 0:
            break
    except:
        continue

x = random.choice(range(1,lvlrange))
# could also do x = random.randint(1,lvlrange)
while True:
    try:
        guessrange = int(input('Guess: '))
            
        if guessrange > 0:
            if guessrange == x:
                print('Just right!')
                break
            elif guessrange < x:
                print('Too small!')

            elif guessrange > x:
                print('Too large!')

    except:    
        continue
        
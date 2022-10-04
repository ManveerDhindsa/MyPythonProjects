import random

while True: 
    try:
        level = int(input('Level: '))
        if level in range(1,3):
            break
    except:
        pass

if level == 1:
    score = 0
    for i in range(1,5):
        while True:
            x = random.randint(0,9)
            y = random.randint(0,9)
            tries = 0
            try:
                while tries <=3:
                    answer = int(input(f'{x} + {y} = '))
                    if (x + y) == answer: 
                        
                        break
                    else:
                        print('EEE')
                        tries += 1  
                        pass

            except:
                print('EEE')
                tries +=1
                pass
            break
        if tries == 0:
            score += 1
        if tries == 3:
            print(f'{x} + {y} = {x+y}')
    
            
print('Score: ',score)        

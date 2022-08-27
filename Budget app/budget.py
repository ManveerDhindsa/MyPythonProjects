import re

class Budget:
    def __init__(self, deposit, withdraw):
        self.deposit = deposit
        self.withdraw = withdraw
        
    def food(self, foodbal):
        foodbal = foodbal + self.deposit - self.withdraw
        self.foodbal = foodbal
        return self.foodbal
        
    def clothing(self, clothingbal):
        clothingbal = clothingbal + self.deposit - self.withdraw
        self.clothingbal = clothingbal
        return self.clothingbal
        
    def entertainment(self, entbal):
        entbal = entbal + self.deposit - self.withdraw
        self.entbal = entbal
        return self.entbal
    
    def __str__(self):
        return self.foodbal, self.clothingbal, self.entbal
    
    
def main():
    foodbal, clothingbal, entbal = budget()
    while True:
        foodbal_, clothingbal_, entbal_ = transfer(foodbal, clothingbal, entbal)
        balance(foodbal_, clothingbal_, entbal_)
        foodbal = foodbal_
        clothingbal = clothingbal_
        entbal = entbal_

def budget():
    try: # add regex into these to strip everything outside of x.xx
        fbal = (input('Food Budget: ').strip())
        cbal = (input('Clothing Budget: ').strip())
        ebal = (input('Entertainment Budget: ').strip())
        
        matches = re.search(r"^\$?([0-9]+(?:\.[0-9]{2})?)(.*)?$", fbal)
        foodbal = float(matches.group(0))
        matches = re.search(r"^\$?([0-9]+(?:\.[0-9]{2})?)(.*)?$", cbal)
        clothingbal = float(matches.group(0))        
        matches = re.search(r"^\$?([0-9]+(?:\.[0-9]{2})?)(.*)?$", ebal)
        entbal = float(matches.group(0))
                
    except:
        raise ValueError('Enter a valid number')
    return foodbal, clothingbal, entbal

def balance(foodbal, clothingbal, entbal ):
    float_foodbal = "{:.2f}".format(foodbal)
    float_clothingbal = "{:.2f}".format(clothingbal)
    float_entbal = "{:.2f}".format(entbal)
    print('\nFood balance: ', float_foodbal)
    print('Clothing balance: ', float_clothingbal)
    print('Entertainment balance: ', float_entbal)
    print()

def transfer(foodbal, clothingbal, entbal):
    category = input('Input which cateogry you want to withdraw or transfer for (foodbal, clothingbal, entbal): \nIf you want to change balance between categories input "change": \nIf you do not want to transfer anything input "Done": ').lower().strip()
    
    if category == 'done':
        exit('Bye')
    
    if category == 'change':
        switch1 = input('Which category to transfer from (foodbal, clothingbal, entbal): ').lower().strip()
        switch2 = input('Which category to transfer to (foodbal, clothingbal, entbal): ').lower().strip()
        amount = (input('amount to move: ').strip())
        matches = re.search(r"^\$?([0-9]+(?:\.[0-9]{2})?)(.*)?$", amount)
        amount = float(matches.group(0))
        foodbal_, clothingbal_, entbal_= swap(switch1, switch2, amount, foodbal, clothingbal, entbal)
        return foodbal_, clothingbal_, entbal_
    else:
        action = input('"deposit" or "withdraw": ').lower().strip()
    
    if category == 'foodbal' or category == 'clothingbal' or category == 'entbal':
        try:
            amount = (input('amount to withdraw or transfer: ').strip())
            matches = re.search(r"^\$?([0-9]+(?:\.[0-9]{2})?)(.*)?$", amount)
            amount = float(matches.group(0))
        except ValueError:
            raise ValueError('Enter a valid number')
        
        if action == 'deposit':
            deposit = amount
            withdraw = 0
            foodbal, clothingbal, entbal = give(category, foodbal, clothingbal, entbal, deposit)
            return foodbal, clothingbal, entbal # this deposit code isn't working
        elif action == 'withdraw':
            withdraw = amount
            deposit = 0
            foodbal, clothingbal, entbal = take(category, foodbal, clothingbal, entbal, withdraw)
            return foodbal, clothingbal, entbal
        else:
            raise ValueError('not a valid action')

def give(category, foodbal, clothingbal, entbal, depo):
    budget = Budget(depo, 0)
    if category == 'foodbal':
        foodball = budget.food(foodbal)
        return foodball, clothingbal, entbal
    elif category == 'clothingbal':
        clothingball = budget.clothing(clothingbal)
        return foodbal, clothingball, entbal
    elif category == 'entbal':
        entball = budget.entertainment(entbal)
        return foodbal, clothingbal, entball
    else:
        raise ValueError('Not a valid category')

def take(category, foodbal, clothingbal, entbal, wdraw):
    budget = Budget(0, wdraw)
    if category == 'foodbal':
        foodbal = budget.food(foodbal)
        return foodbal, clothingbal, entbal
    elif category == 'clothingbal':
        clothingbal = budget.clothing(clothingbal)
        return foodbal, clothingbal, entbal
    elif category == 'entbal':
        entbal = budget.entertainment(entbal)
        return foodbal, clothingbal, entbal
    else:
        raise ValueError('Not a valid category')

def swap(switch1, switch2, amount, foodbal, clothingbal, entbal):
    budget = Budget(0, amount)
    if switch1 == 'foodbal':
        foodbal = budget.food(foodbal)
    elif switch1 == 'clothingbal':
        clothingbal = budget.clothing(clothingbal)
    elif switch1 == 'entbal':
        entbal = budget.entertainment(entbal)
    
    budget = Budget(amount, 0)
    if switch2 == 'foodbal':
        foodbal = budget.food(foodbal)
    elif switch2 == 'clothingbal':
        clothingbal = budget.clothing(clothingbal)
    elif switch2 == 'entbal':
        entbal = budget.entertainment(entbal)
    else:    
        raise ValueError('Please enter valid category to take from and give to')
    return foodbal, clothingbal, entbal

if __name__ == '__main__':
    main()
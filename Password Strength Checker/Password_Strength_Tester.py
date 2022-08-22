#tests the strength of a password based on number of characters, upper case and lower case letters, numbers and special characters using Regex

import re
import sys

def main():
    systest()
    if matches := re.search(r'^\S+$', sys.argv[1]):
        lowerlen, upperlen, minuslower, minusupper = letters()
        numslen, minusnums = numbers()
        specslen, minusspecs = specs()
    else:
        raise ValueError("password contains spaces or invalid characters")

    strength(lowerlen, upperlen, numslen, specslen, minuslower, minusupper, minusnums, minusspecs)

def systest():
    if not len(sys.argv) == 2:
        sys.exit("Please enter 1 password")
        

def letters():
    lower = re.split(r'[^a-z]+', sys.argv[1])
    upper = re.split(r'[^A-Z]+', sys.argv[1])    
    lowers = ''.join(lower)
    uppers = ''.join(upper)
    lowerlen = len(lowers)
    upperlen = len(uppers)
    minuslower = len(set(lowers))
    minusupper = len(set(uppers))
    return lowerlen, upperlen, minuslower, minusupper


def numbers():
    num = re.split(r'[^0-9]+', sys.argv[1])   
    nums = ''.join(num)
    numslen = len(nums)
    minusnums = len(set(nums))
    return numslen, minusnums


def specs():
    spec = re.split(r'[^\$\+\,\:\;\=\?\@\#\|\'\<\>\.\^\*\(\)\%\!\-]+', sys.argv[1])   
    specs = ''.join(spec)
    specslen = len(specs)
    minusspecs = len(set(specs))
    return specslen, minusspecs


def strength(lowerlen, upperlen, numslen, specslen, minuslower, minusupper, minusnums, minusspecs):
    lenss = [lowerlen, upperlen, numslen, specslen]
    i = 0
    # determines how many of the requirements are included in the password
    for _ in lenss:
        if _ > 0:
            i +=1
    strength1  = i * 2.5
    total_len = lowerlen + upperlen + numslen + specslen
    strength2 = total_len * 0.5
    
    if minuslower == 1 or minusupper == 1 or minusnums == 1 or minusspecs == 1:
        total_strength = strength1 + strength2 - 3
    else: 
        total_strength = strength1 + strength2
        
    if 0 <= total_strength < 5:
        print('Strength: Weak Password  [███.........]')
    elif 5 <= total_strength < 10:
        print('Strength: Ok Password  [██████......]')
    elif 10 <= total_strength < 15:
        print('Strength: Good Password  [█████████...]')
    else:
        print('Strength: Excellent Password  [████████████]')

if __name__ == "__main__":
    main()
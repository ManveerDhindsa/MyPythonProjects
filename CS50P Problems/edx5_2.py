def main():
    while True:
        greeting = input('Input: ')
        if greeting == '':
            continue
        else:
            break

    
    print(value(greeting))

def value(x):
    x = x.strip().lower()
    hello = 'hello'

    if hello in x:
        return '$0'
    elif x[0] == 'h':
        return '$20'
    else:
        return '$100'



if __name__ == "__main__":
    main()
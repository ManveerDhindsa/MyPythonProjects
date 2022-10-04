def main():
    fraction = input('Fraction: ')
    convert(fraction)
    gauge(convert(fraction))

def convert(fraction):
    while True:
        try:
            x,y = fraction.split('/')
            x = int(x)
            y = int(y)
            f = x/y
            if 0<= f <= 1:
                return f
            else:
                fraction = input('Fraction: ')
                pass

        except (ValueError ,ZeroDivisionError):
            raise #prompts the user for another input

def gauge(percentage):
    
    percentage = round((percentage)*(100))
    
    if 99 <= percentage <= 100:
        print('F')
    elif 0 <= percentage <= 1:
        print('E')
    else:
        print(f'{percentage}%')

if __name__ == "__main__":
    main()
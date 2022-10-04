from validator_collection import validators, errors

def main():
    if emailcheck(input("What's your email address? ")):
        print('Valid')

def emailcheck(value):
    try:
        email_address = validators.email(value, allow_empty = False)
        return email_address
    except ValueError as error:
        print('Invalid')

if __name__ == '__main__':
    main()
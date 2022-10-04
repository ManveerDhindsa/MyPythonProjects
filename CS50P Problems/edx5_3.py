def main():
    plate = input("Plate: ")
    if is_valid(plate) == True:
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if s[0] == '0':
        return False

    if len(s)>6 or len(s) < 2:
        return False

    for char in s:
        if char in ['.', '!', '?',' ']:
            return False

    if not s[0:2].isalpha() == True:
        return False

    for x in range(len(s)):
        if s[x].isdigit():
            if not s[x:].isdigit():
                return False

    return True


if __name__ == '__main__':
    main()
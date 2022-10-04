import re

def main():
    print(convert(input("Hours: ")))
    
def convert(s):
    match = re.search(r'^([0-9][0-2]*)(:[0-5][0-9])* (AM|PM) to ([0-9][0-2]*)(:[0-5][0-9])* (AM|PM)$', s)

    if match:
        matches = match.groups()
        if int(matches[0]) > 12 or int(matches[3]) > 12:
            raise ValueError("Invalid hours")
        first = newformat(matches[0], matches[1], matches[2])
        second = newformat(matches[3], matches[4], matches[5])
        return first + ' to ' + second
    else:
        raise ValueError("Invalid hours")
    
def newformat(prehour, minutes, ampm):
    if minutes is None:
        minutes = ':00'
    if ampm == 'AM':
        if prehour == '12':
            hour = 0
        else:
            hour = int(prehour)
    if ampm == 'PM':
        if prehour == '12':
            hour = int(prehour)
        else:
            hour = 12 + int(prehour)
    time = (f"{hour:02}{minutes}")
    return time

if __name__ == "__main__":
    main()
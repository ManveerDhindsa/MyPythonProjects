import re
import sys


def main():
    answer = input("IPv4 Address: ").strip()
    print(validate(answer))

def validate(ip):

    if match := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        ips = ip.split('.')    
        for x in ips:
            if int(x) < 0 or int(x) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()

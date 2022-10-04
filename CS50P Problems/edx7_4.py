# def main():
#     print(int(count(input("Text: "))))

# def count(s):
#     words = s.split(' ')
#     count = 0
#     for word in words:
#         if word[0:2] == 'um':
#             count += 1
#     return count
            
# if __name__ == "__main__":
#     main()

import re

def main():
    print(count(input("Text: ")))

def count(s):
    match = re.findall(r'\bum\W*', s, re.IGNORECASE)    
    return len(match)

if __name__ == "__main__":
    main()

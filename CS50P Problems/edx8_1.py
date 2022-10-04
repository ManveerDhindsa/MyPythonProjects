# from datetime import date
# import re
# import sys
# import inflect

# p = inflect.engine()

# class Delta:
#     def __init__(self,birth, today):
#         self.birth = birth
#         self.today = today
        
#     def __sub__(self):
#         pre = date.fromisoformat(self.birth)
#         post = date.fromisoformat(self.today)
#         days = pre - post
#         minutes = int(days) * 1440
#         return minutes.days
    
#     def __str__(self):
#         return f"{minutes}"


# def main():
#         birth = get_birth()
#         today = get_today()
#         delta = Delta(birth, today)
#         words = p.number_to_words(delta, wantlist=True)
#         final = words.replace('and ', '')
#         print(final, 'minutes')
    
# def get_birth():    
#     b = input('Date of Birth: ')
#     try:
#         match = re.search(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', b)
#         return b
#     except ValueError:
#         sys.exit("Invalid Date")
    
    
# def get_today(): 
#     t = date.today()
#     return t



# if __name__ == '__main__':
#     main()

from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
        b = input('Date of Birth: ')
        try:
            year, month, day= get_birth(b)
        except ValueError:
            sys.exit("Invalid Date")
        today = get_today()
        pre = date(int(year), int(month), int(day))
        diff = today - pre
        minutes = diff.days * 60
        words = p.number_to_words(minutes, andword='')
        
        print(words.capitalize(), 'minutes')
    
def get_birth(b):    
    if re.search(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', b):
        year,month,day = b.split('-')
        return year, month, day

    
    
def get_today(): 
    t = date.today()
    return t



if __name__ == '__main__':
    main()
import inflect
p = inflect.engine()

list1 = []
while True:
    try:
        name = input('Name: ')
        list1.append(name)
    except EOFError:
        break

#this code works but there is a package that has the same stuff built in already
# print('Adieu, adieu, to', end='')

# if len(list1) == 1:
#     print(' ', list1)

# elif len(list1) == 2:
#     print(' ', *list1, sep=' and ')
    
# else:
#     print(', ', end='')
#     print(*list1[0:-1], sep=',', end='')
#     print(', and', list1[-1])

output = p.join(list1)
print('Adieu, adieu, to ' + output)
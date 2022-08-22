from csv import writer
from csv import reader

def main():
    with open('new_student.csv', 'r') as rfile, open('newstudent.csv', 'w', newline='') as wfile:
        csv_writer = writer(wfile)
        csv_reader = reader(rfile)
        for row in csv_reader: 
            row.append(traits(row[1]))
            row.append(grade(row[2]))
            csv_writer.writerow(row)

def traits(trait):
    #assigns house to each person based on characteristics
    
    gryffindor = ['courage','loyalty','adventure']
    hufflepuff = ['dedication', 'patience','honesty']
    ravenclaw = ['wisdom', 'creativity', 'perfectionism']
    slytherin = ['ambition', 'competitive', 'leadership']     
    
    if trait in gryffindor:
        return 'gryffindor'
    elif trait in hufflepuff:
        return 'hufflepuff'
    elif trait in slytherin:
        return 'slytherin'
    elif trait in ravenclaw:
        return 'ravenclaw'
    else:
        return 'house'

def grade(year):
    #assigns each person to a specific grade depending on age
    try:
        age = 2022 - int(year)
        grade = age - 5
        return f'grade:{grade}'
    except:
        return 'grade'


if __name__ == "__main__":
    main()
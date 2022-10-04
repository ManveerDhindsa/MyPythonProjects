import sys
import csv


def main():
    check_correct_args()
    data = []
    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row) 
    except:
        sys.exit("file not found")

    output = []
    for row in data:
        house = select_house(row['characteristic'])
        grade = select_grade(row['birthdate'])
        output.append({'name': row['name'], 'house' : house , 'grade' : grade})
    
    with open(sys.argv[2], 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames = ['name', 'house', 'grade'])
        writer.writerow({'name': 'name', 'house': 'house', 'grade': 'grade'})
        for row in output:
            writer.writerow({'name': row['name'], 'house': row['house'], 'grade': row['grade']})

def check_correct_args():
    if len(sys.argv) < 3:
        sys.exit('too few arguments')
    if len(sys.argv) > 3:
        sys.exit('too many arguments')
    
    # if sys.argv[1].endswith('.csv') or sys.argv[2].endswith('csv'):
    #     pass
    # else:
    #     sys.exit('not a csv file')
    
    if '.csv' not in sys.argv[1] or '.csv' not in sys.argv[2]:
        sys.exit('not a csv file')
        

def select_house(char):
    gryffindor = ['courage','loyalty','adventure']
    hufflepuff = ['dedication', 'patience','honesty']
    ravenclaw = ['wisdom', 'creativity', 'perfectionism']
    slytherin = ['ambition', 'competitive', 'leadership']     
    
    if char in gryffindor:
        return 'gryffindor'
    elif char in hufflepuff:
        return 'hufflepuff'
    elif char in slytherin:
        return 'slytherin'
    elif char in ravenclaw:
        return 'ravenclaw'
    else:
        return 'no house'

def select_grade(year):
    age = 2022 - int(year)
    grade = age - 5
    return 'grade:' + str(grade)


if __name__ == "__main__":
    main()
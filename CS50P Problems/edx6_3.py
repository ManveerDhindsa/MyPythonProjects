import sys
import csv

def main():
    check_command_line_args()
    list1 = [] 
    try:
        with open(sys.argv[1], 'r') as csvfile1:
            lines = csv.DictReader(csvfile1)
            for line in lines:
                last, first = line['name'].rstrip().split(",")
                list1.append({'first': first, 'last': last, 'house': line['house']})
    except FileNotFoundError:
        sys.exit('File does not exist')
    
    with open(sys.argv[2], 'w') as csvfile2:
        csvwriter = csv.DictWriter(csvfile2, fieldnames = ['first', 'last', 'house'])
        csvwriter.writeheader()
        for row in list1:
            csvwriter.writerow({'first': row['first'], 'last': row['last'], 'house': row['house']})        
            if any(field.strip() for field in row):
                csvwriter.writerow(row)
            if row == '':
                continue
            
def check_command_line_args():
    if len(sys.argv) > 3:
        sys.exit('Too many command line arguments')
    if len(sys.argv) < 3:
        sys.exit('Not enough command line arguments')
    if sys.argv[1].endswith('.csv') == False:
        sys.exit('Not a csv file')
    
if __name__ == '__main__':
    main()
import sys
import csv
from tabulate import tabulate

def main():
    check_command_line_args()
    try:
        with open(sys.argv[1], 'r') as csvfile:
            lines = csv.reader(csvfile)
            table = []
            for row in lines:
                table.append(row)
                
    except FileNotFoundError:
        sys.exit('File does not exist')
    
    print(tabulate(table[1:], table[0], tablefmt="grid"))
    
    
def check_command_line_args():
    if len(sys.argv) > 2:
        sys.exit('Too many command line arguments')
    if len(sys.argv) < 2:
        sys.exit('Not enough command line arguments')
    if sys.argv[1].endswith('.csv') == False:
        sys.exit('Not a csv file')
    
if __name__ == '__main__':
    main()
import sys

if len(sys.argv) > 2:
    sys.exit('Too many command line arguments')
if len(sys.argv) < 2:
    sys.exit('Not enough command line arguments')
if '.py' in sys.argv[1]:
    try:
        with open(sys.argv[1], 'r') as file:
            lines = len(file.readlines())
            
            for line in file:
                line = line.lstrip()
                if len(line) == 0:
                    lines -= 1
                if line.startswith('#'):
                    lines -= 1
            
            print(lines)
    
    except FileNotFoundError:
        sys.exit('File does not exist')
        
else:
    sys.exit('Not a python file')
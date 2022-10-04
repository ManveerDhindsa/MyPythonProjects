from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

if sys.argv[1] == '-f' and sys.argv[2] in figlet.getFonts():
    answer = input('input: ')
    figlet.getFonts()
else:
    print('Invalid font')
    sys.exit(1)
    
if len(sys.argv) == 3:
    figlet.setFont(font= sys.argv[2])
    print(figlet.renderText(answer))

elif len(sys.argv) == 1:
    figlet.setFont(font = random.choice(figlet.getFonts()))
    print(figlet.renderText(answer))

elif len(sys.argv) == 2:
    print('Invalid usage')
    sys.exit(1)

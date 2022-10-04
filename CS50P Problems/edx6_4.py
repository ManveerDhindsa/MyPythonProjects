import sys
import PIL
from PIL import Image

def main():
    check_command_line_args()
    overlay = PIL.Image.open('shirt.png')
   
    try:
        im1 = PIL.Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit('File does not exist')
    
    im2 = PIL.ImageOps.fit(im1, overlay.size, method=0, bleed=0.0, centering=(0.5, 0.5)) 
    im2.paste(overlay, overlay)
    im2.save(sys.argv[2])
            
def check_command_line_args():
    if len(sys.argv) > 3:
        sys.exit('Too many command line arguments')
    if len(sys.argv) < 3:
        sys.exit('Not enough command line arguments')
    if sys.argv[1].endswith('.png') and sys.argv[1].endswith('.jpg') and sys.argv[1].endswith('.jpeg') == True:
        sys.exit('Not a image file')
    if sys.argv[2].endswith('.png') and sys.argv[2].endswith('.jpg') and sys.argv[2].endswith('.jpeg') == True:
        sys.exit('Not a image file')
    
if __name__ == '__main__':
    main()
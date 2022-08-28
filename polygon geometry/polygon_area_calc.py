import sys
import math

class Triangle:
    def area(self, width, height):
        area_ = 0.5 *(int(width) * int(height))
        return area_
    def perimeter(self, x, y, z):
        perimeter_ = int(x) + int(y) + int(z)
        return perimeter_

class Square:
    def __init__(self, length):
        self.length = int(length)
    
    def area(self):
        area_ = self.length**2
        return area_
        
    def perimeter(self):
        perimeter_ = self.length*4
        return perimeter_

class Rectangle:
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)
        
    def area(self):
        area_ = self.width * self.height
        return area_
        
    def perimeter(self):
        perimeter_ = (self.width * 2) + (self.height * 2)

class Pentagon:
    def __init__(self, length):
        self.length = int(length)
        
    def area(self):
        area_ = (0.25 * self.length**2) * (math.sqrt(5 + 2 * math.sqrt(5)))
        return area_
        
    def perimeter(self):
        perimeter_ = self.length * 5
        return perimeter_

def main():
    inputtest()
    if sys.argv[2].lower() == 'area':
        if sys.argv[1].lower() == 'triangle':
            shape = Triangle()
            print(a(shape))
        if sys.argv[1].lower() == 'square':
            shape = Square(sys.argv[3])
            print(a(shape))
        if sys.argv[1].lower() == 'rectangle':
            shape = Rectangle(sys.argv[3], sys.argv[4])
            print(a(shape))
        if sys.argv[1].lower() == 'pentagon':
            shape = Pentagon(sys.argv[3])
            print(a(shape))       
        
    elif sys.argv[2].lower() == 'perimeter':
        if sys.argv[1].lower() == 'triangle':
            shape = Triangle()
            print(p(shape))
        if sys.argv[1].lower() == 'square':
            shape = Square(sys.argv[3])
            print(p(shape))
        if sys.argv[1].lower() == 'rectangle':
            shape = Rectangle(sys.argv[3], sys.argv[4])
            print(p(shape))
        if sys.argv[1].lower() == 'pentagon':
            shape = Pentagon(sys.argv[3])
            print(p(shape))
    else:
        sys.exit('Enter area or perimeter as the 3rd command prompt')

def a(shape):
    if sys.argv[2].lower() == 'square' or sys.argv[2].lower() == 'rectangle' or sys.argv[2].lower() == 'pentagon':
        _ = shape.area()
        return _
    else: 
        _ = shape.area(sys.argv[3], sys.argv[4])
        return _
    
def p(shape):
    if sys.argv[2].lower() == 'square' or sys.argv[2].lower() == 'rectangle' or sys.argv[2].lower() == 'pentagon':
        _ = shape.perimeter()
        return _
    else: 
        _ = shape.perimeter(sys.argv[3], sys.argv[4], sys.argv[5])
        return _   

def inputtest():    
    if sys.argv[1].lower() == 'triangle':
        if len(sys.argv) == 5 or len(sys.argv) == 6:
            pass
        else:
            sys.exit('Not correct amount of command line arguments')
            
    elif sys.argv[1].lower() == 'square':
        if len(sys.argv) == 4:
            pass
        else:
            sys.exit('Not correct amount of command line arguments')
    elif sys.argv[1].lower() == 'rectangle':
        if len(sys.argv) == 5:
            pass
        else:
            sys.exit('Not correct amount of command line arguments')
    elif sys.argv[1].lower() == 'pentagon':
        if len(sys.argv) == 4:
            pass
        else:
            sys.exit('Not correct amount of command line arguments')
    else:
        sys.exit('Enter a valid shape (triangle, square, rectangle, pentagon')
        
if __name__ == '__main__':
    main()
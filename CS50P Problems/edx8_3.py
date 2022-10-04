from fpdf import FPDF

class PDF():

    def __init__(self, name):
        self.shirt = FPDF()
        self.shirt.add_page()        

        self.shirt.set_font('helvetica', 'B', 50)
        self.shirt.cell(0,60,"CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")
        
        self.shirt.image("shirtificate.png", w=self.shirt.epw)
                
        self.shirt.set_font('helvetica', 'B', 30)
        self.shirt.set_text_color(255,255,255)
        self.shirt.text(x=44,y=140, txt= f'{name} took CS50')
        
    def save(self,name):    
        self.shirt.output(name)


name = input("Name: ")
pdf = PDF(name)

pdf.save("shirt.pdf")
from fpdf import FPDF
import pandas as pd

                                                #A4 ->297
pdf = FPDF(orientation="P", unit="mm", format = "A4")
pdf.set_auto_page_break(auto = False, margin = 0)
# p-> poterate , L->  landscape

df = pd.read_csv("topics.csv")

for index , row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family = "Times", style = "B", size = 24)
    pdf.set_text_color(100,100,100) #RGB
    pdf.cell(w=0, h=12, txt=row["Topic"], align = "L", ln = 1, border = 0)
    
    #lining in the pdf page
    for y in range(20,298,10):
        pdf.line(10,y,200,y)
        
    
    # set the footer for the text page
    pdf.ln(265)
    pdf.set_font(family="Times", style = "I", size = 8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=10, txt = row["Topic"], align = "R")
    
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        
        #set the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style = "I", size = 8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0,h=10, txt = row["Topic"], align = "R")
        
        #lining in the pdf page
        for y in range(20,298,10):
            pdf.line(10,y,200,y)

pdf.output("output.pdf")
""" 
line method -> (x1,y1,x1,y2) --> (initialX,initialY, finalX, finalY)
cell -> method
w = width 
h = height
txt = text to be written
align = alignment of the text
ln = next line for the cell
border = border of the line
"""
import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path #--> for the paths and methods associated with itx


filePaths = glob.glob("invoices/*.xlsx")

"""
We have loaded aur excel file in our datafram
now our motive should be to convert these excel dataframe
into the pdf files
"""
for filepath in filePaths: 
    
    # creating a pdf
    pdf = FPDF(orientation = "p", unit = "mm", format = "A4")
    
    # adding page to the pdf
    pdf.add_page()
    """ 
    Now we have to start adding content to the pdf
    in order to add the content to the pdf we first have
    the sketch of the invoice you want to create
    Method-1 --> using pen and paper
    Method-2 --> using figma
    Method-3 --> using any predefined templates
    """
    
    #extracting the invoice no. and date from the  file path
    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]
    date = filename.split("-")[1]
    """
    filename = Path(filepath).stem
    Method-1
        invoice_nr = filename.split("-")[0]
        date = filename.split("-")[1]
    Method-2
        invoice_nr, date = filename.split("-")
        --> list has 2 menbers , first will be assigned to
            the first variable and second will be 
            assigned to the second variable
    """
    
    #cell for the invoice number
    pdf.set_font(family = "Times", size = 16, style = "B")
    pdf.cell(w=50, h = 8, txt = f"Invoice nr. {invoice_nr}", ln = 1)
    
    # cell for the date 
    pdf.set_font(family = "Times", size = 16, style = "B")
    pdf.cell(w=50, h = 8, txt = f"Date : {date}", ln=1)
    
    # creating a dataframe
    df = pd.read_excel(filepath, sheet_name = "Sheet 1")
    
    # add a header
    columns = df.columns
    columns = [item.replace("_" , " ").title() for item in columns]
    pdf.set_font(family = "Times", size = 10, style = "B")
    pdf.set_text_color(80,80,80)
    pdf.cell(w=30, h=8, txt = columns[0], border = 1)
    pdf.cell(w=70, h=8, txt = columns[1], border = 1)
    pdf.cell(w=30, h=8, txt = columns[2], border = 1)
    pdf.cell(w=30, h=8, txt = columns[3], border = 1)
    pdf.cell(w=30, h=8, txt = columns[4], border = 1, ln=1)

    # now we have to iterate over the dataFrame
    # add rows to the table
    for index , row in df.iterrows():
        pdf.set_font(family = "Times", size = 10)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30, h=8, txt = str(row["product_id"]), border = 1)
        pdf.cell(w=70, h=8, txt = str(row["product_name"]), border = 1)
        pdf.cell(w=30, h=8, txt = str(row["amount_purchased"]), border = 1)
        pdf.cell(w=30, h=8, txt = str(row["price_per_unit"]), border = 1)
        pdf.cell(w=30, h=8, txt = str(row["total_price"]), border = 1, ln=1)
        

    #calcuating the total sum
    total_sum = df["total_price"].sum()
    pdf.set_font(family = "Times", size = 10)
    pdf.set_text_color(80,80,80)
    pdf.cell(w=30, h=8, txt = "", border = 1)
    pdf.cell(w=70, h=8, txt = "", border = 1)
    pdf.cell(w=30, h=8, txt = "", border = 1)
    pdf.cell(w=30, h=8, txt = "", border = 1)
    pdf.cell(w=30, h=8, txt = str(total_sum), border = 1, ln=1)
    
    # Add total sum sentence
    pdf.set_font(family = "Times", size = 10)
    pdf.cell(w=0, h=8, txt = f"the total price : {total_sum}", ln=1)
    
    # add company name and logo
    pdf.set_font(family = "Times", size = 10, style = "B")
    pdf.cell(w=40, h=8, txt = f"Gaurav Kumar Maurya")
    pdf.image("gkm.png", w = 10)
    
    
    # now its time to save the pdf
    pdf.output(f"PDFs/{filename}.pdf")
    

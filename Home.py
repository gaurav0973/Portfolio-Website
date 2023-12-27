import streamlit as st
import pandas  # for reading csv file

st.set_page_config(layout = "wide")


col1 , col2 = st.columns(2)

with col1:
    st.image("images/photo.png")


with col2:
    st.title("Gaurav Kumar Maurya")
    content = """ Hello, I'm Gaurav Kumar Maurya, currently pursuing 
    my Bachelor of Technology (B.Tech) in Information Technology from
    Jaypee University. With a passion for technology and a keen 
    interest in exploring the ever-evolving world of IT, I am 
    dedicated to acquiring knowledge and skills that will contribute
    to my academic and professional growth. Eager to embrace 
    challenges and always open to learning, I am on a journey to 
    make a positive impact in the field of Information Technology.
    """
    #st.write(content)
    st.info(content)
    
#Method
# col3 = st.columns(1)
# col3[0].write("""Below you can find some of the apps I have
#              built in Python. Feel free to contact me!""")
#Alternative approach
content2 = """Below you can find some of the apps I have
             built in Python. Feel free to contact me!"""
st.write(content2)

col3 , empty_col,  col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep = ";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row[0]) # title
        st.write(row[1])  # description
        st.image("images/" + row[3]) # images
        st.write(f"[Source code]({row[2]})")
        
with col4:
    for index, row in df[10:].iterrows():
        st.header(row[0]) 
        st.write(row[1])
        st.image("images/" + row[3])
        st.write(f"[Source code]({row[2]})")
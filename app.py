import streamlit as st

# Page title
st.title("TextbookIQ: PDF Question Answering System")

# File uploader
uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files:
    st.write("PDF files uploaded successfully.")
    
# Query input
query = st.text_input("Enter your question:")

if query:
    st.write(f"Your question is: {query}")

st.write("This is a simple Streamlit app. More functionality will be added soon.")

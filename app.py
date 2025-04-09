import streamlit as st
from dotenv import load_dotenv
load_dotenv()  # Loads environment variables from .env (for your API key)

# Import our function to analyze financial data from analyzer.py
from analyzer import analyze_financial_data
# Import the helper function to extract text from PDFs
from utils import extract_text_from_pdf, parse_csv

st.set_page_config(page_title="Smart Budget AI", layout="centered")
st.title("💡 Smart Budgeting Assistant")

st.write("Upload a PDF or CSV file containing your budget or expense data.")

# File Uploader: Accepts PDF or CSV files
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "csv"])

if uploaded_file:
    # Decide how to extract text based on file type
    file_type = uploaded_file.name.split('.')[-1].lower()
    if file_type == "pdf":
        # Extract text from PDF using our helper function in utils.py
        text = extract_text_from_pdf(uploaded_file)
    elif file_type == "csv":
        # Extract text from CSV (for a CSV, we might just read it as text)
        text = parse_csv(uploaded_file)
    else:
        text = uploaded_file.read().decode("utf-8")
    
    st.text_area("Extracted File Content", text, height=300)

    # Analyze the text using your AI function and display suggestions
    with st.spinner("Analyzing your budget..."):
        suggestions = analyze_financial_data(text)
    st.write("### Suggestions:")
    st.markdown(suggestions)

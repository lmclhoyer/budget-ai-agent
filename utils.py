import pdfplumber
import pandas as pd

def extract_text_from_pdf(file):
    # Reads a PDF file and extracts text from each page
    all_text = ""
    try:
        # Open PDF using pdfplumber
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    all_text += page_text + "\n"
        return all_text
    except Exception as e:
        return f"Error extracting PDF text: {e}"

def parse_csv(file):
    # Read CSV as a Pandas DataFrame and then convert to a string
    try:
        df = pd.read_csv(file)
        return df.to_string(index=False)
    except Exception as e:
        return f"Error parsing CSV: {e}"

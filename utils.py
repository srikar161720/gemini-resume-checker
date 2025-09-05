# utils.py

import streamlit as st
import fitz  # PyMuPDF


def get_file_text(uploaded_file):
    """
    Extracts text from an uploaded file (PDF or TXT).

    Args:
        uploaded_file: An uploaded file object from Streamlit's file_uploader.

    Returns:
        A string containing the extracted text, or None if the file type is unsupported.
    """
    text = ""
    file_name = uploaded_file.name

    if file_name.endswith('.txt'):
        # For .txt files, read the file as a string
        text = uploaded_file.getvalue().decode("utf-8")
    elif file_name.endswith('.pdf'):
        try:
            # For .pdf files, use PyMuPDF to extract text
            with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
                for page in doc:
                    text += page.get_text()
        except Exception as e:
            st.error(f"Error reading PDF file: {e}")
            return None
    else:
        st.error("Unsupported file type. Please upload a .txt or .pdf file.")
        return None

    return text
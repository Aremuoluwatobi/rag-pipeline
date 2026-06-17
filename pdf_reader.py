import pdfplumber
import re
import os
from docx import Document


def clean_text(text):

    text = text.replace("\n", " ")

    text = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def extract_pdf_text(file_path):

    pdf_text = ""

    try:

        with pdfplumber.open(file_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    pdf_text = clean_text(pdf_text)
                    pdf_text += page_text + " "

        return pdf_text

    except Exception as e:
        print(f"PDFPlumber Error: {e}")
        return ""


def extract_docx_text(file_path):

    doc_text = ""

    try:

        document = Document(file_path)

        for paragraph in document.paragraphs:

            if paragraph.text:

                doc_text += paragraph.text + " "

        doc_text = clean_text(doc_text)
        return doc_text

    except Exception as e:
        print(f"DOCX Error: {e}")
        return None


def extract_all_text(file_path):

    try:
        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".pdf":
            return extract_pdf_text(file_path)

        elif extension == ".docx":
            return extract_docx_text(file_path)

    except Exception as e:
        print(f"Unsupported file type: {e}")
        return None

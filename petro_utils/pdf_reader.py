from pypdf import PdfReader

def extract_text(uploaded_pdf):
    reader = PdfReader(uploaded_pdf)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text
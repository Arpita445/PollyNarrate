from pypdf import PdfReader
from docx import Document


def extract_text(file):

    if file.name.endswith(".pdf"):

        reader = PdfReader(file)

        text = ""

        for page in reader.pages:
            text += page.extract_text()

        return text


    elif file.name.endswith(".docx"):

        doc = Document(file)

        text = ""

        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"

        return text


    elif file.name.endswith(".txt"):

        return file.read().decode("utf-8")


    else:
        return "Unsupported file format"

from docx import Document

def extract_text_from_file(file_storage):
    filename = file_storage.filename
    ext = filename.rsplit(".", 1)[-1].lower()

    if ext == "txt":
        return file_storage.read().decode("utf-8", errors="ignore")

    if ext == "docx":
        doc = Document(file_storage)
        text = "\n".join([p.text for p in doc.paragraphs])
        return text

    # Unsupported format
    raise ValueError("Unsupported file type. Please upload a .txt or .docx file.")

from pypdf import PdfReader;

def has_meaning_text(page):
    try:
        data = page.extract_text();
        return bool(data and len(data.strip())>= 30);
    except:
        return False;

def read_pdf():
    reader = PdfReader("");

    for i,page in enumerate(reader.pages):
        if has_meaning_text(page):
            return "text found";
    return "NO_TEXT_FOUND_OR_ERROR";       
print(read_pdf())

# extract_text.py
import PyPDF2

def extract_text_from_pdf(pdf_path, output_txt_path):
    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        with open(output_txt_path, "w", encoding="utf-8") as text_file:
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text_file.write(page.extract_text())

if __name__ == "__main__":
    # Replace with your file paths
    pdf_path = "dataset/textbook.pdf"
    output_txt_path = "dataset/textbook.txt"
    extract_text_from_pdf(pdf_path, output_txt_path)

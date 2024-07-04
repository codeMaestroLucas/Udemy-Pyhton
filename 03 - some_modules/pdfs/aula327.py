# PDFS
# Most of the PDFs will work in this library, but if dosen't work is because it
# dosen't follow the correct regulamentation.

#? Doc: https://pypdf2.readthedocs.io/en/3.0.0/
# pip install pypdf2 PyPDF2[image]

def main() -> None:
    """Function used to run the main code."""
    from pathlib import Path
    from PyPDF2 import PdfReader, PdfWriter, PdfMerger
    
    ROOT_DIR: Path = Path(__file__).parent
    ORIGINAL_FILES: Path = ROOT_DIR / 'original_pdfs'
    NEW_FILES: Path = ROOT_DIR / 'new_pdfs'

    ORIGINAL_PDF: Path = ORIGINAL_FILES / 'R20230210.pdf'


    reader: PdfReader = PdfReader(ORIGINAL_PDF)

    print(reader)
    print(len(reader.pages))

    pg_1 = reader.pages[0]

    print(pg_1.extract_text)
    print(pg_1.images)
    print(len(pg_1.images))

    img_1 = pg_1.images[0]
    
    with open(NEW_FILES / img_1.name, 'wb') as fp:
        fp.write(img_1.data)


    writer: PdfWriter = PdfWriter()
    writer.add_page(pg_1)

    with open(NEW_FILES / 'new_pdf.pdf', 'wb') as file:
        writer.write(file) # Adding the new Page

    with open(NEW_FILES / 'duplicated_pdf.pdf', 'wb') as file:
        for c in range(2):
            for page in reader.pages:
                writer.add_page(page)
                
        writer.write(file) # Adding all the pages from the original PDF to the new PDF


    merger: PdfMerger = PdfMerger()
    
    files: list[Path] = [
        NEW_FILES / 'duplicated_pdf.pdf', # P0
        NEW_FILES / 'new_pdf.pdf', # P1
    ]

    
    with open(ROOT_DIR / 'merged.pdf', 'wb') as merg:
        for file in files:
            merger.append(file)
        
        merger.write(merg)
        # Merging all the PDFs in the files list to a new PDF named merged.pdf

    
if __name__ == '__main__':
    main()
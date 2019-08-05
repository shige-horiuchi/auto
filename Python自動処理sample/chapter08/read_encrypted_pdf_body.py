import sys
from pdfminer.converter import TextConverter
from pdfminer.pdfdocument import PDFDocument, PDFPasswordIncorrect
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

def get_pdf_document(parser, password):
    try:
        document = PDFDocument(parser, password)
    except PDFPasswordIncorrect:
        document = None
        print(f'PDFファイルはパスワードで保護されています')
        if password:
            print(f'指定したパスワードが間違っています')
        else:
            print(f'PDFファイルの後にパスワードを指定してください')
    return document

def read_body(f, password):
    parser = PDFParser(f)
    document = get_pdf_document(parser, password)
    if document is None:
        return
    if not document.is_extractable:
        print(f'このPDF文書はテキスト抽出できません')
        return

    resource_manager = PDFResourceManager()
    device = TextConverter(resource_manager, sys.stdout, codec='utf-8')
    interpreter = PDFPageInterpreter(resource_manager, device)

    for i, page in enumerate(PDFPage.create_pages(document), 1):
        print(f"ページ: {i} {'=' * 32}")
        interpreter.process_page(page)
        print()

    device.close()

def usage():
    if len(sys.argv) < 2:
        print(f'{__file__} の後にPDFファイルを指定してください')
        sys.exit(0)

def main():
    with open(sys.argv[1], 'rb') as f:
        password = ''
        if len(sys.argv) == 3:
            password = sys.argv[2]
        read_body(f, password)

if __name__ == '__main__':
    usage()
    main()

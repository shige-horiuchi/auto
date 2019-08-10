import sys
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

def read_outline(f):
    parser = PDFParser(f)
    document = PDFDocument(parser, None)

    if document.catalog.get('Outlines') is not None:
        outlines = document.get_outlines()
        for level, title, dest, a, se in outlines:
            print(f'階層: {level}, タイトル: {title}')
    else:
        print(f'PDF文書にアウトラインはありません')

def usage():
    if len(sys.argv) < 2:
        print(f'{__file__} の後にPDFファイルを指定して下さい')
        sys.exit(0)

def main():
    with open(sys.argv[1], 'rb') as f:
        read_outline(f)

if __name__ == '__main__':
    usage()
    main()

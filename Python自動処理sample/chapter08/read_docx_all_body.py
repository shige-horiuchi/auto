import docx

doc = docx.Document('book-proposal1.docx')
all_body = '\n'.join(paragraph.text for paragraph in doc.paragraphs)
print(all_body)

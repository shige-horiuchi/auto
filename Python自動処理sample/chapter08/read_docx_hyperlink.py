import docx
from docx.opc.constants import RELATIONSHIP_TYPE as rt

doc = docx.Document('book-proposal1.docx')

print(f'文書内にあるリンク')
for relation in doc.part.rels.values():
    if relation.reltype == rt.HYPERLINK:
        print(relation.target_ref)

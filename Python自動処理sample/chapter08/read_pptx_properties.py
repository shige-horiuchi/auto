import pptx

prs = pptx.Presentation('book-proposal1.pptx')
properties = prs.core_properties

print(f'作成者: {properties.author}')
print(f'カテゴリ: {properties.category}')
print(f'コメント: {properties.comments}')
print(f'キーワード: {properties.keywords}')
print(f'最終編集者: {properties.last_modified_by}')
print(f'件名: {properties.subject}')
print(f'タイトル: {properties.title}')
print(f'文書の作成日時: {properties.created}')
print(f'文書の最終印刷日時: {properties.last_printed}')
print(f'文書の編集日時: {properties.modified}')

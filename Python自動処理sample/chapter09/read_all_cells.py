from openpyxl import load_workbook

filename = 'various_worksheets.xlsx'
wb = load_workbook(filename, read_only=True)
print(f'{filename} のワークシート情報を読み込みます')

ws0 = wb.worksheets[0]        #←最初のワークシートを取得する
print(f'{ws0.title} のセルを1行ずつ表示します')
for row in ws0:        #←行を読み込む
    values = [str(column.value) for column in row]        #←列を読み込む
    print(values)

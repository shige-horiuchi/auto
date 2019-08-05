from openpyxl import Workbook

wb = Workbook()        #←ワークブックを作成
ws = wb.active        #←選択されているワークシートを取得
ws.title = '新しいワークシート'        #←ワークシートの名前を設定
wb.save('new_workbook.xlsx')        #←ワークブック(ファイル)を保存

import sys
from openpyxl import load_workbook
from pprint import pprint

rule_method = {
    'cellIs': 'CellIsRule',
    'colorScale': 'ColorScaleRule',
    'dataBar': 'DataBarRule',
    'expression': 'FormulaRule',
    'iconSet': 'IconSetRule',
}

if len(sys.argv) < 2:
    print(f'{__file__}のあとに条件付き書式設定を持つExcelファイルを指定してください')
    sys.exit(0)

filename = sys.argv[1]
wb = load_workbook(filename)
ws = wb.active
for cond in ws.conditional_formatting:
    for rule in cond.rules:
        rule_method_name = rule_method.get(rule.type)

        if rule_method_name is None:
            continue

        print(f'#' * 32)
        print(f'セルの範囲： {cond.cells}')
        print(f'メールメソッド： {rule_method_name}')
        print(f'パラメーター：')
        pprint(vars(rule))

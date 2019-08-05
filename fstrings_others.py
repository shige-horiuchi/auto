value = 5
print(f'３桁でゼロ詰めしたいとき： {value:03}')
s = str(value)
print('３桁でゼロ詰めしたいとき：', s.zfill(3))

value = 12345678
print(f'３桁ずつカンマ区切りしたいとき： {value:,}')
print()

value = '右寄せ'
print(f'８桁で： {value:_>8}')
value = '左寄せ'
print(f'８桁で： {value:_<8}')
alue = '中央'
print(f'８桁で： {value:_^8}')
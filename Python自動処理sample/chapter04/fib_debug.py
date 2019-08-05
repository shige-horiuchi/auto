def show_fibonacci(index, n):
    x, y = 0, 1
    result = [x, y]
    print(x, y, end=' ')
    z = x + y
    print(z, end=' ')
    result.append(z)
    while z < n:
        x, y = y, z
        z = x + y
        print(z, end=' ')
        result.append(y)
    print()
    print(f'fibonatti[{index}] => {result[index]}')

show_fibonacci(5, 30)

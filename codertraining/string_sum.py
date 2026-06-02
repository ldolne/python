def sum_strings(x, y):
    if x == '' and y == '':
        return '0'
    if x == '':
        return y
    if y == '':
        return x
    result = []
    max_len = len(x) if len(x) > len(y) else len(y)
    for i in range(max_len):
        if i < len(x) and i < len(y):
            rest, addition = make_addition(x[i],y[i])
            result.append(rest + addition)
        elif i >= len(x):
            result.append(int(y[i]))
        elif i >= len(y) :
            result.append(int(x[i]))
    return str(result)

def make_addition(a, b):
    rest = 0
    result = int(a) + int(b)
    if result > 9:
        rest = int(str(result)[0])
        result = int(str(result)[1])
    return (rest, result)
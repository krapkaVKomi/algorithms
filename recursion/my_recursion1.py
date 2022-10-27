

def some(num):
    if num <= 1:
        return 1
    else:
        print('num', num, 'num-1', num-1)
        return num * some(num-1)                         # ретьорн обовязковий, інакше процесору буде сумно


x = some(int(input('Ведіть число:   ')))
print(x)


def some2(num):
    result = 1
    count = 1
    while count <= num:
        result *= count
        count +=1
    return result


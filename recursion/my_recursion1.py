

def some(num):
    if num <= 1:
        return 1
    else:
        print('num', num, 'num-1', num-1)
        return num * some(num-1)


x = some(int(input('Ведіть число:   ')))
print(x)



def some3(num, st):
    if st == 0:
        return 1
    else:
        return num * some3(num, st-1)  # ретьорн обовязковий, інакше процесору буде сумно


print(some3(5, 3))
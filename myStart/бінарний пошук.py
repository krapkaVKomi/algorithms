from random import randint

# Створення списку,
# Його сортування по наростанню
# Вивід на екран
a = []
for i in range(10):
    a.append(randint(1, 50))
a.sort()
print(a)

# Шукане число
value = int(input('Ведіть шукане число\n'))

mid = len(a) // 2
low = 0
high = len(a) - 1

while a[mid] != value and low <= high:
    if value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("No value")
else:
    print("ID =", mid)
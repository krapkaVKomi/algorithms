# знаходемо найбільший спільний дільник


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print(a)


gcd(20, 33)

"""
a = 50
b = 130
 
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
 
print(a + b)
"""
num = int(input('Введите число: '))
ls = []

while num > 10:
    ls.append(num % 10)
    num //= 10
r = max(ls)
print(r)
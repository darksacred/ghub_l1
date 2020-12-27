s = int(input("Введите кол-во секунд: "))

m, s = divmod(s, 60)
h, m = divmod(m, 60)

print(f'{h:02d}:{m:02d}:{s:02d}')
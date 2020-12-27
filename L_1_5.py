varuchka = int(input('Введите выручку: '))
izderzhki = int(input('Введите издержки: '))

if varuchka > izderzhki :
    print("Вы в прибыли!")
    ren = varuchka - izderzhki
    print(f'Ваша выручка: {ren}')
    sotrudnik = int(input("Введите количество сотрудников: "))
    premiya = ren / sotrudnik
    print(f'Прибыль на одного сотрудника: {int(premiya)}')
elif varuchka < izderzhki :
    print("Вы в убытке")
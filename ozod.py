son = int(input('nechta ishchi kelmadi :'))
names = []
for i in range(1,son+1):
    names.append(input(f'{i} - nchi odamning ismini kiriting'))
for name in names:
    print(f'{name.capitalize()}ga xabar yuborildi')

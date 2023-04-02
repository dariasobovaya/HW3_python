kashi = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
f = int(input())
gg = 0
for i in range(f):
    print(kashi[gg])
    gg += 1
    if gg >= 5:
        gg = 0
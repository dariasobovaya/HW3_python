perem1 = [1, 2, 3, 4, 5]
for i in range(4, 0, -1):
    perem1[i] = perem1[i - 1]
perem1[0] = 5
print(perem1)
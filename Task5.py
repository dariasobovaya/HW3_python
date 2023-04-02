spisochek = [3, 5, 2, 3, 14, 2, 3]
gg = 0
for i in range(len(spisochek)):
    for u in range(i + 1, len(spisochek)):
        if spisochek[i] == spisochek[u]:
            gg += 1
print(gg)
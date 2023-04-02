def can_eat(k, f):
    kx = abs(k1 - f1) 
    fx = abs(k2 - f2)
    if kx == 2 and fx == 1 or kx == 1 and fx == 2:
        return 'True'
    else:
        return 'False'
k1 = int(input())
k2 = int(input())
f1 = int(input())
f2 = int(input())
k = k1, k2
f = f1, f2

print (can_eat(k, f))
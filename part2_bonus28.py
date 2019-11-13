a= [0, 2, 3, -4, 5, -1, 2, 3, -4, 5, 1]
for n, i in enumerate(a):
    if i > 0:
        a[n] = 1
    elif i < 0:
        a[n] = -1
    else:
        i == 0
        a[n] = 0    
print(a)
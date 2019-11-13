txt = [1,-2,34,6,7,-8,9,0,-10,-7,6,4,-4,3] 
minus = []
plus = []
for i in txt:
    if i > 0:
        plus.append(i)
    else:
        minus.append(i)
print("Plus:", plus)
print("Minus:", minus)
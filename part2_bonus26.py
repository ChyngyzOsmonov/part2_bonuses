txt = [1,2,34,6,7,8,9,0,10,7,6,4,4,3] 
even = 0
odd = 0
for i in txt:
    if i%2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even)
print("Odd:", odd)

    
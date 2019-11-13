s = input()
a = s.split()
a = ''.join(a)
for i in range(len(a)//2):
    if a[i] != a[-1-i]:
        print("It's not palindrome")
        quit()

print("It's palindrome")
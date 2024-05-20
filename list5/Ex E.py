a=input()
if len (a) > 1:
    a=a[0].capitalize() + a[1:]
else:
    a=a.capitalize()
for i in range (len(a)):
    if a[i] == '.':
        if i+1 < len(a) and a[i+1] != ' ':
            l=a[i+1]
            a=a[:i+1] + a[i+1].capitalize() + a[i+2:]
        elif i+1 < len(a) and a[i+1] == ' ':
            while a[i+1] == ' ':
                i+=1
            l=a[i+1]
            a=a[:i+1] + a[i+1].capitalize() + a[i+2:]
print(a)

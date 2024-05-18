a,b=input().split()
a=int(a)
b=int(b)
def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)
def mmc(a, b):
    return (a * b) / mdc(a, b)
print(mmc(a,b))
while a > 0 and b > 0:
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(mmc(a,b))

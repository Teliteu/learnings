def maior(num, maior):
    if(num < maior):
        return maior
    else:
        return num

PrimNum = int(input())

MaiorNum = PrimNum

for i in range(9):
    x = int(input())
    MaiorNum = maior(x, MaiorNum)

if MaiorNum % PrimNum == 0:
    print(MaiorNum)
    print(PrimNum)
else:
    print(MaiorNum)
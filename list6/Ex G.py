def t(n, f, a, i, p):
    if n > 0:
        p = t(n-1, f, i, a, p)
        if p <= 0:
            return p
        p=p-1
        a.append(f.pop())
        if p <= 0:
            return p
        p = t(n-1, i, a, f, p)
        if p <=0:
            return p
 
    return p
 
 
d,p = input().split()
d= int(d)
p= int(p)
 
g = list(range(d))
g.reverse()
 
h = []
k = []
 
t(d, g, k, h, p)
print(len(g), len(h), len(k))

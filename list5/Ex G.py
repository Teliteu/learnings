t=input()
def mrn (tx):
    for n in '0,1,2,3,4,5,6,7,8,9':
        tx=tx.replace(n,'D')
    return tx
def mrla (tx):
    for la in 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z':
        tx=tx.replace(la,'L')
    return tx
def mrli (tx):
    for li in 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z':
        tx=tx.replace(li,'U')
    return tx
def mre (tx):
    for e in ' ':
        tx=tx.replace(e,'W')
    return tx
print(mre(mrn(mrla(mrli(t)))))

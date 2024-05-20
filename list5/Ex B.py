def conM (tx):
    for li in 'B,C,D,F,G,H,J,K,L,M,N,P,Q,R,S,T,V,W,X,Y,Z':
        tx=tx.replace(li,'p')
    return tx
def conm (tx):
    for la in 'b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z':
        tx=tx.replace(la,'p')
    return tx

f=input()
print(conM(conm(f)))

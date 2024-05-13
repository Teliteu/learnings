hi,mi,hf,mf=input().split()
hi,mi,hf,mf=int(hi),int(mi),int(hf),int(mf)
if hi==hf and mi==mf:
    print ("O jogo durou 24 hora(s) e 0 minuto(s).")
elif hi==hf and mi>mf:
    m=60-(mi-mf)
    print ("O jogo durou 23 hora(s) e %d minuto(s)."%m)
elif hi>hf and mi==mf:
    h = 24-(hi-hf)
    print ("O jogo durou %d hora(s) e 0 minuto(s)."%h)
elif hi<hf and mi==mf:
    h=hf-hi
    print ("O jogo durou %d hora(s) e 0 minuto(s)."%h)
elif hi<hf and mi<mf:
    h=hf-hi
    m=mf-mi
    print ("O jogo durou %d hora(s) e %d minuto(s)." %(h,m))
elif hi<hf and mi>mf:
    h=(hf-hi) - 1
    m=60-(mi-mf)
    print ("O jogo durou %d hora(s) e %d minuto(s)." %(h,m))
elif hi>hf and mi>mf:
    h=23-(hi-hf)
    m=60-(mi-mf)
    print ("O jogo durou %d hora(s) e %d minuto(s)." %(h,m))
else:
    h=24-(hi-hf)
    m=mf-mi
    print ("O jogo durou %d hora(s) e %d minuto(s)." %(h,m))
    
          

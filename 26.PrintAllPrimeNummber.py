c=0
for i in range(0,101):
    for j in range(2,i):
        if(i%j==0):
            c+=1
    if(c==0 and i!=1):
        print(i) 
    c=0
    
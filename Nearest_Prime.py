x=int(input())
for i in range(1,x+1):
    n=int(input())
    a=0
    b=0
    d=0
    for i in range(1,n+1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            if i<=n:
                a=i
                if i>n:
                    break
    i=n+1
    while(i>0):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if(count==2):
            b=i
            d=1
            break
        if d==1:
            break
        else:
            i+=1
    if abs(n-a)<=abs(n-b):
        print(a)
    elif abs(n-a)>abs(n-b):
        print(b)
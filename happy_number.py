def happy(n):
    sum=0
    temp=n
    while(temp):
        r=temp%10
        sum=sum+(r*r)
        temp=temp//10
    if(sum>=10):
        happy(sum)
    else:
        if(sum==1 or sum==7):
            print("True")
        else:
            print("False")
n=int(input())
happy(n)
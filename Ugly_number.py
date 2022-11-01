n=int(input())
x=0
f=0
while(f!=1):
    if n==1:
        print("Ugly Number")
        x=1
        break
    elif n%5==0:
        n/=5
    elif n%3==0:
        n/=3
    elif n%2==0:
        n/=2
    else:
        f=1
if f==1:
    print("Not Ugly Number")
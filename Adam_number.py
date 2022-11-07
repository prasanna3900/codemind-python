def rev(a):
    su=0
    while a>0:
        rem=a%10
        su=su*10+rem
        a=a//10
    return su
a=int(input())
res=rev(a)
if a**2==rev(res**2):
    print("True")
else:
    print("False")
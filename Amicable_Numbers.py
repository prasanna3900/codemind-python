def amicable(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum
a=int(input())
b=int(input())
if amicable(a)==b and amicable(b)==a:
    print("Amicable")
else:
    print("Not Amicable")
    
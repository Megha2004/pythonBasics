n=int(input("enter value for n"))
x=int(input("enter value for x"))
sin=-1
sums=0
for i in range(1,n+1,2):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    p=x**i
    sin=sin*-1
    sums=sums+sin*p/fact
print("sin(",x,")=",sums)

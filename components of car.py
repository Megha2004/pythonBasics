fuel=["electricity","petrol","diesel"]
brake=["disc brake","drum brake","electromagnetic brake"]
engine=["pzd51r engines","rxd500 engines","mr15 engines"]
print("Fuel subdivision:",fuel)
print("Brake subdivisions:",brake)

n=input("enter type of fuel used")
m=input("enter type of brake used")
for x in range(0,3):
    if fuel[x]==n:
        i=x

for x in range(0,3):
    if brake[x]==m:
        j=x

if(i==0 and j==0):
    print("Required Engine",engine[0])
elif(i==0 and j==1):
    print("Required Engine",engine[0])
elif(i==0 and j==2):
    print("Required Engine",engine[0])

elif(i==1 and j==0):
    print("Required Engine",engine[1])
elif(i==1 and j==1):
    print("Required Engine",engine[1])
elif(i==1 and j==2):
    print("Required Engine",engine[1])

elif(i==2 and j==0):
    print("Required Engine",engine[2])
elif(i==2 and j==1):
    print("Required Engine",engine[2])
elif(i==2 and j==2):
    print("Required Engine",engine[2])
else:
    print("invalid option")
    




    

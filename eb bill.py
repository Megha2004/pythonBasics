n=int(input("Enter no of units"))
if(n<=100):
    Amount=n*0.05
    A_Charge=Amount*0.2
elif(n<=250):
    Amount=50+n*0.75
    A_Change=Amount*0.2
elif(n<=500):
    Amount=100+n*1.25
    A_Charge=Amount*0.2
else:
    Amount=250+n*2
    A_Charge=Amount*0.2
Total_amount=Amount+A_Charge
print("Your electricity bill is",Total_amount)

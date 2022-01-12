print("1==grocery,2==clothes,3==icecream,4==e appliances",sep="\n")
pay1=0
pay2=0
pay3=0
pay4=0
a=int(input("enter product nuumber"))      
print("Megha welcomes you to shopping")
if(a==1):
      #grocery
      n=int(input("enter the price of grocery to calculate discount:"))
      if(n==100):
          disc=n*0
      elif(n==150):
          disc=n*0.02
      else:
          disc=n*0.05
      pay1=n-disc
      print("your grocery total is",pay1)
elif(a==2):
      #clothes
      kurti=300
      short_tops=500
      num_kurti=int(input("enter no of kurti purchased"))
      num_short_tops=int(input("enter no of short tops purchased"))
      pay2=kurti*num_kurti+short_tops*num_short_tops
      print("your total price for clothes is",pay2)
elif(a==3):
      #icecream
      butterscotch=50
      chocolate=30
      num_butterscotch=int(input("enter no of butterscotch purchased"))
      num_chocolate=int(input("enter no of chocolate purchased"))
      pay3=butterscotch*num_butterscotch+chocolate*num_chocolate
      print("your icecream purchase is",pay3)
else:
      #e appliances
      n=int(input("enter the price of your e appliances to calculate discount:"))
      if(n<=50000):
          disc=n*0.2
      elif(n<=75000):
          disc=n*0.5
      else:
          disc=n*0.7
      pay4=n-disc
      print("your e appliances total is",pay4)
total_purchase=pay1+pay2+pay3+pay4
print(total_purchase)
if(total_purchase>30000):
    a=total_purchase*0.02
    gst=total_purchase+a
    print("your total purchase: ",gst)
else:
    a=total_purchase*0.03
    gst=total_purchase+a
    print("your total purchase: ",gst)
print("thank you for shopping and visit again")

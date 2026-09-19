item1=input("enter the item name 1")
price1=int(input("enter the price of item1"))
item2=input("enter the item name 2")
price2=int(input("enter the price of item2"))
item3=input("enter the item name 3")
price3=int(input("enter the price of item3"))
item4=input("enter the item name 4")
price4=int(input("enter the price of item4"))

total=price1 + price2 + price3 + price4
if (total>=2000):
  total2=total*0.70
  print ("patable amount is :",total2)
else:
  print("payable amount is :",total)
  print("total amount should be more than 2000 to avail discount")

# electricity bill
unit=int(input("unit consumed by the customer "))

if(unit<=100):
 print("your bill is :", unit*3)
 print("unit charge is 3rs/unit because units are under 100")
elif(100<unit<=200):
  print("your bill is:", unit*5)
  print("unit charge is 5rs/unit because it is between 100 to 200")
elif(200<unit<=300):
 print("your bill is:", unit*7)
 print("unoit charge is 7rs/unit because unit is between 200 to 300")
else:
   print("your bill is:", unit*12) 

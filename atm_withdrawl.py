# ATM CASH WITHDRAWL
need=int(input("enter the amount you need to withdrawl"))
balance=10000

if (need<=balance):
  print("amount withdrawl successful")
  print("remaining balance:",balance-need)
else:
    print("balance is not sufficient")

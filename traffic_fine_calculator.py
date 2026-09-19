speed=int(input("enter the vehicle speed"))

if(70<speed<=100):
    print("vehicle is fined:",1000)
elif(100<speed<=180):
    print("vehicle is fined :",2500)
elif(speed>180):
    print("vehicle is fined:",5000)
else:
    print("speed is under limit ")
    

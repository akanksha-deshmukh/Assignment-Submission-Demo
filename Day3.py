ops = int(input("Enter the Altitude of the plane: "))

if ops == 3000 :
  print("Plane is safe for landing")
elif ops >= 3000 and ops <= 6000:
  print("Come down to 3000 and open landing gear")  
elif ops >= 6000 :
  print("Go around")
else:
  print("Plane is not safe for landing")    
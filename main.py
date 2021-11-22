print("Select your ride:")
print("1. Bike")
print("2. Car")
print("3. SUV")
choice=int(input())
if( choice == 1 ):
  print( "You have selected Bike" )
elif( choice == 2 ):
  print( "You have selected Car" )
elif( choice == 3 ):
  print( "You have selected SUV" )
else:
  print("Wrong choice!")
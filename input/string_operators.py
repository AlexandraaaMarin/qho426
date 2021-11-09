my_list = []
n = int(input("Enter the number of lives:"))
c=int(input("Enter the energy level:"))
d=int(input("Enter the shield level:"))
print("Health has been set.")
print("Number of lives:")
for i in range(0, n):
    print('\u2665', end=" ")
print("\n")


print("Energy level:")
for i in range(0,c):
    print('\u25c6', end=" ")
print("\n")


print ("Shield level:")
for i in range(0,d):
    print('\u25c6',end=" ")
 
print("\n")


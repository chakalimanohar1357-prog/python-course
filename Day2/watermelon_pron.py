# wt = int(input("Enter the weight of the watermelon in kg: "))
# if wt % 2 == 0:
#     print("YES")
# else:
#     print("NO")


######### elephant problem########

# x = int(input("Enter the number of coordinates: "))
# if x % 5 == 0:
#     print(x//5)
# else:
#     print(x//5 + 1)

####leap year problem ####
y = int(input("Enter the year: "))
if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")    


### nested if ####


# age = int(input("Enter your age: "))
# if age > 13:
#   if age < 19:
#     print("You are teen.")
#   elif age < 35:
#     print("You are adult.")
#   else:
#     print("You are senior citizen.")
# else:
#   print("You are child.")\

######   marks grade  #####


# marks = int(input("Enter your marks: "))
# if marks >= 90:
#     print("Grade A")
# elif marks >= 80:
#     print("Grade B")
# elif marks >= 70:
#     print("Grade C")
# elif marks >= 60:
#     print("Grade D")
# else:
#     print("Grade F")

#### greater number ####
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# if a > b:
#     print("The greater number is:", a)
# else:
#     print("The greater number is:", b)

#### 3 numbers ####
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c:
    print("The greatest number is:", a)
elif b>a and b > c:
    print("The greatest number is:", b)
else:
    print("The greatest number is:", c)        
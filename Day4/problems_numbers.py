#####perfect square or not#####

# n = int(input("Enter a number: "))
# for i in range(1, n + 1):
#     if i * i == n:
#         print( " yes.")
#         break
# else:
#         print( "no.")

#########perfect number or not########

# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1, n):
#     if n % i == 0: 
#         sum += i
# if sum == n:
#     print("yes")
# else:
#     print("no")

###bitwise even or odd#####

# n = int(input("Enter a number: "))
# if n &1 == 1:
#     print("odd")
# else:
#     print("even")

#####power of 2 or not#####

# n = int(input("Enter a number: "))
# while n > 1:
#     if n % 2 != 0:
#         break
#     n = n // 2
# if n == 1:
#     print("yes")
# else:
#     print("No")

#####using bitwise operator#####

# n = int(input("enter number:"))
# if n & n-1 == 0:
#     print("yes")
# else:
#     print("no")


#### armstrong number ###
n = int(input("Enter a number: "))
original = n

count = 0
temp = n

while temp > 0:
    count += 1
    temp = temp // 10

sum = 0
temp = n

while temp > 0:
    rem = temp % 10
    sum += rem ** count
    temp = temp // 10

if sum == original:
    print("yes")
else:
    print("no")

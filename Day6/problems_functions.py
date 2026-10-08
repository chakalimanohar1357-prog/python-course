#####even or odd ######
# def eo(n):
#     if n % 2 == 0:
#         print("even")
#     else:
#         print("not")
# eo(3)  

######## sqaure of num#######3
# def sq(n):
#     return n**2
# x = sq(5)
# print(x)

#####
# def sq(n):
#     return n**2
# x = sq(25)
# print(x)       

########## max of 2 no######3
# def no(*args):
#     print(max(args))
# no(10,20,30)

########power of 2#####

# def nitin(n,a):
#     return n**a
# x=nitin(5,2)
# print(x)

#######reverse of number####

# def reverse_number(n):
#     rev = 0
#     while n > 0:
#         digit = n % 10
#         rev = rev * 10 + digit
#         n = n // 10
#     return rev
# x=reverse_number(int(input("enter no:")))
# print(x)

######## count no of digits ######
# def number(n):
#     count = 0
#     while n > 0:
#          = n % 10
#         count +=1
#         n = n // 10
#     return count
# x= number(int(input("enter no:")))
# print(x)

#####sum of digits#######

# def sumofdigits(n):
#     sum = 0
#     while n > 0:
#         rem = n % 10
#         sum = sum + rem
#         n = n // 10
#     return sum
# x=sumofdigits(int(input("enter no:")))
# print(x)


############armstrong number########


# def is_armstrong(n):
#     temp = n
#     digits = len(str(n))
#     total = 0
#     while temp > 0:
#         digit = temp % 10
#         total = total + (digit ** digits)
#         temp = temp // 10
#     return total == n

# num = int(input("Enter a number: "))

# if is_armstrong(num):
#     print(num, "is an Armstrong number")
# else:
#     print(num, "is not an Armstrong number")


###########perfect number or not########


# def is_perfect(n):
#     total = 0

#     for i in range(1, n):
#         if n % i == 0:
#             total += i

#     return total == n

# num = int(input("Enter a number: "))

# if is_perfect(num):
#     print(num, "is a Perfect Number")
# else:
#     print(num, "is not a Perfect Number")

############perfect square or not#####

# def is_perfect_square(n):
#     i = 1

#     while i * i <= n:
#         if i * i == n:
#             return True
#         i += 1

#     return False

# num = int(input("Enter a number: "))

# if is_perfect_square(num):
#     print(num, "is a Perfect Square")
# else:
#     print(num, "is not a Perfect Square")


################ prime or not############

# def prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# n = int(input("Enter a number: "))
# if prime(n):
#     print("Prime")
# else:
#     print("Not")

#############facorial###########

# def fac(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact = fact * i
#     return fact

# n = int(input("Enter a number: "))
# print("Factorial =", fac(n))

################poer 0f 2##########

# def power_of_2(n):
#     while n > 1:
#         if n % 2 != 0:
#             return False
#         n = n // 2
#     return True
# n = int(input("Enter a number: "))

# if power_of_2(n):
#     print("Power of 2")
# else:
#     print("Not a Power of 2")



##############fibonacci series######333

# def fibonacci(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         print(a, end=" ")
#         c = a + b
#         a = b
#         b = c
# n = int(input("Enter the number of terms: "))
# fibonacci(n)    


############celcius to farenheit#######


# def celsius_to_fahrenheit(c):
#     f = (c * 9/5) + 32
#     return f
# x = celsius_to_fahrenheit(25)
# print(x)


############### farenheit to celcius#######

def f_to_c(f):
    cel = (f-32)*5/9
    return cel
x = f_to_c(77)
print(x)

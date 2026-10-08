################## recurrsion ################
# def numbers(n):
#     if n == 0:
#         return
#     print(n)
#     numbers(n-1)
# numbers(6)

########################
# def numbers(n):
#     if n == 7:
#         return
#     print(n)
#     numbers(n+1)
# numbers(1)


############# factorial#############33


# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))

############## fibonacci series #############

# def fib(n):
#     if n<=1:
#         return n
#     return fib(n-1)+fib(n-2)
# fib(6)
# print(fib(6))
    
############### reverse#####################
def reverse(n, rev=0):
    if n == 0:
        return rev
    return reverse(n // 10, rev * 10 + n % 10)

num = int(input("Enter a number: "))
print("Reverse:", reverse(num))
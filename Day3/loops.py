
# for i in range(1,11):
#     print(i)

####table of 5 ####
# n= int(input("Enter a number: "))
# for i in range(1, 11):
#     print(n, "x", i, "=", n*i)

##### even numbers ####
# for i in range(21):
#     if i % 2 == 0:
#         print(i)

###while loop ###
# i = 0
# while(i<=10):
#     print(i)
#     i+=1


#########sum of n numbers ####

# n = int(input("Enter a number: "))
# i=0
# sum=0
# while(i<=n):
#     sum += i
#     i += 1
#     print("The sum of first", n, "natural numbers is:", sum)

###### reverse number ####


# n = int(input("Enter a number: "))
# rev = 0
# while(n>0):
#     rem = n % 10
#     rev = rev * 10 + rem
#     n = n // 10
#     print("The reverse of the number is:", rev)


#### palindrome number ####


# n = int(input("Enter a number: "))
# temp = n
# rev = 0
# while(n!=0):
#     rem = n % 10
#     rev = rev * 10 + rem
#     n = n // 10
# if(rev == temp):
#     print("palindrome.")
# else:
#     print("not a palindrome.")


#########sum of digits ####
# n = int(input("Enter a number: "))
# sum = 0
# while(n!=0):
#     rem = n % 10
#     sum = sum + rem
#     n = n // 10
# print(sum)



#######product of digits ####


# n = int(input("Enter a number: "))
# product = 1
# while(n!=0):
#     rem = n % 10
#     product = product*rem
#     n = n//10
#     print(product)


#######count number of digits ####


# n = int(input("Enter a number: "))
# count = 0
# while(n>0):
#     rem = n%10
#     count += 1
# n = n // 10
# print(count)

###### number of steps to reduce a number to zero ####
# n = int(input("Enter a number: "))
# count = 0
# while(n!=0):
#     if n % 2 == 0:
#         n = n // 2
#     else:
#         n = n - 1
#     count += 1
# print(count)

####### SUB PRODUCT AND SUM OF DIGITS ####
# n = int(input("Enter a number: "))
# sum = 0
# product = 1
# while(n!=0):
#     rem = n % 10
#     sum = sum + rem
#     product = product*rem
#     n = n // 10
# print(sum - product)

###break , continue#####
for i in range(1, 11):
    if i == 5:
        break
    print(i)

    for i in range(1, 11):
        if i == 5:
            continue
        print(i)
        
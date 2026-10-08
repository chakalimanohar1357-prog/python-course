############ decimal to binary##########
# n = 10
# c = " "
# while(n>0):
#     rem = n%2
#     c = str(rem) + c
#     n = n//2
# print(c)    



#################binary to decimal#########

# s = "1010"
# sum = 0
# power = 0
# for i in range(len(s)-1,-1,-1):
#     sum += int(s[i]) * (2 ** power)
#     power += 1
# print(sum)


############### decimal to octal######
    
# n = 100
# c = " "
# while(n>0):
#     rem = n%8
#     c = str(rem) + c
#     n = n//8
# print(c)    

########## octal  t0 decimal ######

# s = "1010"
# power = 0
# sum = 0
# for i in range(len(s)-1,-1,-1):
#     sum += int(s[i])*(8**power)
#     power += 1
# print(sum)

##############decimal to hexadecimal########
# n = 100
# hexa = "0123456789ABCDEF"
# n1 = " "
# while(n>0):
#     n1 = hexa[n % 16] + n1
#     n = n//16
# print(n1) 


################hexa to decimal##########


# hexa=input().upper()
# digits="0123456789ABCDEF"
# decimal=0
# power=0
# for i in range(len(hexa)-1, -1, -1):
#     decimal += digits.index(hexa[i]) * (16 ** power)
#     power += 1
# print(decimal)


############### BINARY TO OCTAL######
####Binary to Octal###

# binary = input()
# decimal = 0
# for i in binary:
#     decimal = decimal * 2 + int(i)
# octal = ""
# while decimal > 0:
#     octal = str(decimal % 8) + octal
#     decimal = decimal // 8
# print(octal)


#########Octal to Binary#######

# octal = input()
# decimal = 0
# for i in octal:
#     decimal = decimal * 8 + int(i)
# binary = ""
# while decimal > 0:
#     binary = str(decimal % 2) + binary
#     decimal = decimal // 2
# print(binary)


############Binary to Hexadecimal###########

# binary = input()
# decimal = 0
# for i in binary:
#     decimal = decimal * 2 + int(i)
# hexa = "0123456789ABCDEF"
# result = ""
# while decimal > 0:
#     result = hexa[decimal % 16] + result
#     decimal = decimal // 16
# print(result)


###########Hexadecimal to Binary#############

# hexa = input().upper()
# digits = "0123456789ABCDEF"
# decimal = 0
# for i in hexa:
#     decimal = decimal * 16 + digits.index(i)
# binary = ""
# while decimal > 0:
#     binary = str(decimal % 2) + binary
#     decimal = decimal // 2
# print(binary)


############Octal to Hexadecimal###########

# octal = input()
# decimal = 0
# for i in octal:
#     decimal = decimal * 8 + int(i)
# hexa = "0123456789ABCDEF"
# result = ""
# while decimal > 0:
#     result = hexa[decimal % 16] + result
#     decimal = decimal // 16
# print(result)


############### Hexadecimal to Octal ############
# hexa = input().upper()
# digits = "0123456789ABCDEF"
# decimal = 0
# for i in hexa:
#     decimal = decimal * 16 + digits.index(i)
# octal = ""
# while decimal > 0:
#     octal = str(decimal % 8) + octal
#     decimal = decimal // 8
#  print(octal)


######## COUNT NO OF BITS IN BINARY#####
# n = int(input("Enter a number: "))
# count = 0
# while n > 0:
#     count += 1
#     n = n >> 1
# print(count)


#########count no 1 in binary######
n = int(input("Enter a number: "))
count = 0
while n > 0:
    if n & 1 == 1:
        count += 1
    n = n >> 1
print(count)
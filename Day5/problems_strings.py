#####revrese of a string######
# name = "manohar"
# print(name[::-1])

######reverse without slicing######3


# s = "python"
# reverse = " "
# for i in s:
#     reverse = i + reverse
# print(reverse)


#############palindrome########


# s = input("enter string:")
# x = s[::-1]
# if s==x:
#     print("palindrme")
# else:
#     print("not")

#########4.count no of vpwels######


# s = input("enter string:")
# v = "aeiou"
# count = 0
# for i in s:
#     if i in v:
#         count += 1
# print(s)
# print(count) 

        
########6.no of consonants#####



# s = input("enter string:")
# v = "aeiou"
# count = 0
# for i in s:
#     if i not in v:
#         count += 1
# print(s)
# print(count)         

########count no of upper and lower letters######

# s = input("enter string:")
# upper = 0
# for i in s:
#     if i.isupper():
#         upper += 1
# print(upper)

##########lower############
# s = input("enter string:")
# lower = 0
# for i in s:
#     if i.islower():
#         lower += 1
# print(lower)

############COUNT OF SRINGS########
# s = "python"
# count = 0
# for i in s:
#     count += 1
# print(count)


###################################
# s = "i like python"
# print(s.replace(" ",""))
###################################removing duplictes###########
# s= "college"
# res = ""
# for i in s:
#     if i not in res:
#         res += i
# print(res)


#################### count no of letters in string#########
# s = "college"
# cou = ""
# for i in s:
#     if i not in cou:
#         print(i,"-",s.count(i))
#         cou += i

################## count first non repeationg element########

# s = "college"
# for i in s:
#     if s.count(i) == 1:
#         print(i)
#         break
# else:
#      print("no element")   
        

########################## anagram ###############
s1 = "computer"
s2 = "moputcer"
if sorted(s1) == sorted(s2):
    print("anagram")
else:
    print("not")    
        
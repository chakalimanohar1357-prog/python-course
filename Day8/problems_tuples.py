##############sum of elements in tuple#########3

# t = ((1, 2, 3), (3, 4))
# sum = 0
# for i in t:
#     for j in i:
#         sum += j
# print(sum)

##########333want only prime no#########
# t = (2,3,4,5,6,7,8,9,10,11)
# prime = []
# for num in t:
#     if num>1:
#         for i in range(2,num):
#             if num%i == 0:
#                 break
#         else:
#                 prime.append(num)
# print(tuple(prime))
        
###############common elements##########

# l = [1,2,3,4,5]
# s = {3,4,5,6}
# t = (2,3,5,7)
# common = []
# for i in t:
#     if i in l and i in s:
#         common.append(i)
# print(common) 

##############count unique elements###########

# t = (1,2,2,3,4,4,5)
# s = set(t)
# print(len(s))


#################difference###########

# l = [1,2,3,4,5]
# t = set(l)
# s = {3,5}
# print(tuple(t-s))

#############same but using not in #############

# l = [1, 2, 3, 4, 5]
# s = {3, 5}
# result = ()
# for i in l:
#     if i not in s:
#         result += (i,)
# print(result)

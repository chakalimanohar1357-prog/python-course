#######sum of even elements at odd index######
# a = [1,2,3,4,5,6,7,8]
# sumofeven = 0
# for i in range(len(a)):
#     if a[i]%2==0 and i%2!=0:
#         sumofeven += a[i]
# print(sumofeven)        
    
    
    
#################sum of even elemets in even index#######
# a = [1,2,60,4,5,6,90,8]
# sumofeven = 0
# for i in range(len(a)):
#     if a[i]%2==0 and i%2==0:
#         sumofeven += a[i]
# print(sumofeven)    


####sum of odd elements in even index#####3


# a = [1,2,3,4,5,6,7,8]
# sumofodd = 0
# for i in range(len(a)):
#     if a[i]%2!=0 and i%2==0:
#         sumofodd += a[i]
# print(sumofodd)    

####sum of odd elements in odd index#####3

# a = [1,2,3,4,5,6,7,8]
# sumofodd = 0
# for i in range(len(a)):
#     if a[i]%2!=0 and i%2!=0:
#         sumofodd += a[i]
# print(sumofodd)    


##########unique numbers in list####333333

# a = [1,2,3,4,5,5,6,6,777,7]
# for i in a:
#     if a.count(i)==1:
#         print(i)

############# sunrise problem ###############

# a = [3, 4, 5, 4, 7, 6, 2, 2, 6, 8]
# maximum = a[0]
# count = 0
# for i in (a):
#     if i > maximum:
#         count += 1
#         maximum = i
# print(count)


########## sum of any 2 elememts ==9 ########### 


# a = [5,2,7,4,6]
# t = 10
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i] + a[j]==t:
#             print(a[i],a[j])

#########################################################33

# a = [2,7,11,15]
# t = 9
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i] + a[j]==t:
#             print(i,j)
            
##########left rotate array###########  
# a = [1,2,3,4,5]
# s = a[:2]
# e = a[2:]
# print(e+s)


#############right rotate array#######

# a = [1,2,3,4,5]
# s = a[:-2]
# e = a[-2:]
# print(e+s)

############even no shuld be in descending and odd in ascending########

# a = [1,2,3,4,5,6,7,8,9,10,11,12]
# even = []
# odd = []
# for i in a:
#    if i%2==0:
#        even.append(i)
#        even.sort()
#        even.reverse()
#    else:
#        odd.append(i)
# print(even+odd)

##############same but using single container result[]#############

# a = [1,2,3,4,5,6,7,8,9,10,11,12]
# result = []
# for i in a:
#     if i % 2 == 0:
#         result.insert(0, i)   
#     else:
#         result.append(i)      
# print(result)

#######################################
##o/p = 1,2,4,0,0,0

# a = [1,0,2,0,4,0]
# result1 = []
# result2 = []
# for i in a:
#     if i != 0:
#         result1.append(i)
#     else:
#         result2.append(i)   
# print(result1+result2)


#########33using one empty list#3333#3333
# a = [1,0,2,0,4,0]
# result = []
# for i in a:
#     if i > 0:
#         result.append(i) 
# while(len(result)<len(a)):
#     result.append(0)
# print(result)


######without empty list######3
# a = [1,0,2,0,4,0]
# a.sort()
# print(a[3:]+a[:3])
######################################

# def moveZeroes(self, nums):
#     index = 0
#     for i in range(0,len(nums)):
#         if nums[i] != 0:
#             nums[index],nums[i] = nums[i],nums[index]
#             index += 1 
#             print(nums)  
 #################################################       
    # def moveZeroes(self, nums):
    #     for i in nums:
    #         if i == 0:
    #             nums.remove(i)
    #             nums.append(i)      
    #             print(nums)
    
 ####################leet code  485 #############################

# nums = [1,0,1,1,0,1]
# def findMaxConsecutiveOnes(nums):
#     c = 0
#     mc = 0

#     for i in range(len(nums)):
#         if nums[i] == 1:
#             c += 1
#             mc = max(mc, c)
#         else:
#             c = 0

#     print(mc)

# findMaxConsecutiveOnes(nums)

# d = {}
# for i in range(1,6):
#     d[i]=i*i
# print(d)

#####################2nd method#######################################

# n = int(input("Enter number of students: "))
# m = {}
# for i in range(n):
#     m[i] = i*i
# print(m)

###################################
# s = "banana"
# m={}
# for i in s:
#     m[i]=s.count(i)
# print(m)
    
###################2 method########################################
    
# s = "banana"
# d = {}
# for ch in s:
#     if ch in d:
#         d[ch] += 1
#     else:
#         d[ch] = 1
# print(d)

###################3rd method################################

# s = "banana"
# m={}
# for i in s:
#     m[i]=m.get(i,0)+1
# print(m)
    
    
#############sum of values#########
# d = {"a":10,"b":20,"c":30}
# sum = 0
# for v in d.values():
#     sum += v
# print(sum)

#############max of values##########

# d = {"a":10,"b":20,"c":30}
# max_value = 0
# for i in d:
#     if d[i]>max_value:
#         max_value = d[i]
# print(max_value)        
    
################count keys###########3

# d = {"a":10,"b":20,"c":30}
# count = 0
# for i in d:
#     count += 1
# print(count)

################most frequent char###########3

# s = "engineering"
# d = {}
# l = 0
# mc = ""
# for i in s:
#     d[i]=s.count(i)
#     if d[i]>l:
#         l = d[i]
#         mc = i
# print(mc,l) 

################ 2nd method ########## 

# s = "banana"
# d = {}
# for i in s:
#     d[i]=s.count(i)
# print(max(d,key=d.get))


################### even no and odd no ##############
# n = [1,2,3,4,5,6,7]
# even = 0
# odd = 0
# d = {}
# for i in n:
#     d[i]=n.count(i)
#     if i%2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(even,odd)

################# find duplictes elements########

# l = [1,2,3,2,4,1,5]
# d = {}
# for i in l:
#     d[i]=l.count(i)
# for i in d:
#         if d[i]>1:
#             print(i)
    
############3leetcode two sum using dictionary ########
# nums = [2,7,11,15]
# target = 9
# def twoSum(nums, target):
#     d = {}
#     for i in range(len(nums)):
#         diff = target - nums[i]
#         if diff in d:
#             return [d[diff], i]
#         d[nums[i]] = i
# x = twoSum(nums,target)
# print(x)        

####################total milage##################################

# logs = [{"km":200,"litre":5},
#         {"km":350,"litre":8}]
# total_m=0
# total_l=0
# for i in logs:
#     total_m += i["km"]
#     total_l += i["litre"]
#     milage = total_m/total_l
# print(milage)

# #############
# arr = [(3,1),(2,5),(3,0),(2,1)]
# arr.sort(key=lambda t:(t[0],-t[1]))
# print(arr)

############################################################

class Solution:
    def longestConsecutive(self, nums):
        ans = 0

        for num in nums:
            if num - 1 not in nums:
                count = 1

                while num + 1 in nums:
                    num += 1
                    count += 1

                ans = max(ans, count)

        return ans
    
    ##############################################33######
    
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maximum = max(candies)
        result = []
        for i in candies:
            if i + extraCandies >= maximum:
                result.append(True)
            else:
                result.append(False)

        return result
    
    
    
    ###############################################
    
class Solution:
    def longestConsecutive(self, nums):
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                current = num
                count = 1
                while current + 1 in nums:
                    current += 1
                    count += 1
                if count > longest:
                    longest = count
        return longest

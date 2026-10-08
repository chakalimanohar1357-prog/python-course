#######two pointer ############

# arr = [1,2,3,4,5]
# left = 0
# right = len(arr)-1
# while(left<=right):
#     print(arr[left],arr[right])
#     left +=1
#     right -= 1


#############reverse of two pointers########


# arr = [1,2,3,4,5]
# left = 0
# right = len(arr)-1
# while(left<right):
#     arr[left],arr[right] == arr[right],arr[left]
#     left +=1
#     right -= 1
# print(arr)    


########3palindrome using 2 pointer############



# arr = [1,2,3,2,1]
# left = 0
# right = len(arr)-1
# while(left<right):
#    if(arr[left] == arr[right]): 
#        print("yes")
#        break
# else:
#        print("no")
#        left +=1
#        right -= 1   


#################two sum using two pointers###########
# Two Sum 
# arr = [1, 2, 3, 4, 5]
# target = 9

# left = 0
# right = len(arr) - 1

# while left < right:
#     if arr[left] + arr[right] == target:
#         print(arr[left], arr[right])
#         break
#     elif arr[left] + arr[right] < target:
#         left += 1
#     else:
#         right -= 1


#################sliding window################
# arr = [2, 1, 5, 1, 2, 3]
# k = 3
# window_sum = sum(arr[:k])
# max_sum = window_sum
# for i in range(k, len(arr)):
#     window_sum = window_sum - arr[i - k] + arr[i]
#     max_sum = max(max_sum, window_sum)
# print("Maximum Sum:", max_sum)


#################how amy ab in abababd############



s = "abababd"
count = 0
k = 2
for i in range(len(s)-k+1):
    if s[i:i+k] == "ab":
        count += 1
print(count)
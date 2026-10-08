############### linear search #########

# arr = [1,2,3,4,5,6,7,8,9,10]
# t =6
# for i in arr:
#     if i == t:
#         print("found")
#         break
# else:
#     print("not")


################# binary search ######3333333

arr = [10,20,30,40,50,60,70]
t = 50
left = 0
right = len(arr) - 1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == t:
        print("Found at index", mid)
        break
    elif arr[mid] > t:
        right = mid - 1
    else:
        left = mid + 1
else:
    print("Not Found")
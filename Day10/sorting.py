#################bubble sort ###########3
# arr = [5, 4, 3, 2, 1]
# for i in range(len(arr) - 1):
#     for j in range(len(arr) - 1 - i):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
#             print(arr)

# print("Sorted Array:", arr)


##################### slection sort ##############

# arr = [5, 4, 3, 2, 1]
# for i in range(len(arr) - 1):
#     min_index = i
#     min_element = arr[i]
#     for j in range(i + 1, len(arr)):
#         if arr[j] < min_element:
#             min_element = arr[j]
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index], arr[i]

#     print(arr)

# print("Sorted Array:", arr)


############# insertion sort ######################
arr = [5, 4, 3, 2, 1]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key
    print(arr)

print("Sorted Array:", arr)
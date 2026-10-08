#######sum of list elements########
# a = [10,20,30,40]
# sum = 0
# for i in range(len(a)): 
#     sum += a[i]
# print(sum)


########largest ele in list######
# a = [10,20,30,40]
# largest =0
# for i in range(len(a)):
#     if a[i] > largest:
#         largest = a[i]
# print(largest)   

#############smallest  element in list#########
# a = [10,20,30,40]
# smallest = a[0]
# for i in range(len(a)):
#     if a[i] < smallest:
#         smallest = a[i]
# print(smallest)   

#######count elements######

# a = [10,20,30,40,20]
# print(len(a))

########even or odd elements########

# a = [10,20,30,40,33,47,69]
# even = 0
# odd = 0
# for i in a:
#     if i%2==0:
#         even += 1
#     else:
#         odd += 1
# print(even)
# print(odd)


######## remove  duplicates######


# a = [10,20,30,10,10]
# s = []
# for i in a:
#     if i not in s:
#         s.append(i)
# print(s)    
        
        
###### 2nd largest element#########

# a = [10,20,30,35,40,45]
# a.sort()
# largest = 0
# secondlargest = 0
# for i in range(len(a)):
#     if a[i] > largest:
#         secondlargest = largest
#         largest = a[i]
# print(secondlargest) 
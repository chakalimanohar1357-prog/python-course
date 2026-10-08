########## remove duplicates(using set)############

# l = [1,2,3,1,3,4]
# s = set(l)
# w = list(s)
# print(w)


############union and intresection#############

# t1 = "python is a great programming language"
# t2 = "many developers love the python language"
# print(set(t1.split())&set((t2.split())))
# print(set(t1.split())|set((t2.split())))


########leet code 217###########
nums = [1, 2, 3, 1]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            print ("True")
        else:
            print ("False")

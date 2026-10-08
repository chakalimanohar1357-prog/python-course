# n = 4
# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

####no patterns######
# n = 4
# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end=" ")
#     print()

    ########
# n = 4
# for i in range(1, n + 1):
#     for j in range(1,i + 1):
#         print(j, end=" ")
#     print()
###############
# n = 5
# for i in range(n, 0, -1):
#     for j in range(i):
#         print(i, end="")
#     print()

####################
# rows = 4
# for i in range(rows, 0, -1):
#     for j in range(1,i+1):
#         print(j, end="")
#     print()
#####################
# rows=4
# n = 1
# for i in range(1,rows + 1):
#     for j in range(i):
#         print(n, end="")
#         n += 1
#     print()
###########################3
# n = 4
# ch = 65 
# for i in range(1, n + 1):
#     for j in range(i):
#         print(chr(ch), end=" ")
#         ch += 1
#     print()
#########################
# n = 4
# for i in range(1, n + 1):
#     ch = 65
#     for j in range(i):
#         print(chr(ch), end=" ")
#         ch += 1
#     print()
###################square###########3
# n = 4
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
######################pyramid##########
# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * (2 * i - 1))
    
    #############revrese pyramid########
n = 5
for i in range(1, n + 1):
     print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n,0,-1):
    print(" " * (n - i) + "*" * (2 * i - 1))
    
    
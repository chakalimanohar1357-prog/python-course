# EXTRA (added): more recursion problems (same style as recursion.py)

############# sum of first n numbers #############
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(5))            # 15


############# sum of digits #############
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

print(sum_digits(1234))    # 10


############# count digits #############
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

print(count_digits(12345))  # 5


############# power (a ** b) #############
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

print(power(2, 5))         # 32


############# print 1 to n and n to 1 together (going and coming back) #############
def up_down(n):
    if n == 0:
        return
    print(n, end=" ")
    up_down(n - 1)
    print(n, end=" ")

up_down(3)                 # 3 2 1 1 2 3
print()


############# reverse a string #############
def reverse_string(s):
    if s == "":
        return ""
    return reverse_string(s[1:]) + s[0]

print(reverse_string("python"))   # nohtyp


############# palindrome string #############
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("madam"))     # True
print(is_palindrome("python"))    # False


############# GCD (Euclid) #############
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))         # 6


############# binary search (recursive) #############
def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)

arr = [10, 20, 30, 40, 50, 60, 70]
print(binary_search(arr, 50, 0, len(arr) - 1))   # 4

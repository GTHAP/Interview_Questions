# Recursion | Time - O(2^n) | Space - O(N)

# def climbStairs(n):
#     if n is None:
#         return None
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n == 3:
#         return 3
#     return climbStairs(n - 2) + climbStairs(n - 1)

# Dynamic Programming | Fibonacci Number | Time - O(N) | Space - O(1)

def climbStairs(n):
    if n == 1:
        return 1
    first = 1
    second = 2
    for i in range(3, n + 1):
        third = first + second
        first = second
        second = third
    return second

n = 38
climbStairs(n)

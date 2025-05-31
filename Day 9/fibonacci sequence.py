from collections import deque
import copy
fib_list=[0,1]

def fib(iteration,fib_list:list[int]):
    next=0
    fib_list_copy=fib_list.copy()
    additions=deque()
    for i in range(2):
        additions.append(fib_list_copy.pop())

    print(additions)
    for i in range(iteration):
        next=additions[len(fib_list) - 1] + additions[len(additions) - 2] #next = additions[-1] + additions[-2] always use -1 -2 for last elements and not the length
        fib_list.append(next)
        additions.append(next)
    print("additions after iterations: " + str(additions))


fib(10,fib_list)
print("fib_list after iterations: " + str(fib_list))

# ---------------------------------------------------------------
# chatgpt versions:
#
# Iterative Version:
# python
# Copy
# Edit
# def fibonacci(n):
#     sequence = []
#     a, b = 0, 1
#     for _ in range(n):
#         sequence.append(a)
#         a, b = b, a + b
#     return sequence
#
# # Example usage:
# print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#
#
#
#
# Recursive Version (less efficient for large n):
# python
# Copy
# Edit
# def fib_recursive(n):
#     if n <= 1:
#         return n
#     return fib_recursive(n-1) + fib_recursive(n-2)
#
# # Print first 10 Fibonacci numbers
# for i in range(10):
#     print(fib_recursive(i), end=" ")
#
#
#
# Fastest (using memoization / dynamic programming):
# python
# Copy
# Edit
# def fibonacci_memo(n, memo={}):
#     if n in memo:
#         return memo[n]
#     if n <= 1:
#         return n
#     memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
#     return memo[n]
#
# # Example: Get the 30th Fibonacci number
# print(fibonacci_memo(30))
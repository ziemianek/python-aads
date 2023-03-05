"""

Recursion is a way of solving a problem by having a function calling itself
    -- performing the same operation multiple times with different inputs
    -- in every step we try smaller inputs to make the problem smaller
    -- base condition is needed to stop the recursion, otherwise infinite loop will occur

"""

# basic example using russian doll:
def open_russian_doll(doll):
    if doll == 1:
        return "All dolls are opened"
    else:
        open_russian_doll(doll - 1)

"""

How recursion works?
    -- a method calls itself
    -- then exits from infinite loop

When to use recursion?
    -- when we can breakdown a problem into similar subproblems
    -- when we dont mind some extra overhead (both time and space) that comes with it
    -- when we need a solution quickly but we dont care about efficiency
    -- when we traverse a tree
    -- when we use memorization in recursion

When to avoid recursion?
    -- when time and space complexity matters for us
    -- when we have limited memory
    -- when we care about efficiency

3 STEPS TO CODE RECURSION:
    1) Recursive case - the flow
    2) Base case - the stopping condition
    3) Unintentional case - the constraint

"""

# counting factorial using recursion
# example:
# 4! == 4*3*2*1 == 24
def factorial(n):
    assert n >= 0 and int(n) == n, \
        "The number must be a non-negative interger only"
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)

print(f"4! = {factorial(4)}")  # output: 4! = 24


# calculating Fibbonacci numbers using recursion
# Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...  
# example:
# fib(7) ==  13
def fib(n):
    assert n >= 0 and int(n) == n, \
        "The number must be a non-negative interger only"
    if n in [0, 1]:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

print(f"fib(7) = {fib(7)}")  # output: fib(7) = 13
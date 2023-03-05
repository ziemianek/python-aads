"""

Question: How to find the sum of digits of a positive number using recursion?

Case:
    10  10/10 = 1 and remainder = 0
    1 + 0 = 1

    54  54/10 = 5 and remainder = 4
    5 + 4 = 9

    112 112/10 = 11 and remainder = 2
        11/10 = 1 and remainder = 1
    2 + 1 + 1 = 4

Solution:

"""

def sum_of_digits(n):
    assert n >=0 and int(n) == n, \
        "The number must be a non-negative interger only"
    if n == 0:
        return n
    else:
        return int(n % 10) + sum_of_digits(n // 10)

print(f"Sum of digits of 112 = {sum_of_digits(112)}")  # Output: Sum of digits of 112 = 4


"""

Question: How to calculate power of a number using recursion?

Case:
    x ** n = x * x * x * ...(n times)... * x
    x ** n = x * x ** (n - 1)

    2 ** 4 = 2 * 2 * 2 * 2 = 16

Solution:

"""

def power(base, exp):
    assert int(exp) == exp, "The exponent must be an integer"
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / base * power(base, exp + 1)
    else:
        return base * power(base, exp - 1)

print(f"2 ** 4 = {power(2, 4)}")  # Output: 2 ** 4 = 16


"""

Question: How to find GCD (Greatest Common Divisor) of two numbers using recursion?

GCD ---> the largest positive integer that divides the numbers without a remainder

Case:
    using Euclidean Algorithm:
    gdc(48, 18):
        Step 1: 48/18 = 2 remainder 12
        Step 2: 18/12 = 1 remainder 6
        Step 3: 12/6 = 2 remainder 0
    Thus, 6 is the GCD of 48 and 18
    
    gcd(a, 0) = a
    gcd(a, b) = gdc(b, a % b)

Solution:

"""

def gcd(a, b):
    assert int(a) == a and int(b) == b, \
        "Both numbers must be integers"

    a = -1 * a if a < 0 else a
    b = -1 * b if b < 0 else b

    return a if b == 0 else gcd(b, a % b)

print(f"GCD of 48 and 18 is {gcd(48, 18)}")  # Output: GCD of 48 and 18 is 6


"""

Question: How to convert a number from Decimal to Binary using recursion?

Case:
    Step 1: divide number 2
    Step 2: get the integer quotient for next iteration
    Step 3: get the remainder for the binary digit
    Step 4: repeat the steps until the quotient is equal to 0
    
    Example:
    10 to binary
    
    Division:    Quotient:   Remainder:
    10/2         5           0              
    5/2          2           1              101 * 10 + 0 = 1010 done
    2/2          1           0              10 * 10 + 1 = 101   up^
    1/2          0           1              1 * 10 + 0 = 10     up^

    So recursion will look like this: f(n) = n % 2 + 10 * f(n // 2)

Solution:

"""

def dec_to_bin(n):
    assert int(n) == n, \
        "The number must be an interger"
    if n == 0:
        return 0
    return n % 2 + 10 * dec_to_bin(n // 2)

print(f"10 in decimal in binary is {dec_to_bin(10)}")  # Output: 10 in decimal in binary is 1010
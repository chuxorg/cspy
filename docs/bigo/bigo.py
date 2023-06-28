# What is Big O Notation?
# Big O notation is a way of describing the performance of an algorithm.
# It's a way of describing how long an algorithm takes to run.
# It's a way of describing how much memory an algorithm uses.
# It's a way of describing how much space an algorithm uses.
# O stands for order of magnitude and "O" refers to the Greek letter "Omicron" and
# it's used to describe the worst case scenario of an algorithm. In this module, we'll
# cover the following Big O notations:
# O(1) - Constant Time
# O(n) - Linear Time
# O(n^2) - Quadratic Time
# O(n + n^2) - Quadratic Time
# O(log n) - Logarithmic Time
# There is another notation called O(n log n) - Linearithmic Time, but we won't cover it here.
# Typically, O(n log n) is considered to be a good algorithm in sorting algorithms.


# O(1) - Constant Time.
# This is constant time because it doesn't matter large n is
# it will always take the same amount of time to add n to itself.
# The number of operations is constant. Even if the algorithm were
# n + n + n, it is still constant time because the number of operations.
# This is the best case scenario for an algorithm, although it's rare.
def print_item_a(n):
    return n + n    
    
# O(n) - Linear Time. 
# Time complexity is O(n) because the number of operations 
# is directly proportional to the size of n.
# In other words, if n == 1 then the loop runs 1 time.
# If n == 10 then the loop runs 10 times. etc.
def print_items(n):    
    for i in range(n):
        print(i)

# O(n^2) - Quadratic Time.
# Time complexity is O(n^2) because the number of operations
# is directly proportional to the square of n.
def print_items_b(n):
    for i in range(n):
        for j in range(n):
            # printing n * n times OR n^2 times, so O(n^2)
            # O(n^2) is also called quadratic time and is generally 
            # considered to be a bad algorithm.
            print(i, j)

# O(n + n^2) - Quadratic Time.
# Time complexity is O(n^2) because the number of operations
# is directly proportional to the square of n.
# This is because the n^2 term "dominates" the n term.
# O(n + n^2) is aka: "dropping the constants". Because we drop the n term and
# only keep the n^2 term.
def print_items_c(n):
    for i in range(n):
        for j in range(n):
            # printing n * n times OR n^2 times, so O(n^2)
            # O(n^2) is also called quadratic time and is generally 
            # considered to be a bad algorithm.
            print(i, j)
            
    # printing n times, so O(n)
    # When done running, we have O(n^2 + n) which is O(n^2) because the n^2 term "dominates" the n term.
    # If n == 100 then the first loop runs 100 * 100 times (bad). 
    # The following second loop runs 100 times. The second loop is insignificant compared to the first loop.
    # So we can ignore it, for Big O purposes, and say that the time complexity is O(n^2). 
    # This is called "dropping the constants".
    for k in range(n):
        print(k)
    
 # O(log n) - Logarithmic Time.
 # Time complexity is O(log n) because the number of operations
 # is directly proportional to the log of n.
 # This is because the log n term "dominates" the n term.
 # O(log n) is also called logarithmic time and is generally
 # considered to be a good algorithm.
def print_numbers_c(n):
    # Consider the following array : | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
    # The goal is to find the number of times 
    # we can divide n by 2 until we get to 1.
    # If n == 8, then the loop runs 3 times. Because 8 / 2 / 2 / 2 == 1.
    for i in range(n):
        while i > 0:
            # // means integer division. So 5 // 2 == 2 (integer) while 5 / 2 == 2.5 (float/double)
            # essentially, drop the remainder. Which is what we want here.
            i = i // 2 
                       
            print(i)
    # What if n = 1,073,741,824? The loop runs 31 times. Because 2^31 =~ 1,073,741,824.
    # log n is the inverse of 2^n. So if 2^n == 1,073,741,824 then log n == 31. 31 operations is
    # far better than 1,073,741,824 operations. Or an "Order of Magnitude" better :) 
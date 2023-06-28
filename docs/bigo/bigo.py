# What is Big O Notation?
# Big O notation is a way of describing the performance of an algorithm.
# It's a way of describing how long an algorithm takes to run.
# It's a way of describing how much memory an algorithm uses.
# It's a way of describing how much space an algorithm uses.
# O stands for order of magnitude and "O" refers to the Greek letter "Omicron" and
# it's used to describe the worst case scenario of an algorithm.

# O(1) - Constant Time.
# This is constant time because it doesn't matter how many items are in the list.
# It will always take the same amount of time to print the first item in the list.
def print_first_item(items):    
    print(items[0])
    
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
    for k in range(n):
        print(k)
    # When done running, we have O(n^2 + n) which is O(n^2) because the n^2 term "dominates" the n term.
    # If n == 100 then the first loop runs 100 * 100 times. 
    # The second loop runs 100 times. The second loop is insignificant compared to the first loop.
    # So we can ignore it and say that the time complexity is O(n^2). This is called "dropping the constants".

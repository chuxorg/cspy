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

"""
Fibonacci sequence is a sequence of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.
the sum of the preceding two terms. 
e.g. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
"""

def fibA(n):
    """
        fibA is a recursive function that returns the nth number in the fibonacci sequence
        using brute force.
    Args:
        n (integer): The nth number in the fibonacci sequence.

    Returns:
        integer: The nth number in the fibonacci sequence.
    """
    # The first two numbers in the fibonacci sequence are 0 and 1.
    if n <= 1: return n
    if n <= 2: return 1
    # The nth number in the fibonacci sequence is the sum of the previous two numbers.
    # So, use recursion to get the sum of the previous two numbers.
    return fibA(n-1) + fibA(n-2)


def foo(n):
    """
    The fibA method uses brute force to get the nth number in the fibonacci sequence. When n is less than 10, fibA returns the correct value
    in a reasonable amount of time. However, when n is greater than 10, fibA gets slower and slower. At first glance, it seems like fibA is
    0(n). However, fibA is actually 0(2^n). This is because fibA calls itself twice for every n. To get the nth number in the fibonacci sequence.
    
    So, as n gets larger, fibA gets slower and slower. This is because fibA is doing a lot of redundant work. For example, to get the 7th number
    in the fibonacci sequence, fibA calls itself 13 times. However, fibA calls itself 5 times to get the 6th number in the fibonacci sequence.
    
    Essentially, this algorithm is returning the correct answer, but it is doing a lot of redundant work. To understand why, let's look at the
    the following few code examples.
    
    Args:
        n (integer): n (integer): The nth number in the fibonacci sequence.
    """
    if(n <= 1): return
    foo(n-1);
    

if __name__ == '__main__':
    print(fibA(7)) # 13
    foo(7) # 6
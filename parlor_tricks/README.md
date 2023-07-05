# Parlor Tricks

<img src="https://chuxorg.github.io/cspy/docs/logo.svg" height="30" width="30" align="left" style="margin-right:5px"/> Chuck Sailer  
July 5th, 2023

I call these algorithms parlor tricks because the mere mortal programmer will rarely run into a scenario where these 
algorithms are required in a day-to-day situation. BUT these algorithms provide good material to see Big O Notation in
action and re-enforce best practices for making algorithms more efficent. For interviewers, these algorithms are great assesment tools.

## Fibonacci Sequence
The Fibonacci series is a sequence of numbers where each number is the sum of the previous two.
This series has many real life applications, such as in nature, art, and mathematics.
In nature, Fibonacci numbers can be found in the arrangement of leaves on a stem or petals on a flower.
Artists often use Fibonacci sequences to create patterns in their work.
Mathematicians use Fibonacci numbers to study chaos theory and fractals.
Technical interviewers use Fibonacci to test the ability of a candidate to write algorithms effeciently.

```
def fib(n):
   """
   This is brute force Fibonacci. You'll get the right answer, eventually =).
   Time Complexity == O(2^n) # Exponential == Bad, Bad, Bad
   Space Complexity == O(n) # Linear == The best case is Meh. Worst case is bad, bad, bad.

   Note: Space complexity is measured by memory usage, disk space, and call stack. The call stack
   is the metric used in measuring O(n). The initial call is placed on the call stack and the subsequent
   recursive calls are also placed on the call stack. When a function returns, that function is removed
   from the call stack.
   """
   if n <= 2: return 1
   return fib(n-1) + fib(n-2)
```
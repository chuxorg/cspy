# Big O Notation

<img src="https://chuxorg.github.io/cspy/docs/logo.svg" height="30" width="30" align="left" style="margin-right:5px"/> Chuck Sailer  
July 2nd, 2023


Big O notation is a mathematical notation used in computer science to describe the performance or complexity of an algorithm. Specifically, it describes the worst-case scenario in terms of time or space complexity, as the size of the input data grows.

The "O" in Big O stands for "Order of", and it's used to classify algorithms based on how their run time or space requirements grow as the input size increases.

Here are some common Big O notations:

    - O(1): Constant time complexity. No matter how large the input data set is, the time (or space) taken by the algorithm does not change. An example is accessing an array element by its index.

    - O(n): Linear time complexity. The time (or space) taken grows linearly with the size of the input data set. An example is finding an item in an unsorted list.

    - O(log n): Logarithmic time complexity. The time (or space) taken increases logarithmically with the size of the input data set. An example is binary search.

    - O(n^2): Quadratic time complexity. The time (or space) taken grows quadratically with the size of the input data set. An example is a simple bubble sort algorithm.

    - O(2^n): Exponential time complexity. The time (or space) taken grows exponentially with the size of the input data set. An example is the naive recursive calculation of Fibonacci numbers.

Understanding Big O notation is crucial for evaluating the efficiency of algorithms, especially for large data sets. It allows us to estimate the time and space requirements of an algorithm as the input size grows, helping us choose the most efficient algorithm for a given task.
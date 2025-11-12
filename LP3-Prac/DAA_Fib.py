def fibonacci_recursive(n):
    # Base cases
    if n <= 1:
        return n
    # Recursive relation
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Driver code
n = int(input("Enter the number of terms: "))
print("Fibonacci sequence (Recursive):")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")

#time complexity of recursive fibonacci is O(2^n)
#space complexity of recursive fibonacci is O(n)




def fibonacci_iterative(n):
    a, b = 0, 1
    print("Fibonacci sequence (Iterative):")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


# Driver code
n = int(input("Enter the number of terms: "))
fibonacci_iterative(n)


#time complexity of iterative fibonacci is O(n)
#space complexity of iterative fibonacci is O(1)
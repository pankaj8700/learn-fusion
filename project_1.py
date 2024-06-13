# fibonacci function that returns the first n elements of the Fibonacci sequence
def fibonacci(n):
    if n <= 0:
        return "Input should be positive integer"
    elif n == 1:
        return [0]
    else:
        fib_sequence = [0, 1]
        for _ in range(n - 2):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

print(fibonacci(10))
# Uses python3
import sys

def get_fibonacci_last_digit(n):
    # write your code here
    if (n <= 1):
        return n
    fib_array = []
    fib_array.append(0)
    fib_array.append(1)
    for index in range(2,n + 1):
        fib_array.append((fib_array[index - 1] + fib_array[index - 2]) % 10)
    return fib_array[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))

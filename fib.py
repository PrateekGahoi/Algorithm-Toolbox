# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    fib_array = []
    fib_array.append(0)
    fib_array.append(1)
    for index in range(2,n + 1):
        fib_array.append(fib_array[index - 1] + fib_array[index - 2])
    return fib_array[n]

n = int(input())
print(calc_fib(n))

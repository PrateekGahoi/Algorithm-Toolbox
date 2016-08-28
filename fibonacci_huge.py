# Uses python3
import sys

def get_fibonacci_huge(n, m):
    # write your code here
    fib_huge_pattern = get_fibonacci_pattern(m)
    index = n % len(fib_huge_pattern)
    return fib_huge_pattern[index]

def get_fibonacci_pattern(m):
    # write your code here
    fib_list = [[]]
    fib_list.pop()
    fib_array = []
    last_no = 1
    sec_last_no = 0
    zero_count = 0
    fib_array.append(0)
    fib_array.append(1)
    while(1):
        new_no = (last_no + sec_last_no) % m
        sec_last_no = last_no
        last_no = new_no
        if new_no != 0:
            fib_array.append(new_no)
        elif new_no == 0 and zero_count == 0:
            fib_list.append(fib_array)
            fib_array = []
            fib_array.append(new_no)
            zero_count = 1
        else:
            if fib_list[0] == fib_array:
                break
            else:
                if len(fib_list[0]) == len(fib_array):
                    fib_list[0] = fib_list[0] + fib_array
                    fib_array = []
                fib_array.append(new_no)
    return fib_array 

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))

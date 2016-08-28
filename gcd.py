# Uses python3
import sys

def gcd(a, b):
    current_gcd = 1
    if b == 0:
        return a
    a_prime = a % b
    current_gcd = gcd(b, a_prime)

    return current_gcd

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))

# Uses python3
import sys

def lcm(a, b):
    #write your code here
    prod1 = (int)(b/gcd(a,b))
    return (a * prod1)

def gcd(a, b):
    current_gcd = 1
    if b == 0:
        return a
    a_prime = a % b
    current_gcd = gcd(b, a_prime)

    return current_gcd

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))


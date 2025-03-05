import sys
from itertools import groupby, combinations

# Implementing the Euclidean algorithm for finding GCDs:
# https://sites.math.rutgers.edu/~greenfie/gs2004/euclid.html
# Find the GCD of (210,45)
# Example of the algorithm in practice:
# 210 / 45 => 4 * 45 + 30 => Feed 45 and 30 into next step
# 45 / 30  => 1 * 30 + 15 => Feed 30 and 15 into next step
# 30 / 15  => 2 * 15 + 0  => End algorithm because remainder = 0

# Generally, this means we take the first number A, divided it by B a number of times, and get the remainder (A mod B <=> A%B). This is equivalent to A = (A//B)*B + A%B. We pull out the remainder, R, and the smaller number B. If A < B, then they do automatically reverse in the algorithm to make sure A > B.
# For the algorithm, we are going to do a recursion. If the remainder is not zero, then we will repeat this step with B and the remainder.

def gcd(A,B):
    R = A%B
    if R != 0:
        return gcd(B,R)
    else:
        return B

def main():
    cases = int(sys.stdin.readline().rstrip())
    for caseNum in range(cases):
        data = sys.stdin.readline().rstrip()
        numbers = [int(''.join(y)) for x,y in groupby(data, lambda x: x.isdigit()) if x]
        if all(gcd(x,y) == 1 for x,y in combinations(numbers, 2)):
            print("TRUE")
        else:
            print("FALSE")
        
if __name__ == "__main__":
    main()

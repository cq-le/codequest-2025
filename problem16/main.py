import sys
from test import get_reciprocal_digits, find_cycle_start, CycleError

def main():
    cases = int(sys.stdin.readline().rstrip())
    for caseNum in range(cases):
        n = int(sys.stdin.readline().rstrip())
        D = len(str(n))  # length of the initial division
        Q = 10**D//n    # first digit of the division
        R = 10**D % n   # remainder after division
        # Creates a generator object.
        digit_generator = get_reciprocal_digits(n, Q, R)
        # Initializes the digits with the proper place value
        digits = f'{"0"*(D-1)}'
        # Generates the first 2*(n-1)+n digits of the number to ensure we have enough digits for finding a cycle
        for _ in range(2*(n-1)+n):
            try:
                # Next method is called on the digit generator to generate the next digit
                digits += str(next(digit_generator))
            # Exception raised when there are no more divisions, so we break out of this loop.
            except StopIteration:
                break
            except CycleError:
                print("Cycle detected!")
                break
        print(n, find_cycle_start(digits), digits)

if __name__ == "__main__":
    main()
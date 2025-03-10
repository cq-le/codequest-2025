from functools import cache

# Long division with a reciprocal works as follows:
# 7 | 1.000... -> We have a divisor (n=7), a dividend (d=1.000...), and it results in a quotient (Q) and a remainder (R).
# We are interested in generating the digits of Q.
# Because of the repeating zeroes, we are essentially working with 10 (or multiples of it) by multiplying and subtracting off of it.
# Because of how the algorithm repeats, we can use recursion to yield digits.

# Ex: 1/13
# First division:   100/13 => 11Q + R: Q=7, R=9
# Second division:  90/13  => 11Q + R: Q=6, R=12
# Third division:  120/13  => 11Q + R: Q=9, R=3
# Fourth division: 30/13   => 11Q + R: Q=2, R=4
# Fifth division:  40/13   => 11Q + R: Q=3, R=1
# ...
# Generally:      10*R/n   => 11Q + R: Q=(10*R)//n, R=10*R % n

# Step 1a: Determine the first division. This requires that we know how many digits (D) are in n - we can use len(n) to get that.
#          Then, the first division is (10**D)/n. In the above case, we had D=2, so our first division was 100/13.
# Step 1b: The first digit of this division is however many times n can fit into 10**D - mathematically expressed, we can figure that out by using the expression x = 10**D//n.
#          The floor division allows us to discard the decimal portion of a division and only keep the integer part.
#          The remainder can be calculated using the modulus operation, R = 10**D % n.
#          In the above case, we had 100//13 and 100 % 13 which gave us Q=7 and R=9.
#          This will be the first remainder and quotient we feed into the algorithm, so we start off with (n,Q,R) = (13,7,9)
# Step 1c: If the remainder is 0, then that means there are no more digits to be yielded, so we should terminate the algorithm.

# Step 2: Calculate the next division.
#         Carrying down 0 in a long division is the equivalent of multiplying the remainder by 10. So, we have 10*R/n as our next division.
#         Again, we can get Q and R using the expressions above, so Q = 90//13 = 6, and R = 90 % 13 = 12.
#         Feed (13,6,12) into the next step of the algorithm
# Step 3: ...
#         ...Recursively, we are yielding Q and then calling the algorithm again.

# Now, we can create a generator function. Generators can have the function next() applied to them to to calculate the next item in a sequence without having to precompute the digits beforehand.
# This is useful in this case because we don't know how many digits a cycle will take, only that it cannot have a length greater than the number itself.


def get_reciprocal_digits(n, Q, R):
    quotient = 10*R // n
    remainder = 10*R % n
    yield Q
    if R == 0:
        return StopIteration
    else:
        yield from get_reciprocal_digits(n, quotient, remainder)


# Cycle detection algorithm: Floyd's Tortoise and Hare
# https://visualgo.net/en/cyclefinding
# The way this algorithm works is that it has two pointers which traverse a graph at different rates: one going 1 point at a time, and another going 2 points at a time. 
# Because of the difference in speed, if there is a cycle, at some point the tortoise and hare will meet again. 
# You can then figure out where the cycle starts by making the tortoise and the hare traverse towards each other at equal rates. 
# There's a lot of theoretical discussion about how this algorithm works, which we won't have to worry about here.
# For example, consider the following graph for 1/14:
#          1 -> 4
#        /       \
# 0 -> 7          2
#       \        /
#        5  <- 8
# The pointers would traverse the graph with the following numbers:
# Tortoise: [0, 7, 1, 4, 2, 8, (5)] -> Cycle detected -> [0, (7)] -> Cycle starts at 7 (or index position 1)
# Hare:     [0, 1, 2, 5, 1, 2, (5)] -> Cycle detected -> [5, (7)]
# Another example: consider 1/17
#     5 -> 8 -> 8 -> 2 -> 3 -> 5 -> 2
#   /                                \
# 0                                  9
#  \                                /
#   7 <- 4 <- 6 <- 7 <- 1 <- 1 <- 4
# Tortoise: [0,5,8,8,2,3,5,2,9,4,1,1,7,6,4,7,(0)] -> Cycle detected -> [(0)] -> Cycle starts at 0 (or index position 0)
# Hare:     [0,8,2,5,9,1,7,4,0,8,2,5,9,1,7,4,(0)] -> Cycle detected -> [(0)]
for n in range(2, 20):
    D = len(str(n))  # length of the initial division
    Q = 10**D//n    # first digit of the division
    R = 10**D % n   # remainder after division
    # Creates a generator object.
    digit_generator = get_reciprocal_digits(n, Q, R)
    # Initializes the digits with the proper place value
    digits = f'{"0"*(D-1)}'
    # Generates the first 2*(n-1) digits of the number to ensure we have enough digits for finding a cycle
    for _ in range(2*(n-1)):
        try:
            # Next method is called on the digit generator to generate the next digit
            digits += str(next(digit_generator))
        # Exception raised when there are no more divisions, so we break out of this loop.
        except StopIteration:
            break
    print(n, digits)

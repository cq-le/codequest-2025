# Long division with a reciprocal works as follows:
# 7 into 1.00000... => 
# Step 0: Notice, because of the repeating zeroes, we are essentially working with 10 (or multiples of it) by multiplying and subtracting off of it. Because of how it repeats, we can use recursion to yield digits.
# Feed (7,10,(10**D-7)) into the algorithm as the initial step. 7 is the number we are interested in dividing into 1. We get a quotient (Q) and a remainder (R). The 10**D represents the number of decimal places we need to go to to allow us to actually divide (ex: 11 needs 100 to first start dividing because it has 2 digits). 
# Step 1: 10*R - (7 x Q) : n=7, Q=1, R=3   | generally, 10*R1 - (n*Q) = R2 => Q = (10*R1 - R2)/n
# Step 2: 10*R - (7 x Q) : n=7, Q=4, R=2
# Step 3: 10*R - (7 x Q) : n=7, Q=2, R=6
# Step 4: ...
# Generalizing, we are feeding the remainder into the long division algorithm and returning D.
def get_reciprocal_long_division_digits(n,Q,R):
    if R == 0:
        raise StopIteration
    else:
        quotient = 
        yield 


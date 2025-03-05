import sys

def main():
    cases = int(sys.stdin.readline().rstrip())
    for caseNum in range(cases):
        bits = int(sys.stdin.readline().rstrip())
        max_number = 2 ** bits - 1 #bits tell you how many binary digits are needed to represent the number. A single bit can only be 0 or 1. To calculate the maximum number of bits, you can figure out how many numbers are possible using just 0 or 1.
        #ex: 5 bits 
        #-> 2 options for the 1st bit, 2 options for the 2nd bit, etc.
        #-> total: 2 x 2 x 2 x 2 x 2 = 2 ** 5
        #Another way of thinking about this is in terms of binary digits - every place value in a binary digit represents a power of two. Adding together all powers of two from 2^0 to 2^number of bits gives you the maximum number.
        data = [int(x) for x in sys.stdin.readline().rstrip().split(" ")]
        if all(x <= max_number for x in data):
            print(f"{max_number} TRUE")
        else:
            print(f"{max_number} FALSE")
        
if __name__ == "__main__":
    main()
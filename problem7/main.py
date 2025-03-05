import sys

def main():
    cases = int(sys.stdin.readline().rstrip())
    for caseNum in range(cases):
        bits = int(sys.stdin.readline().rstrip())
        max_number = 2 ** bits
        data = [int(x) for x in sys.stdin.readline().rstrip().split(" ")]
        if all(x < max_number for x in data):
            print(f"{max_number - 1} TRUE")
        else:
            print(f"{max_number - 1} FALSE")
        
if __name__ == "__main__":
    main()
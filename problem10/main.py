import sys
from functools import reduce

def main():
    cases = int(sys.stdin.readline().rstrip())
    for caseNum in range(cases):
        number_of_protocols = int(sys.stdin.readline().rstrip())
        requirements = sys.stdin.readline().rstrip().split(",")
        tests = reduce(lambda x,y: x+y, [sys.stdin.readline().rstrip().split(",")[1:] for _ in range(number_of_protocols)])
        #reduce(lambda x,y: x+y, array) combines all items from one array into a single value by adding them together. In this case, an array of arrays was generated through the .split(",") method, and needs to be collapsed into one array.
        #[1:] skips the first entry and returns an array containing the rest of the entries. We skip the first entry because it just identifies what protocol we are working with.
        missed_requirements = [requirement for requirement in requirements if requirement not in tests]
        if missed_requirements: #empty lists are falsy
            print(','.join(missed_requirements))
        else:
            print("FULL COVERAGE")


if __name__ == "__main__":
    main()
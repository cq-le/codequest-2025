import sys
from collections import Counter

def main():
    cases = int(sys.stdin.readline().rstrip())
    assignments = {}
    hours = Counter({})
    for caseNum in range(cases):
        T, E = [int(x) for x in sys.stdin.readline().rstrip().split(" ")] # T: number of tasks, E: number of actions
        for _ in range(T):
            task, employee = sys.stdin.readline().rstrip().split(":")
            assignments[task] = employee
        for _ in range(E):
            task, time = sys.stdin.readline().rstrip().split(":")
            time = float(time)
            hours += Counter({assignments[task]: time})
    hours = {int(x): round(y, 1) for x,y in hours.items()}
    hours = {k:v for k,v in sorted(hours.items(), key=lambda item: item[0])}
    print(hours)

        




if __name__ == "__main__":
    main()
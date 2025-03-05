import sys

def main():
    cases = int(sys.stdin.readline().rstrip())
    for caseNum in range(cases):
        number_of_weeks = int(sys.stdin.readline().rstrip())
        total_hours_worked = 0
        for week in range(number_of_weeks):
            data = sys.stdin.readline().rstrip()
            week_hours = sum([int(x) for x in data.split(" ")])
            #using list comprehension - a way to compress a loop into a list. 
            #data.split(" ") splits all items inside of the data by spaces, and accumulates them into an array. Each item in the array is a string, so you will need to cast its type to int.
            # The built-in sum function allows you to add all items inside of a list.
            total_hours_worked += week_hours
        print(total_hours_worked - 40)

if __name__ == "__main__":
    main()
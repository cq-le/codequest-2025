import sys

def average(numbers):
    return sum(numbers)/len(numbers)

def main():
    cases = int(sys.stdin.readline().rstrip())
    for caseNum in range(cases):
        config_data = sys.stdin.readline().rstrip().split(" ")
        sensor_data = sys.stdin.readline().rstrip().split(" ")
        readings, L, A, H = [int(x) if i == 0 else float(x) for i,x in enumerate(config_data)]
        sensor_data = [float(x) for x in sensor_data]
        #We are using data destructuring - a way to assign variables in one line to a list of known size (in this case, 4)
        #For example: x,y = (1,2) assigns x to 1, and y to 2
        #We are using a condition inside of our list comprehension by using if/else after the expression.
        #enumerate allows you to access the indices of an array while iterating.
        if any(temp < L for temp in sensor_data):
            #any allows you to check every item inside of an array for a condition. If any fail, the entire check fails.
            #all is a related built-in function - If all succeed, the entire check succeeds.
            print("TOO COOL")
        elif any(temp > H for temp in sensor_data):
            print("TOO HOT")
        elif average(sensor_data) > A:
            print("WARNING")
        else:
            print("OK")

if __name__ == "__main__":
    main()
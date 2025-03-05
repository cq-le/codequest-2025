import sys
from functools import reduce

def process(data):
    valid_numbers = [32, 44, 46, 58, 91, 93] + [x for x in range(48,58)] + [x for x in range(65,91)] + [x for x in range(97, 123)] 
    #add together lists to combine specific symbols and ranges

    data = [int(x, 16) for x in data.split(" ")] #using list comprehension - a way to compress a loop into a list
    #int(N, B) converts any number in base B to a number in base 10

    map_valid = list(map(lambda x: x in valid_numbers, data)) 
    #map applies a function to every item inside of a list. the function is known as a "lambda" - a way to create a function specifically for the map. In this case, it is checking to see if each item is inside of the valid numbers array. It must then be cast into a list.

    is_valid = reduce(lambda x,y: x and y, map_valid)
    #reduce collapses a list into one accumulated value using the function inside. Another way to look at it is that it takes the first two items in the list and does something to them until there is only one item in the list. 
    # In this example, if our list is [True, True, True, True, False], it would apply the following steps:
    #      x      y                          x and y
    #1: [(True, True), True, True, False] -> [True, True, True, False]
    #      x      y                          x and y
    #2: [(True, True), True, False]       -> [True, True, False]
    #      x      y                          x and y
    #3: [(True, True), False]             -> [True, False]
    #      x      y                          x and y
    #4: [(True, False)]                   -> [False]
    #Return: False
    #We use x AND y instead of x OR y because we need to check if *all* items in the list are true. OR would be useful if we need to check if *any* item is true.
    #There are also built in functions for doing this
    # all() -> Checks if all items in the list are True or are truthy
    # any() -> Checks if any item in the list is True or is truthy


    if is_valid:
        print("VALID")
    else:
        print("INVALID")
    

def main():
    cases = int(sys.stdin.readline().rstrip())
    for caseNum in range(cases):
        data = sys.stdin.readline().rstrip()
        process(data)

if __name__ == "__main__":
    main()
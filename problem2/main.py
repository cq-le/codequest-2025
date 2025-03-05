import sys
from itertools import product #useful for this problem

def get_possible_numbers(numbers):
    array = []
    for number1, number2 in product(numbers, repeat=2): 
        #goes through two-number pairs. 
        #Ex: [1,2,3] ->
        #((1,1),(1,2),(1,3),
        # (2,1),(2,2),(2,3),
        # (3,1),(3,2),(3,3))    
        if number1 == number2: #skips AA, BB, CC, etc. Cards are guaranteed to be unique, so we don't have to worry about cases such as [1,1,2] giving 11 as one of the options.
            continue
        array.append(str(number1)+str(number2)) #casting into string to combine the symbols. You could also multiply one number by 10 and add it to the other number.
    array = set(array) #removes repeats
    array = sorted(array) #sorts the array
    return array

def process(numbers):
    numbers = [int(x) for x in numbers.split(" ")]
    #using list comprehension - a way to compress a loop into a list. 
    #data.split(" ") splits all items inside of the data by spaces, and accumulates them into an array. Each item in the array is a string, so you will need to cast its type to int.
    # The built-in sum function allows you to add all items inside of a list.
    length = len(numbers)
    player1_nums = numbers[0:length//2]
    player2_nums = numbers[length//2:]
    #Here we are using list slicing. L[I:J] returns a list that includes all items from index I (inclusive) to index J (exclusive). 
    # Index J in this case is half of the length of the list (using // to make sure it is an integer).
    #For player2_nums, we only specified I - Python automatically makes J the end of the list if not specified.

    player1_nums = get_possible_numbers(player1_nums)
    player2_nums = get_possible_numbers(player2_nums)
    player1_max_num = int(player1_nums[-1]) #negative indexing to get last item
    player2_max_num = int(player2_nums[-1])
    if player1_max_num > player2_max_num:
        print("PLAYER 1")
    elif player2_max_num > player1_max_num:
        print("PLAYER 2")
    else:
        print("WAR!")

def main():
    cases = int(sys.stdin.readline().rstrip())
    for caseNum in range(cases):
        numbers = sys.stdin.readline().rstrip()
        process(numbers)

if __name__ == "__main__":
    main()
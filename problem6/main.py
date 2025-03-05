import sys
from itertools import groupby

def main():
    cases = int(sys.stdin.readline().rstrip())
    for caseNum in range(cases):
        data = sys.stdin.readline().rstrip()
        message = ''
        for isNumber, characters in groupby(data, lambda x: x.isdigit()):
            #groupby is a function from itertools which returns arrays of checks and characters that splits up the data according to its condition - in this case, if the character is a numerical digit. Here we used a lambda function to avoid having to write a separate number checker function. 
            #Ex: "aaa123bb456" -> 
            # (False, ['a', 'a', 'a']), <- False because these are not digits
            # (True, ['1', '2', '3']),  <- True because these are digits
            # (False, ['b', 'b']),      <- False because these are not digits
            # (True, ['4', '5', '6'])   <- True because these are digits
            string = ''.join(characters) #Join collects all items inside of an array and collapses them into the string it is joining to - in this case, an empty string
            if isNumber:
                number = int(string)
                message += chr(number + 64) #chr is a function which returns the Unicode character at that point. The ASCII letter 'A' starts at Unicode point 65, and since A = 1, we need to add 64 to the number.
            else:
                continue
        print(message)
            

if __name__ == "__main__":
    main()
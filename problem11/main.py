import sys
import re
from collections import Counter

def is_anagram(word1, word2):
    #Sanity check - if the lengths are different or the words are the same, it can't be an anagram
    if len(word1) != len(word2) or word1 == word2:
        return False
    
    letter_count1 = Counter({}) # Using collection's Counter - allows you to add dictionaries together easily without having to initialize the dictionary to begin with
    letter_count2 = Counter({})
    for i in range(len(word1)):
        letter_count1 += Counter({word1[i]: 1}) # Add 1 to the corresponding letter in the dictionary
        letter_count2 += Counter({word2[i]: 1})
    if letter_count1 == letter_count2:
        return True
    else:
        return False

def main():
    cases = int(sys.stdin.readline().rstrip())
    for caseNum in range(cases):
        data = sys.stdin.readline().rstrip()
        regex_pattern = '\[(\d+,\d+)\] \"(.+)\" \"(.+)\"'
        # This is a Regular Expression (regex) pattern. This pattern helps us capture data from a string by matching it to a pattern using this peculiar notation.
        # When you see \ in front of a symbol, it means to take it literally as that character. \[ and \] therefore mean "Look for the symbols [ and ] exactly as they are not part of the regular expression."
        # The (...) allows us to group patterns together for later lookup, called captures. In this case, our pattern looks like the following:
        # [(...)] "(...)" "(...)" - A capture within the brackets, a capture within two quotation marks, and another capture within two quotation marks.
        # Inside the brackets, the capture pattern is \d+,\d+
        # \d stands for any number 0-9, and the + stands for "any length sequence of" - together, it reads "any length sequence of numbers followed by a comma followed by any length sequence of numbers".
        # Inside the quotation marks, the capture pattern is .+
        # . stands for any character, so this capture pattern reads as "any length sequence of any character"
        match = re.match(regex_pattern, data) # Creates a match object which has useful methods for accessing the patterns within a string
        array, sentence1, sentence2 = match.group(1), match.group(2), match.group(3) # Assigns each of the capture groups to a variable
        index1, index2 = [int(x) for x in array.split(",")]
        word1, word2 = sentence1.split(" ")[index1 - 1], sentence2.split(" ")[index2 - 1] # -1 on index because the numbering starts from 1 but Python starts from 0
        if is_anagram(word1, word2):
            print("Verified")
        else:
            print("Intercepted")
        
if __name__ == "__main__":
    main()
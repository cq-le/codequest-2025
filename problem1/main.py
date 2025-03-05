import sys

def process(text):
    if "red" in text:
        print("red")
    elif "blue" in text:
        print("blue")
    else:
        print("no color found")

def main():
    cases = int(sys.stdin.readline().rstrip())
    #Here, we are processing each line one by one. sys.stdin takes in data from an external source.
    # .readline() consumes one line of the data and returns a copy of the data as a string.
    # .rstrip() removes any trailing whitespace at the end of the string - in this case, any new line characters.
    # In order to use this file, you must be in a command line terminal and input the following commands in sequence:
    #cd problem1
    #python main.py < input.txt
    #This says to the terminal, "Enter the problem 1 folder. Then, run the python file main.py using the language Python, and pipe the data from input.txt into the file."
    for caseNum in range(cases):
        text = sys.stdin.readline().rstrip()
        process(text)
        #Here, we wrote a custom function to help us answer the question. This function should be written before the main() function.

if __name__ == "__main__":
    main()
    #This syntax here is preferred because we may need to write multiple files to help us solve these problems. We are ensuring that only this file is responsible for running the program, and that any other files are just resources for us to use.
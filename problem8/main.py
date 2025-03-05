import sys

#Classes are useful when you want to keep track of state - it's not necessary to this problem but it makes it easier to reason with when things get complicated.
class Robot:
    def __init__(self, x, y, direction):
        #The __init__ method of a class provides meaningful state information of your object. It is the first method of a class when you construct the object, meaning we will need to provide the x, y, and direction when we create this robot.
        #The self keyword allows you to modify only one particular instance of a robot instead of all robots.
        self.x = int(x)
        self.y = int(y)
        self.direction = direction
    
    def turn_left(self):
        #These are methods of the robot - functions which, when called, do something to the robot. In this case, it is changing direction.
        self.direction = "N" if self.direction == "E" else\
                         "W" if self.direction == "N" else\
                         "S" if self.direction == "W" else\
                         "E" if self.direction == "S" else None
        #Here we are using ternary conditionals to help us condense code. It essentially chains together a lot of conditionals in an alternate format to using if/elif/else.
    def turn_right(self):
        self.direction = "S" if self.direction == "E" else\
                         "E" if self.direction == "N" else\
                         "N" if self.direction == "W" else\
                         "W" if self.direction == "S" else None
    def advance(self):
        if self.direction == "N":
            self.y += 1
        elif self.direction == "S":
            self.y += -1
        elif self.direction == "E":
            self.x += 1
        elif self.direction == "W":
            self.x += -1 

def main():
    cases = int(sys.stdin.readline().rstrip())
    for caseNum in range(cases):
        data = sys.stdin.readline().rstrip()
        x, y, direction, instructions = data.split(" ")
        robot = Robot(x, y, direction)
        for instruction in instructions:
            if instruction == "R":
                robot.turn_right()
            elif instruction == "L":
                robot.turn_left()
            elif instruction == "A":
                robot.advance()
            else:
                pass
        print(f"{robot.x} {robot.y} {robot.direction}")

if __name__ == "__main__":
    main()
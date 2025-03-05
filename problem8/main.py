import sys

class Robot:
    def __init__(self, x, y, direction):
        self.x = int(x)
        self.y = int(y)
        self.direction = direction
    
    def turn_left(self):
        self.direction = "N" if self.direction == "E" else\
                         "W" if self.direction == "N" else\
                         "S" if self.direction == "W" else\
                         "E" if self.direction == "S" else None
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
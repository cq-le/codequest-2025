import sys

def find_last_position(array):
    for index, element in enumerate(reversed(array)):
        if element != "":
            return len(array)-index-1
    return None

class Buffer:
    def __init__(self, size):
        self.size = size
        self.pointer = 0
        self.array = ["" for i in range(self.size)]
    
    def set_pointer(self, position):
        self.pointer = position
    
    def add(self, values):
        print(f"Adding: {values}")
        for value in values:
            self.array[self.pointer] = value
            self.pointer = (self.pointer + 1) % self.size
    
    def consume(self, value):
        print(f"Consuming {value} characters")
        if value > self.size:
            self.pointer = find_last_position(self.array)
            self.array = ["" for i in range(self.size)]
        else:
            for _ in range(value):
                self.array[self.pointer] = ""
                self.pointer = (self.pointer + 1) % self.size
    
    def show(self):
        print("Showing")
        count_buffer_values = sum(1 for x in self.array if x != "")
        last_character_position = find_last_position(self.array)
        midpoint = (self.pointer + last_character_position)//2
        if count_buffer_values == 0:
            print("EMPTY")
        elif count_buffer_values % 2 == 0:
            print(self.array[midpoint])
        elif count_buffer_values % 2 == 1:
            print(' '.join(self.array[midpoint-1] + self.array[midpoint+1]))
    
def main():
    cases = int(sys.stdin.readline().rstrip())
    for caseNum in range(cases):
        num_commands, buffer_size = [int(x) for x in sys.stdin.readline().rstrip().split(" ")]
        buffer = Buffer(buffer_size)
        for _ in range(num_commands):
            instruction, *data = sys.stdin.readline().rstrip().split(" ")
            if instruction == "ADD":
                buffer.add(data)
            elif instruction == "SHOW":
                buffer.show()
            elif instruction == "CONSUME":
                buffer.consume(int(data[0]))
            print(buffer.array)

if __name__ == "__main__":
    main()
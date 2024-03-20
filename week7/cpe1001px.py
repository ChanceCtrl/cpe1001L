# Std lib imports
import sys
from enum import Enum

# Pi sense hat import
from sense_hat import SenseHat


# These represent the instruction set, add some more here
class fCalls(Enum):
    # A value to associate with text
    MOVE = 0
    LOAD = 1
    STORE = 2
    ADD = 3
    SUBTRACT = 4
    MULTIPLY = 5
    DIVIDE = 6


# Some defs for images, Just change the O's to G or R to make LEDs light up
def check_mark():
    G = (0, 255, 0)
    img = [G] * 64

    return img


def red_x():
    R = (255, 0, 0)
    img = [R] * 64

    return img


def main():
    # Gets file name from cli
    file_name = sys.argv[1]

    # Init the boi
    my_hw = ALU()

    ops = load_file(file_name)

    if not ops:
        # Display that there was an error loading the file
        my_hw.has_error = True
        my_hw.display
    else:
        for op in ops:
            match op[0]:
                case fCalls.MOVE:
                    # Set register equal to int
                    my_hw.regs[op[1]] = op[2]
                case fCalls.LOAD:
                    # Load from memory into reg
                    my_hw.regs[op[1]] = my_hw.data[op[2]]
                case fCalls.STORE:
                    # Store reg into memory
                    my_hw.data[op[2]] = my_hw.regs[op[1]]
                case fCalls.ADD:
                    # Add two regs together into another reg
                    my_hw.regs[op[3]] = my_hw.regs[op[1]] + my_hw.regs[op[2]]
                case fCalls.SUBTRACT:
                    my_hw.regs[op[3]] = my_hw.regs[op[1]] - my_hw.regs[op[2]]
                case fCalls.MULTIPLY:
                    my_hw.regs[op[3]] = int(my_hw.regs[op[1]] * my_hw.regs[op[2]])
                case fCalls.DIVIDE:
                    my_hw.regs[op[3]] = int(my_hw.regs[op[1]] / my_hw.regs[op[2]])

        # Return display info if everything
        my_hw.print_tables()
        my_hw.display


# This represents the "raw hardware"
class ALU:
    # The actual arrays for memory
    regs = [0] * 5
    data = [0] * 10

    # Bool for if there was an error
    has_error = False

    # I hate python printing and I hate that I couldn't clean this up in time
    def print_tables(self):
        # Table
        r = "+-----------+\n| REGISTERS |\n| R0: PR0     |\n| R1: PR1     |\n| R2: PR2     |\n| R3: PR3     |\n| R4: PR4     |\n+-----------+"

        # Replace with actual data in the worst way possible
        r = r.replace("PR0", str(self.regs[0]))
        r = r.replace("PR1", str(self.regs[1]))
        r = r.replace("PR2", str(self.regs[2]))
        r = r.replace("PR3", str(self.regs[3]))
        r = r.replace("PR4", str(self.regs[4]))

        # Return table
        print(r)

        # Table
        m = "+--------+-------+\n| MEMORY |       |\n| D0: PD0  | D1: PD1 |\n| D2: PD2  | D3: PD3 |\n| D4: PD4  | D5: PD5 |\n| D6: PD6  | D7: PD7 |\n| D8: PD8  | D9: PD9 |\n+--------+-------+"

        # Replace with actual data in the worst way possible
        m = m.replace("PD0", str(self.data[0]))
        m = m.replace("PD1", str(self.data[1]))
        m = m.replace("PD2", str(self.data[2]))
        m = m.replace("PD3", str(self.data[3]))
        m = m.replace("PD4", str(self.data[4]))
        m = m.replace("PD5", str(self.data[5]))
        m = m.replace("PD6", str(self.data[6]))
        m = m.replace("PD7", str(self.data[7]))
        m = m.replace("PD8", str(self.data[8]))
        m = m.replace("PD9", str(self.data[9]))

        # Return table
        print(m)
        return

    def display(self):
        # Init sense hat
        s = SenseHat()
        s.low_light = True

        if self.has_error:
            s.set_pixels(red_x)
        else:
            s.set_pixels(check_mark)


def load_file(file_name: str):
    # Open the file with read perms
    file = open(file_name, "r")
    Lines = file.readlines()

    # Make a list of ops
    ops = []

    for line in Lines:
        # Split up line based on whitespace
        split_line = line.split(" ")

        # Sanitize commas and /n
        for val in range(len(split_line)):
            split_line[val] = split_line[val].replace(",", "")
            split_line[val] = split_line[val].replace("\n", "")

        # Get function
        match split_line[0]:
            case "MOVE":
                # Sanitize
                rx = split_line[1].replace("R", "")

                # Append to list
                ops.append([fCalls.MOVE, int(rx), int(split_line[2])])
            case "LOAD":
                # Sanitize
                rx = split_line[1].replace("R", "")
                ry = split_line[2].replace("R", "")
                ry = ry.replace("[", "")
                ry = ry.replace("]", "")

                # Append to list
                ops.append([fCalls.LOAD, int(rx), int(ry)])
            case "STORE":
                rx = split_line[1].replace("R", "")
                dy = split_line[2].replace("D", "")
                dy = dy.replace("[", "")
                dy = dy.replace("]", "")

                # Append to list
                ops.append([fCalls.STORE, int(rx), int(dy)])
            case "ADD":
                rx = split_line[1].replace("R", "")
                ry = split_line[2].replace("R", "")
                rz = split_line[3].replace("R", "")
                ops.append([fCalls.ADD, int(rx), int(ry), int(rz)])
            case "SUBTRACT":
                rx = split_line[1].replace("R", "")
                ry = split_line[2].replace("R", "")
                rz = split_line[3].replace("R", "")
                ops.append([fCalls.SUBTRACT, int(rx), int(ry), int(rz)])
            case "MULTIPLY":
                rx = split_line[1].replace("R", "")
                ry = split_line[2].replace("R", "")
                rz = split_line[3].replace("R", "")
                ops.append([fCalls.MULTIPLY, int(rx), int(ry), int(rz)])
            case "DIVIDE":
                rx = split_line[1].replace("R", "")
                ry = split_line[2].replace("R", "")
                rz = split_line[3].replace("R", "")
                ops.append([fCalls.DIVIDE, int(rx), int(ry), int(rz)])

            case _:
                # Return flase if invalid instruction is passed
                return False

    # Return Ops on success
    return ops


# Run main
main()

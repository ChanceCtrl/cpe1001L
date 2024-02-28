# Std lib imports
import sys
from enum import Enum

# Pi sense hat import
# from sense_hat import SenseHat


def main():
    # Gets file name from cli
    file_name = sys.argv[1]

    # Returns list of ops
    open_file(file_name)

    # Init the boi
    x = fCall
    x.print_tables

    # Run the code

    # Return display info if it worked
    # x.display


def open_file(file_name):
    # Open the file with read perms
    file = open(file_name, "r")
    Lines = file.readlines()

    for line in Lines:
        # Split up line based on whitespace
        split_line = line.split(" ")

        # Remove any commas
        for val in split_line:
            val = val.replace(",", "")


class fCall:
    # The actual arrays for memory
    regs = [0] * 5
    data = [0] * 10

    # Add more functions here
    class call(Enum):
        MOVE = 0
        LOAD = 1
        STORE = 2
        ADD = 3

    # This handles any registers we may have to work with
    r1 = 0
    r2 = 0
    r3 = 0
    d = 0

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

    # def display(self):
    #     # Init sense hat
    #     s = SenseHat()
    #     s.low_light = True
    #
    #     if self.has_error:
    #         s.set_pixels(red_x)
    #     else:
    #         s.set_pixels(check_mark)


# Some defs for images, Just change the O's to G or R to make LEDs light up
def check_mark():
    G = (0, 255, 0)
    O = (0, 0, 0)

    # img = [
    # O, O, O, O, O, O, O, O,
    # O, O, O, O, O, O, O, O,
    # O, O, O, O, O, O, O, O,
    # O, O, O, O, O, O, O, O,
    # O, O, O, O, O, O, O, O,
    # O, O, O, O, O, O, O, O,
    # O, O, O, O, O, O, O, O,
    # O, O, O, O, O, O, O, O,
    # ]

    # return img


def red_x():
    R = (255, 0, 0)
    O = (0, 0, 0)

    # img = [
    # O, O, O, O, O, O, O, O,
    # O, O, O, O, O, O, O, O,
    # O, O, O, O, O, O, O, O,
    # O, O, O, O, O, O, O, O,
    # O, O, O, O, O, O, O, O,
    # O, O, O, O, O, O, O, O,
    # O, O, O, O, O, O, O, O,
    # O, O, O, O, O, O, O, O,
    # ]

    # return img


# Run main
main()

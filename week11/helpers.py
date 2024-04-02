from time import sleep

# Color defs
R = [255, 0, 0]
B = [0, 0, 255]
Y = [255, 255, 0]
W = [255, 255, 255]


def dis_thing(sh):
    make_logo(sh, R)  # Display RED
    sleep(1)
    make_logo(sh, B)  # Display BLUE
    sleep(1)
    make_logo(sh, Y)  # Display YELLOW
    sleep(1)
    make_logo(sh, W)  # Display WHITE
    sleep(1)


# Lol my linter really hates this guy
def make_logo(sh, p):
    logo = [
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
        p,
    ]
    sh.set_pixels(logo)

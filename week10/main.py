import time
import sys

from sense_hat import SenseHat

if __name__ == "__main__":
    # Get time stuffs
    log_time = 60
    t_end = time.time() + log_time

    # Open file
    log = open("Chance.csv", "w")

    # Setup SenseHat
    sh = SenseHat()

    # Log for "log_time"
    while time.time() + t_end:
        acl = sh.get_accelerometer_raw()
        print(str(acl["x"]) + "," + str(acl["y"]) + "," + str(acl["z"]) + "\n")
        log.write(str(acl["x"]) + "," + str(acl["y"]) + "," + str(acl["z"]) + "\n")
        time.sleep(1)

    # Close file and save
    log.close

from time import sleep

import sense_hat

from .helpers import make_logo

if __name__ == "__main__":
    cont = True
    sh = sense_hat.SenseHat()
    # Compass, Gyro, Accelerometer
    sh.set_imu_config(False, False, True)

    R = [255, 0, 0]
    B = [0, 0, 255]
    Y = [255, 255, 0]
    W = [255, 255, 255]
    N = [0, 0, 0]

    while cont:
        acl = sh.get_accelerometer_raw()

        # "sensehat accelerating" state
        if acl["pitch"] >= 2 or acl["roll"] >= 2 or acl["yaw"] >= 2:
            make_logo(sh, R)  # Display RED
            sleep(1)
            make_logo(sh, B)  # Display BLUE
            sleep(1)
            make_logo(sh, Y)  # Display YELLOW
            sleep(1)
            make_logo(sh, W)  # Display WHITE
            sleep(1)

        # "sensehat stationary" state
        else:
            make_logo(sh, N)  # Display NONE
            sleep(1)

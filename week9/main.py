from time import sleep

import sense_hat

from helpers import make_logo

if __name__ == "__main__":
    cont = True
    th = 3
    sh = sense_hat.SenseHat()
    # Compass, Gyro, Accelerometer
    sh.set_imu_config(False, False, True)

    # Color defs
    R = [255, 0, 0]
    B = [0, 0, 255]
    Y = [255, 255, 0]
    W = [255, 255, 255]

    while cont:
        acl = sh.get_accelerometer_raw()

        # "sensehat accelerating" state
        if abs(acl["x"]) >= th or abs(acl["y"]) >= th or abs(acl["z"]) >= th:
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
            sh.clear()  # Display NONE

        for event in sh.stick.get_events():
            if event.action == "held":
                sh.clear()  # Display NONE
                sleep(1)
                cont = False
                break

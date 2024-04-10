import os
import sense_hat

from time import sleep

if __name__ == "__main__":
    cont = True
    th = 2
    sh = sense_hat.SenseHat()

    # Compass, Gyro, Accelerometer
    sh.set_imu_config(False, False, True)

    while cont:
        acl = sh.get_accelerometer_raw()

        for event in sh.stick.get_events():
            if event.action == "held":
                sh.clear()  # Display NONE
                sleep(1)
                cont = False

        # "sensehat accelerating" state
        if abs(acl["x"]) >= th or abs(acl["y"]) >= th or abs(acl["z"]) >= th:
            print("Was shaken")
            stream = os.popen("ping -c 3 google.com")
            o = stream.readlines()
            joe_split = o[7].split(" ")
            split_joe_split = joe_split[3].split("/")
            print("joe ping: ", split_joe_split[1])
            sh.show_message(split_joe_split[1], 0.08, [0, 255, 100])

        # "sensehat stationary" state
        else:
            sh.clear()  # Display NONE

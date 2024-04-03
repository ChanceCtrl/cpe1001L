from time import sleep

import sense_hat

from helpers import make_logo, dis_thing

if __name__ == "__main__":
    mode = 1
    cont = True
    th = 3
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
        if mode == 1:
            if abs(acl["x"]) >= th or abs(acl["y"]) >= th or abs(acl["z"]) >= th:
                dis_thing(sh)

            # "sensehat stationary" state
            else:
                sh.clear()  # Display NONE

        if mode == 2:
            if acl["x"] < -0.236347:
                if acl["x"] < -4.23925:
                    sh.clear()

                if acl["x"] >= -4.23925:
                    dis_thing(sh)

            if acl["x"] >= -0.236347:
                if acl["x"] < 0.40523:
                    if acl["z"] < 0.673576:
                        if acl["z"] < 0.4754:
                            sh.clear()

                        if acl["z"] >= 0.4754:
                            dis_thing(sh)

                    if acl["z"] >= 0.673576:
                        if acl["z"] < 1.02195:
                            if acl["z"] < 1.01292:
                                sh.clear()

                            if acl["z"] >= 1.01292:
                                if acl["y"] < 0.067985:
                                    sh.clear()

                                if acl["y"] >= 0.067985:
                                    dis_thing(sh)

                        if acl["z"] >= 1.02195:
                            if acl["x"] < -0.0808383:
                                dis_thing(sh)

                            if acl["x"] >= -0.0808383:
                                sh.clear()

                if acl["x"] >= 0.40523:
                    if acl["y"] < -1.54229:
                        sh.clear()

                    if acl["y"] >= -1.54229:
                        if acl["z"] < 0.37677:
                            sh.clear()

                        if acl["z"] >= 0.37677:
                            dis_thing(sh)

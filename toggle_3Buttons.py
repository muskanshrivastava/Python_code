import os
from msvcrt import getch
import time


def toggle_button():
    toggle_A = toggle_S = toggle_D = 0
    while True:

        inp = ord(getch())
        os.system('cls')
        if inp in [ord("A".lower()), ord("S".lower()), ord("D".lower())]:

            if inp == ord("A".lower()) and toggle_A == 0:
                print("ON")
                toggle_A = 1

            elif inp == ord("A".lower()) and toggle_A == 1:
                print('OFF')
                toggle_A = 0

        # ---------------------------------------------------------------------

            elif inp == ord("S".lower()) and toggle_S == 0:
                print("ON")
                toggle_S = 1

            elif inp == ord("S".lower()) and toggle_S == 1:
                print('OFF')
                toggle_S = 0

        # ---------------------------------------------------------------------

            elif inp == ord("D".lower()) and toggle_D == 0:
                print("ON")
                toggle_D = 1

            elif inp == ord("D".lower()) and toggle_D == 1:
                print('OFF')
                toggle_D = 0

        # ---------------------------------------------------------------------

        else:
            print('Thanx for playing !!\n')
            exit()


print('\nLets start the game........')
time.sleep(1)
print('\nA - OFF', 'S - OFF', 'D - OFF')
time.sleep(1)
print('\nPress any key from " A  S  D" key to start the game and press another key to end the game\n')

toggle_button()

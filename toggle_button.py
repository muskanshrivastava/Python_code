import os
from msvcrt import getch
toggle = 0
print('\nPress space key to start the game and press another key to end the game\n')
while True:
    try:
        inp = ord(getch())
    except :
        exit()
    os.system('cls')
    if inp == 32 and toggle == 0:
        print("OFF")
        toggle = 1
    elif inp == 32 and toggle == 1:
        print('ON')
        toggle = 0
    else :
        print('Thanx for playing !!\n') 
        exit()
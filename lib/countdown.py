# countdown.py

import time

def countdown():
    number = 10

    while number > 0:
        print(f'{number} SECOND(S)!')
        time.sleep(1)
        number -= 1

    print("HAPPY NEW YEAR!")

def countdown_with_sleep(seconds):
    while seconds > 0:
        print(f'{seconds} SECOND(S)!')
        time.sleep(1)
        seconds -= 1

    print("HAPPY NEW YEAR!")

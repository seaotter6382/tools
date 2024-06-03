import random
import time
import math
import sys
import string

class math():
    def randint(number1, number2):
        return random.randint(number1, number2)
    def randstr(length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))
    def randstrint(length):
        return ''.join(str(random.randint(0, 9)) for _ in range(length))

def sleep(number):
    time.sleep(number)

class tools():
    def help():
        print("math")
        print("    randint(1, 3) change the 1 and 3 for the top and bottom number")
        print("    randstr(4) random strirng, the number is the length")
        print("    randstrint(4) random string int, the number is the length")
        print("sleep(4) change the number for the seconds")
        print("tools.help() prints this")

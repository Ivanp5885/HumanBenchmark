User
import random
import os
import time

intl = []
int = 0
guess = 0
rep = 1
level = 1
gameOn = True

print("Human benchmark test")
time.sleep(1)
print("Ready? Press any key to continue.")
input()
print("You are going to see numbers that you have to memorize. Then simply return the number and continue to the next level. Each level consists of 5 repetitions with the same amount of numbers. Press any key to continue.")
input()
while gameOn == True:
    intl.clear()
    for i in range(2):
        intl.clear()
        while level != len(intl):
            if not intl:
                intl.append(random.randint(1,9))
            else:
                intl.append(random.randint(0,9))
        int = ''.join(str(digit) for digit in intl)
        print(int)
        time.sleep(3)
        os.system('clear')
        guess = input()
        if guess != int:
            gameOn = False
            break
    level += 1
print("Congratulations. You lasted " + str(level) + " levels and you messed up " + str(int) + " for " + str(guess) + ".")

import random
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

welcomeMsg = input(
    "Welcome to Guest The Number Game.\nPress any button to continue...")

startNum = int(config['DEFAULT']['startNum'])
endNum = int(config['DEFAULT']['endNum'])

num = random.randrange(startNum, endNum)

while (True):
    try:
        guestNum = int(
            input(f"Guest The Number between {startNum} - {endNum}\t: "))

        # Check with the range (startNum and endNum)
        if (guestNum > startNum) and (guestNum < endNum):
            if guestNum < num:
                startNum = guestNum
            elif guestNum > num:
                endNum = guestNum
            elif guestNum == num:
                winMsg = input("You Win!")
                againAnswer = input("You Wanna Play Again? [y / N]\t: ")
                if againAnswer == "y":
                    num = random.randrange(startNum, endNum)
                    startNum = int(config['DEFAULT']['startNum'])
                    endNum = int(config['DEFAULT']['endNum'])
                    print("\n")
                else:
                    print("\nThank You for Playing!!")
                    break

        else:
            errorMsg = input("start from a predetermined number range... \n")

    except ValueError as msg:
        errorMsg = input("you must input a valid number! \n")

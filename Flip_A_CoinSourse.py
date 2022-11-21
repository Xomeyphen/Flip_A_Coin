#flip a coin with responce
import random
import time

while True:
    time.sleep(0.8)
    print("Welcome to Flip A Coin")
    time.sleep(0.8)
    print("Pick Your side and take a chance at winning \nHeads or Tails?")
    time.sleep(0.8)
    #answer here
    answer = str.lower(input(("Enter your answer --> ")))

    if answer == "heads" or answer == "tails":
        time.sleep

        print("Digging in the box of treasure...")
        time.sleep(0.8)
        print("Thorwing the gold coin on the floor...")
        time.sleep(0.8)
        print("Many times...")
        time.sleep(0.8)
        print("...")
        time.sleep(0.8)
        print("One more time...")
        time.sleep(0.8)

    #number generator/check
        coin = random.randint(1,2)
        if coin == 1:
            coin = str("heads")
        elif coin == 2:
            coin = str("tails")

        print(f"The answer is, {coin}!")
        time.sleep(0.5)
        print(f"You chose {answer}.")
        time.sleep(0.5)
    #if 1 then heads if 2 then tails
        if answer == coin:
            print("You're lucky you got it! \n----------------------------------------------------")
        elif answer != coin:
            print("Nope I guess luck wasnt on your side today! \n----------------------------------------------------")
            time.sleep(2)

    else:
        print(f'I litteraly said heads or tails not "{answer}".')
        print("This isn't 5th grade.")
        time.sleep(5)
        break
exit()
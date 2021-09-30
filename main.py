import time
import random
userinp = 0
points = 0
noq = 0
wroans = 0
qcount = 1

print("WELCOME TO MY GAME\nINSTRUCTIONS:-\nYOU HAVE TO SOLVE AS MANY MATH PROBLEMS AS YOU CAN IN 1 MINUTE\n"
      "EACH CORRECT ANSWER GIVES YOU 20 POINTS! BUT EACH INCORRECT ANSWER DEDUCTS 5 POINTS!\n")
time.sleep(2)
gamestartend = input("\npress enter to start\n")
ini = time.time()
while 1:

    fin = time.time()
    if fin - ini >= 60:
        print("--------------\nTIME'S UP!!!\n--------------")
        print()
        print(f"YOU ATTEMPTED {noq + wroans} QUESTIONS,\nAND SCORED {points} POINTS\n\nANSWERED {noq} QUESTIONS CORRECTLY, AND\n         {wroans} QUESTIONS INCORRECTLY")
        gamestartend = input("\nPress Enter To Exit")
        break

    oppr = "x"
    op = (lambda a, b: a*b)

    no1 = random.randrange(5, 15)
    no2 = random.randrange(3, 11)

    print("------------\nQUESTION", qcount, "\n------------\n")
    qcount += 1
    print(f"What is {no1} {oppr} {no2}")
    corans = op(no1, no2)
    while True:
        userinp = input("enter your answer -\n")
        if userinp.isnumeric():
            userinp = int(userinp)
            break
        else:
            print("You Must Enter A Positive Integer!!!")


    if userinp == corans:
        print("\nCorrect, +20 Points!!\n")
        noq += 1
        points += 20
    else:
        print("\nIncorrect, -5 Points\n")
        points -= 5
        wroans += 1

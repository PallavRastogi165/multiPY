import random
print("WELCOME TO MY GAME\nINSTRUCTIONS:-\nYOU HAVE TO GUESS A SECRET NUMBER \nAT EACH STEP I WILL TELL YOU IF THE NUMBER YOU ENTERED IS LOWER OR HIGHER THAN THE SECRET NUMBER\nYOU HAVE LIMITED GUESSES BEFORE YOU LOSE")
print()
print("choose difficulty-easy,medium,hard")
diflv = input().lower()
if diflv == "easy":
    uplim = 100
    sno = random.randrange(1, 100)
    guess = 8
if diflv == "medium":
    uplim = 200
    sno = random.randrange(1, 200)
    guess = 8
if diflv == "hard":
    uplim = 500
    sno = random.randrange(1, 500)
    guess = 10
print()
print("you have choosen", diflv, "difficulty\n")
print("THE SECRET NUMBER IS AN INTEGER BETWEEN 1 AND", uplim)

while(1):
    print("YOU HAVE",guess,"GUESSES LEFT!")
    print("ENTER YOUR NUMBER")

    userinp = int(input())
    guess = guess - 1

    if guess == 0 and userinp != sno:
        print("GAME OVER\nNO GUESSES LEFT\nTHE SECRET NUMBER WAS",sno)
        break
    elif userinp < sno:
        print("try something bigger")
        continue
    elif userinp > sno:
        print("try something smaller")
        continue
    elif userinp == sno:
        print("CONGRATULATIONS YOU WON, THE SECRET NUMBER WAS",sno,"GUESSES REMAINING =", guess)
        break
print("\n the end")
print("game made by pallav")
exit12 = input("press enter to exit")

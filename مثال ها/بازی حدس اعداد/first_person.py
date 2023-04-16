import random

n = random.randint(1,1000)
win = False

for step in range(10):
    print("enter your guess", step + 1)
    q = input()
    q = int(q)
    if q == n:
        print("Yayyyyy!")
        win = True
        break
    elif n > q:
        print("go upper")
    else:
        print("go lower")

if win == False:
    print("you are a loser")
    print("my number was:", n)
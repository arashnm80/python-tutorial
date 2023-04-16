up = 1000
down = 1

for step in range(10):
    guess = int((up + down) / 2)
    print("guess number", step + 1)
    print(guess)
    print("Was that right?")
    x = input() # u for upper, l for lower, f for find
    if x == "f":
        print("ok, right guess")
        break
    elif x == "u":
        down = guess
    elif x == "l":
        up = guess
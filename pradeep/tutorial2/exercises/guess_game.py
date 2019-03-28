# Exercise - Guessing Game

number = random.randint(1, 10)

count = 1
while count <= 3:
    guess_number = int(input("Guess: "))
    if guess_number == number:
        print("You guessed correct")
        break
    else:
        print("You guessed wrong")
    count = count + 1

if count > 3:
    print(" No more turns")

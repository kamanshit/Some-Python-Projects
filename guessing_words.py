import random

easy_words=["apple", "banana", "Mango", "orange"]
medium_words=["python", "java", "monkey", "rust"]
hard_words=["elephant", "umbrella", "diamond", "computer"]

print("Welcome to the password guessing game----")

print("\n Choose your level--easy, medium, hard")

level= input("Enter your level: ") .lower()

if level=="easy":
    secret=random.choice(easy_words)

elif level=="medium":
    secret=random.choice(medium_words)

elif level == "hard":
    secret=random.choice(hard_words)

else:
    print("Invalid choice,---Default Level is Easy")
    secret=random.choice(easy_words)



attempts=0

print("\n Guess the words")

while True:
    guess=input("Enter Your Guess: ").lower()
    attempts +=1

    if guess==secret:
        print(f'Congratulations You Guess The Right Word...{guess}. Number of attempts is {attempts}')
        break


    hint=""

    for i in range(len(secret)):
        if i <len(guess) and guess[i]==secret[i]:
            hint+=guess[i]
        else:
            hint+="_"

    print("Hint: ",hint)

print("\n ---Game Over---")
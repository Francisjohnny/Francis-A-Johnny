from random import randint

# Function to check users' guess against actual answer
def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("Too high.")
    elif user_guess < actual_answer:
        print("Too low.")
    else:
        print(f"You got it right! The answer was {actual_answer}")


# Function to set difficulty
def set_difficulty():
    input("Choose a difficulty. Type 'Easy' or 'Hard': ")




# Choosing a random number between 1 and 100.
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = randint(1, 100)



# Let the user guess a number
guess = int(input("Make a guess: "))




# Tracking the number of turns and reduce by 1 if they get it wrong

# Repeat the guessing functionality if they are wronge
import random


def generate_secret_number():
    return ''.join(random.sample('0123456789', 4))


def count_bulls_and_cows(secret, guess):
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = sum(min(secret.count(g), guess.count(g)) for g in set(guess))
    cows -= bulls
    return bulls, cows


def main():
    print("Welcome to the Cows and Bulls Game!")
    print("Type 'exit' to quit the game.")
    secret_number = generate_secret_number()
    print("Secret number has been generated. Try to guess it!")

    trials = 0
    successes = 0

    while True:
        guess = input("Enter your guess: ")

        if guess.lower() == 'exit':
            break

        if len(guess) != 4 or not guess.isdigit():
            print("Please enter a 4-digit number.")
            continue

        bulls, cows = count_bulls_and_cows(secret_number, guess)
        trials += 1

        if bulls == 4:
            successes += 1
            print("Congratulations! You guessed the number {} correctly in {} trials.".format(secret_number, trials))
            break
        else:
            print("Bulls: {}, Cows: {}".format(bulls, cows))

    print("Total number of trials:", trials)
    if trials > 0:
        print("Average success rate: {:.2f}%".format((successes / trials) * 100))


if __name__ == "__main__":
    main()

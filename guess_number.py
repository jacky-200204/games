from random import randint
starting = "Guess the number."
exit_msg = "Do you want to play more? (y/n)"

def validity(num):
    try:
        num = int(num)
        again = False
    except ValueError:
        print("Enter a number.")
        again = True

    return again

def check(num, secret_num, guessed_time):
    if num == secret_num:
        won = True
    elif guessed_time < 3:
        if num > secret_num:
            print("You guessed too high!")
            won = False
        elif num < secret_num:
            print("You guessed too low!")
            won = False
    else:
        won = False

    return won

def try_again():
    print(exit_msg)
    while True:
        response = input(":> ").strip().lower()
        if response in ('y', 'n'):
            if response == 'y':
                cont = True
                break
            else:
                cont = False
                break
        else:
            continue
    return cont


def main():
    while True:
        guessed_time = 0
        secret_num = randint(0, 9)
        print(starting)
        while True:
            if guessed_time < 3:
                guessed_num = input(":> ").strip()
                again = validity(guessed_num)
                if again:
                    continue
                else:
                    guessed_time += 1
                    guessed_num = int(guessed_num)
                    won = check(guessed_num, secret_num, guessed_time)
                    if won:
                        print("You won")
                        break
                    else:
                        continue
            else:
                print("You lost the number is", secret_num)
                break
        again = try_again()
        if again:
            continue
        else:
            break
main()

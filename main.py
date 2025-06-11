import random

def guess_the_number():
    print("Вітаю!")
    print("Я загадав число від 1 до 100. Спробуйте вгадати його за 7 спроб.")

    secret_number = random.randint(1, 100)
    attempts = 7

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"\n Введіть Ваше припущення: "))
        except ValueError:
            print("Будь ласка, введіть ціле число.")
            continue

        if guess < secret_number:
            print("Занадто маленьке!")
        elif guess > secret_number:
            print("Занадто велике!")
        else:
            print(f"Ви вгадали число {secret_number} .")
            break
    else:
        print(f"\n На жаль, ви не вгадали. Загадане число було: {secret_number}")

if __name__ == "__main__":
    guess_the_number()

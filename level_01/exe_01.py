import time


def get_input() -> str:
    raw_input = input("Enter your value: ")
    return raw_input


def main() -> None:
    name = input("What is your name? ")
    raw_age = input("How old are you? ")

    try:
        int_age = int(raw_age)
    except Exception as e:
        raise Exception(f"Error parsing your age: {e}")

    current_time = time.localtime().tm_year
    if int_age < 100:
        print(
            f"Well, {name.title()}, you will turn 100 years old in the year {current_time + 100 - int_age}.")
    else:
        print("Hey, no kidding please!")


if __name__ == "__main__":
    main()

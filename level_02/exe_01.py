from typing import List


def get_input() -> int:
    raw_input = input("Enter your value: ")
    try:
        int_input = int(raw_input)
        return int_input
    except Exception as e:
        raise Exception(f"Error parsing your input: {e}")


def main() -> List[int]:
    number = get_input()
    result = []
    for num in range(1, number//2+1):
        if number % num == 0:
            result.append(num)

    return result


if __name__ == "__main__":
    result = main()
    print(result)

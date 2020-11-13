from typing import List


def get_input() -> int:
    raw_input = input("Enter your number: ")
    try:
        int_input = int(raw_input)
        return int_input
    except Exception as e:
        raise Exception(f"Error parsing your number: {e}")


def main(arr: List[int], bar=None) -> List[int]:

    if bar is None:
        bar = 5

    result = []
    for num in arr:
        if num < bar:
            result.append(num)

    return result


if __name__ == "__main__":
    result_01 = main([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(result_01)

    number = get_input()
    result_02 = main([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], number)

    print(result_02)

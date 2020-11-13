from typing import List


def input_list(arr: List[int], num: int) -> bool:
    left = 0
    right = len(arr) - 1

    while left < right:
        middle_index = left + (right - left) // 2
        middle_item = arr[middle_index]
        if middle_item == num:
            return True
        elif middle_item > num:
            right = middle_index - 1
        else:
            left = middle_index + 1

    return False


if __name__ == "__main__":
    result = input_list([1, 3, 5, 6, 8, 9, 10], 7)
    print(result)

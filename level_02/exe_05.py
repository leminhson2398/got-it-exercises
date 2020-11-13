from typing import List


numOfFibos = 0


def get_input() -> None:
    global numOfFibos

    raw = input("Enter number of numbers: ")
    try:
        int_raw = int(raw)
        numOfFibos = int_raw
    except Exception:
        print(f"Your value must be integer: {raw}")
        exit(0)


def fibonacci(arr: List[int]):
    if numOfFibos < 0:
        exit(0)
    elif numOfFibos == 0:
        return []
    elif numOfFibos == 1:
        return [1]
    elif numOfFibos == 2:
        return [1, 1]
    else:
        if len(arr) < numOfFibos:
            length = len(arr)
            if length <= 2:
                arr = [1, 1]
            nextNum = arr[length-1] + arr[length-2]
            arr.append(nextNum)
            return arr + fibonacci(arr)


if __name__ == "__main__":
    get_input()
    print(
        fibonacci([])
    )

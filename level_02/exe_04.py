from typing import List


def main(arr1: List[int], arr2: List[int]) -> List[int]:
    result = []
    for i in arr1:
        if i not in result:
            result.append(i)

    return [i for i in result if i in arr2]


if __name__ == "__main__":
    result = main(
        [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    )
    print(result)


# METHOD 2 - USING GENERATOR, uncomment code below, comment out the above and run

# def uniqueGenerator(arr: List[int]):
#     for idx in range(len(arr)):
#         existBefore = True if arr[:idx].count(arr[idx]) > 0 else False
#         if not existBefore:
#             yield arr[idx]


# def interception(arr: List[int], brr: List[int]):
#     uniq = uniqueGenerator(arr=arr)
#     result = [item for item in uniq if item in brr]

#     print(result)


# if __name__ == "__main__":
#     interception(
#         [1, 3, 5, 7, 8, 9, 7, 3],
#         [1, 3, 5, 6, 10]
#     )

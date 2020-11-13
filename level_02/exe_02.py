
def get_input() -> str:
    raw_input = input("Enter your string: ")
    return raw_input


def main() -> bool:
    data = get_input()

    data_length = len(data)
    if data_length == 1:
        return True

    for i in range(data_length):
        if data[i] != data[data_length - 1 - i]:
            return False
        if i == data_length // 2:
            break
    return True


result = main()
print(result)

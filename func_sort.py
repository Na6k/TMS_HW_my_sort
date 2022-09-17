number = [5, 1, 3, 2, 12, 42, 32, 4, 14, 0, 166, 3, 132, 1998, 34, -10, -2, -100000, -324, 234, 5234, 5, 65, 75453, 33, 545, -545]


def sorting(input_list):
    n = 1
    while n < len(input_list):
        for i, el in enumerate(input_list):
            if el > input_list[n]:
                b = input_list[n]
                input_list[n] = el
                input_list[i] = b
        n += 1


if __name__ == '__main__':
    print(number, '\n')
    sorting(number)
    print(number)
# Sort Selection Algorithm


def returnSmallest(myArr):
    smallest_index = 0
    smallest_number = myArr[smallest_index]

    for i in range(1, len(myArr)):
        if myArr[i] < smallest_number:
            smallest_index = i
            smallest_number = myArr[i]

    return smallest_index

def SortSelection(myArr):
    newArr = []

    for i in range(len(myArr)):
        smallest_index = returnSmallest(myArr)
        newArr.append(myArr.pop(smallest_index))

    return newArr

def main():
    my_list = [int(numb) for numb in input().split()]

    print(SortSelection(my_list))


if __name__ == '__main__':
    main()
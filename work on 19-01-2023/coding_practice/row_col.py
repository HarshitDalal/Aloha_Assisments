def findCroxSum(matrix):
    mul = 1

    i = len(matrix) // 2
    for j in matrix[i]:
        mul *= j

    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    mul1 = 1
    i = len(result) // 2
    for j in result[i]:
        mul1 *= j

    return mul + mul1


def main():
    matrix = [
        [1, 2, 3],
        [6, 5, 11],
        [7, 8, 4]
    ]
    print(findCroxSum(matrix))


if __name__ == '__main__':
    main()

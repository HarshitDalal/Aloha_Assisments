def printResult(num):
    result = ''
    m = [int(i) for i in num]

    if m == sorted(m) or m == sorted(m, reverse=True):
        result = 'Not a Special Chemical'
    else:
        result = 'Special Chemical'
    return result


def main():
    n = int(input())
    for i in range(n):
        str = input()
        print(printResult(str))


if __name__ == '__main__':
    main()

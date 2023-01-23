def processString(mainStr, strs):
    result = None
    strs = strs.split()
    l_strs = len(strs)
    count = 0
    for i in strs:
        if i in mainStr:
            count += 1
        else:
            return 'No'

    if count == l_strs:
        result = 'Yes'

    return result


def main():
    n = int(input())
    mainStr = input()

    for i in range(n):
        strs = input()
        print(processString(mainStr, strs))


if __name__ == '__main__':
    main()

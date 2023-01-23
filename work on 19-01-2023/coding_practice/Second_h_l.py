def getResult(n, arr):
    result = []
    arr = list(set(arr))
    arr.sort()
    result.append(arr[-2])
    result.append(arr[1])

    return result


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = getResult(n, arr)
    print(result[0])
    print(result[1])

if __name__ == '__main__':
    main()

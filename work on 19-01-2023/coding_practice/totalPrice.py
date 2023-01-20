def totalPrice(arr, n):
    sum = 0
    mys = set(arr)
    ls = list(mys)
    for i in ls:
        sum += i

    return sum


def main():
    N = int(input())
    arr = list(map(int, input().split()))
    print(totalPrice(arr, N))


if __name__ == '__main__':
    main()

l = [[1, 4], [5, 2]]
l.sort(key=lambda x: x[1])
print(l)

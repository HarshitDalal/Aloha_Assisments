class Transform:
    def __init__(self, n):
        self.num = n

    def print_result(self):
        temp = str(self.num)
        zer = ''
        num = ''
        for i in temp:
            if i == '0':
                zer += i
            else:
                num += chr(int(i) + 96)
        print(num + zer)


if __name__ == '__main__':
    obj = Transform(1020101010)
    obj.print_result()
# 1211100000
# abaaa00000
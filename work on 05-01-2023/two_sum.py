class Problems:
    def two_sum(self, array, pair):
        res = []
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if array[i] + array[j] == pair:
                    res.append((array[i], array[j]))
        return res

    def intersection_of_array(self, arr1, arr2):
        arr = [val for val in arr1 if val in arr2]
        return arr

    def remove_repating_ele(self, array):
        arr = []
        for i in array:
            if i not in arr:
                arr.append(i)
        return arr


if __name__ == '__main__':
    p1 = Problems()

    print(p1.two_sum([1, 5, 7, 3, 8, 2], 7))
    print(p1.intersection_of_array([1, 4, 2, 6, 3, 7, 3], [4, 2, 6, 8, 9, 0, 5]))
    print(p1.remove_repating_ele([1, 2, 4, 2, 5, 3, 6, 2, 7, 1, 4]))

    arr = [1,2, 4,6,7]

    a = [i for i in arr if i > 4 ]
    print(a)

"""
给定一个二维数组，其每一行从左到右递增排序，从上到下也是递增排序。给定一个数，判断这个数是否在该二维数组中。
"""


def get_num_from_array(matrix, num):
    if not matrix:
        return False
    data = matrix[0]
    col_index = len(data)
    for index, value in enumerate(data):
        if value == num:
            print(0, index)
            return True
        if value > num:
            col_index = index
            break
    row_index = len(matrix)
    for index, item in enumerate(matrix):
        if item[0] == num:
            print(index, 0)
            return True
        if item[0] > num:
            row_index = index
            break
    print(row_index)
    print(col_index)
    for i in range(row_index):
        for j in range(col_index):
            print(matrix[i][j])
            if matrix[i][j] == num:
                print(i, j)
                return True
    return False


a = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]

print(get_num_from_array(a, 23))
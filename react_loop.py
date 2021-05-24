"""
顺时针打印矩阵
"""

def print_matrix(matrix):
    if not matrix:
        return []
    ret = []
    r1 = 0
    r2 = len(matrix) -1
    c1 = 0
    c2 = len(matrix[0]) -1

    
    while(r1 <= r2 and c1 <= c2):
        for i in range(c1, c2+1):
            ret.append(matrix[r1][i])
            print("shang: %d" % i)
        
        for i in range(r1+1, r2):
            ret.append(matrix[i][c2])
            print("you: %d" % i)
        
        if(r1 != r2):
            for i in range(c2, c1, -1):
                ret.append(matrix[r2][i])
                print("xia: %d" % i)
        if(c1 != c2):
            for i in range(r2, r1, -1):
                ret.append(matrix[i][c1])
                print("zuo: %d" % i)
        r1 += 1
        r2 -= 1
        c1 += 1
        c2 -= 1
        print(r1, r2, c1, c2)
    return ret


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10, 11, 12],
        [13, 14, 15, 16]
        ]
    print(print_matrix(matrix))




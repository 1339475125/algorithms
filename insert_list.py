"""
列表中插入数据[1, 2, 6, 8,10]

1、 有序 2、已存在
"""

def insert_data(data, num):
    """
    插入一个数据，已存在报错， 否则有序插入
    """
    # if num in data:
    #     print("数据已经存在")
    #     return data
    if num < data[0]:
        data.insert(0, num)
        return data
    if num > data[-1]:
        data.append(num)
        return data
    for i in range(1, len(data)):
        if data[i] > num:
            break
    return data[:i] + [num] + data[i:]
    

if __name__ == "__main__":
    data = [1, 2, 6, 8, 10]
    print(insert_data(data, 3))
    
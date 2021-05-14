# -*- coding:utf-8 -*-


def get_max_data(data, start, num, max_data):
    size  = len(data)
    cur_max_size = 0
    if (start > size-num):
        return max_data
    window_data = data[start:start+num]
    max_data.append(max(window_data))
    start = start + 1
    return get_max_data(data, start , num, max_data)



if __name__ == "__main__":
    data = [4, 3, 5, 4, 3, 3, 6, 7]
    # 窗口大小
    num = 3
    max_data = []
    start = 0
    result = get_max_data(data, start, num, max_data)
    print(result)

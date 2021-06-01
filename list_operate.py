"""
两个列表中相同的元素和不同的元素
"""

def get_data(list1, list2):
    if not list1 and not list2:
        #  都为空的情况
        return [], []
    if not list1 and list2:
        return [], list2
    if not list2 and list1:
        return [], list1

    # 相同的元素
    same_list = []
    diff_list = []
    if len(list2) > len(list2):
        list1, list2 = list2, list1
    length = max(len(list1), len(list2))
    for i in range(length):
        if list1[i] in list2:
            same_list.append(list1[i])
        # 不同的元素
        else:
            diff_list.append(list1[i])
    diff_list.extend(list(set(list2) - set(same_list)))
    return same_list, diff_list


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    print(get_data(a, b))
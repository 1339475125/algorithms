"""
导弹拦截
先将第一枚导弹高度设置为初始高度，之后进行验证向下递降的最大值
中间可以跳过
"""

def func(nums):
    if not nums:
        return None

    ans = [nums[0]]
    for item in nums[1:]:
        i = 0
        length = len(ans)
        while i < length:
            if item < ans[i]:
                i = i + 1
            else:
                ans[i] = item
                break
        if i >= length:
            ans.append(item)
    return len(ans)



ls = [389, 207, 155, 300, 299, 170, 158, 65]
print(func(ls))
            
        


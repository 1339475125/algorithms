class Solution:
    # // 动态规划，cost[0]代表当前位不换时最小交换次数
    #     //          cost[1]代表当前位交换时最小交换次数
    def minSwap(self, A: List[int], B: List[int]) -> int:
        cost = [0 ,1]
        for i in range(1, len(A)):
            # 如果两个数组的当前位都大于上一位，理论上不换就可以保持两个数组单调递增
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                # 如果满足这个条件，当前位交不交换都满足单调递增
                if A[i] > B[i - 1] and B[i] > A[i - 1]:
                    # 既然当前位不换，那么当前位的最小交换次数继承上一位的交换或不交换的最小值
                    cost = [min(cost), min(cost) + 1]
                else:
                    # 既然要交换，则是上一位交换或不交换的最小值加1
                    cost[1] += 1
            else:
                # 如果不交换自己，那么需要交换上一位，所以继承上一位交换的次数
                cost = [cost[1],cost[0] + 1]
        return min(cost)
"""
逆序对
"""
from typing import List


class Solution:

    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        end = len(nums) - 1
        tmp = list(nums)
        # 首先先写出归并排序
        def get_sort_num(start, end):
            if start == end:
                # print("6666 start:%d,end:%d" % (start, end))
                return 0
            # 先分开
            mid = start + (end - start)//2
            
            left_num = get_sort_num(start, mid)
            right_num = get_sort_num(mid + 1, end)

            if tmp[mid] <= tmp[mid + 1]:
                # print("7777 start:%d, end:%d" %(start, end))
                return left_num + right_num
            # 分开成最小单元后,在两两合并,每一个合并的个体都是有序的

            def merge(start, mid, end):
                index = start
                # 存储开始和停止的位置
                tmp_start = start
                tmp_end = end
                # 保存逆序对的个数
                reverse_num = 0

                # 第二个区间的开始部分
                second_start = mid + 1
                # print(tmp)
                # print("start:%d,mid:%d" %(start,mid))
                # print("start:%d,mid:%d,secend_start,%d,end:%d" % (start, mid, second_start, end))
                while start <= mid and second_start <= end:
                    if nums[start] > nums[second_start]:
                        tmp[index] = nums[second_start]
                        second_start += 1
                        reverse_num += mid - start + 1
                    elif nums[start] <= nums[second_start]:
                        tmp[index] = nums[start]
                        start += 1
                    index += 1
                # print("index:%d,start:%d,mid:%d,secend_start:%d,end:%d" % (index,start,mid,second_start,end))
                if start > mid and second_start <= end:
                    for i in range(second_start, end + 1):
                        # print("2.1i" + str(i) + "index" + str(index))
                        tmp[index] = nums[i]
                        index += 1
                elif start <= mid and second_start > end:
                    for i in range(start, mid + 1):
                        
                        # print("2.2i" + str(i) + "index" + str(index) + "start" + str(start) + "mid" + str(mid) )
                        tmp[index] = nums[i]
                        index += 1
                # print(tmp)
                
                for i in range(tmp_start, tmp_end + 1):
                    # print("4i" + str(i) + "start" + str(start) + "end" + str(end))
                    nums[i] = tmp[i]
                # print(nums)
                return reverse_num

            merge_num = merge(start, mid, end)
            # print(left_num)
            # print(right_num)
            # print(merge_num)
            all_num = left_num + right_num + merge_num
            # print("all_num:%d" % (all_num))
            return all_num
        res =  get_sort_num(0, end)
        # print("end:%d" % (end))
        # print(res)
        return res
                    

s = Solution()
print(s.reversePairs([7,5,6,4]))

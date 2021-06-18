class Solution:
    def thousandSeparator(self, n: int) -> str:
        data = str(n)
        result = []
        if len(data) < 4:
            return str(data)
        size  = len(data)
        for i in range(len(data)):
            result.append(data[size-i-1])
            if (i+1) % 3 ==0 and i != size - 1:
                result.append(".")
        result = result[::-1]
        return ''.join(result)
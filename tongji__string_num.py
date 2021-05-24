"""
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符 "go" 时，第一个只出现一次的字符是 "g"。当从该字符流中读出前六个字符“google" 时，第一个只出现一次的字符是 "l"。
"""

class Soultion:

    def __init__(self):
        self.strs = []
        self.res = {}
    
    def insert(self, data):
        self.res[data] = self.res.get(data, 0) + 1
        if self.res.get(data, 0) <= 1:
            self.strs.append(data)
        elif self.res.get(data, 0) > 1 and data in self.res:
            self.strs.remove(data)


    def get_once_data(self):
        return self.strs


s = Soultion()
s.insert("h")
s.insert("h")
s.insert("a")
print(s.get_once_data())

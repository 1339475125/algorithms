from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []
        size = 0
        for item in words:
            size = size + len(item)
        s_size = len(s)
        first_data = ''.join([item[0] for item in words])
        res = []
        # import pdb
        # pdb.set_trace()
        for i in range(s_size-size):
            data = s[i:i+size]
            if data[0] not in first_data:
                continue
            all_len = [False] * len(words)
            for j, word in enumerate(words):
                if word not in data:
                    all_len = [False] * len(words)
                    break
                result = data.split(word)
                for item in result:
                    if not item:
                        all_len[j] = True
                data = "".join(result)
            if all(all_len):
                res.append(i)
        return res


    def findSubstring2(self, s: str, words: List[str]) -> List[int]:
        if len(words)==0 or len(s)==0:
            return []

        wl=len(words[0])
        ss=[]
        for i in range(len(s)-wl*len(words)+1):
            tw=words.copy()
            k=i
            while len(tw)!=0:
                if s[k:k+wl] in tw:
                    tw.remove(s[k:k+wl])
                    k+=wl
                else:
                    break
            if len(tw)==0:
                ss.append(i)
        return ss

if __name__ == "__main__":
    s = Solution()
    string = "barfoofoobarthefoobarman"
    words = ["bar","foo","the"]
    print(s.findSubstring(string, words))
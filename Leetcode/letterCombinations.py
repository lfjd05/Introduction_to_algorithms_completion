class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}
        digits_list = list(digits)
        res = []
        while len(digits_list)>0:
            a = digits_list.pop(0)

            # 加入第一个元素
            if not res:
                for i in d[a]:
                    res.append(i)
                print('加入的第一个元素后', res)
            # 加入后续元素
            else:
                # res = [m+n for m in res for n in d[a]]
                temp = []
                for i in d[a]:
                    temp = res

                    # 组合新元素
                    def fx(x):
                        return x+i
                    temp+=list(map(fx, temp))
                res = temp
        return res


# print(Solution().letterCombinations('23'))
print(Solution().letterCombinations('2345'))

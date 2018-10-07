"""
给定一个字符串 S，返回 “反转后的” 字符串，
其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
"""


class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        str_list = []
        str_dict = [0 for _ in range(len(S))]    # 存储符号和位置
        # 找到字母和符号的位置
        for i in range(len(S)):
            # print(S[i])
            # print(S[i].isalpha())
            if S[i].isalpha():
                str_list.append(S[i])
            else:
                str_dict[i] = S[i]
        # 反转
        str_list = str_list[::-1]
        # 插入
        # insert_cnt = 0
        for index, i in enumerate(str_dict):
            if i != 0:
                str_list.insert(index, i)
        # print(str_list)
        return ''.join(i for i in str_list)

# print(Solution().reverseOnlyLetters("ab-cd"))
# print(Solution().reverseOnlyLetters("a-bC-dEf-ghIj"))  # "j-Ih-gfE-dCba"
print(Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!"))  # "Qedo1ct-eeLg=ntse-T!"

# 牛客网 A/B试题
"""
    本题要求计算A/B，其中A是不超过1000位的正整数，B是1位正整数。
    你需要输出商数Q和余数R，使得A = B * Q + R成立。
"""

A, B = [int(each) for each in input().split()]
print(str(A//B) + ' '+str(A%B))
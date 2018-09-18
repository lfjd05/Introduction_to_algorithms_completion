"""
    暴力方法：
逐个检查所有的子字符串，看它是否不含有重复的字符。
设计一个函数，如果该字符串不再s中返回true
"""


def bar(multiple):
    def foo(n):
        return multiple ** n
    return foo
print(bar(2)(3))
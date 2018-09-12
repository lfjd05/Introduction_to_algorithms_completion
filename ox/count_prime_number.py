# 牛课网，数素数。令Pi表示第i个素数。现任给两个正整数M <= N <= 10000，请输出PM到PN的所有素数。
# 输入在一行给出M和N
import math


def mut_input():
    data = [int(each) for each in input().split()]
    M, N = data
    return M, N


# 判断这个数是不是素数
def find_prime(number):
    if number != 1:
        sqrt_i = int(math.sqrt(number))
        for j in range(2, sqrt_i + 1):
            if number % j == 0:
                # 是合数
                return False
        else:
            # 循环完了都没有跳出说明是质数
            return True


M, N = mut_input()
max_num = N
count = 0
test = 2
prime_list = []
# 找到前10000个素数，太多了浪费时间，改成找到前N个
while True:
    if count == max_num:
        # 等于最大数
        break
    else:
        if find_prime(test):  # 如果是质数
            prime_list.append(test)
            count += 1  # 找到一个质数
        test += 1
# print(prime_list)
result = prime_list[M - 1: N]
# print(result)
output_count = 1
for i in result:
    print(i, end='')
    if output_count < len(result) and output_count % 10 != 0:
        print(' ', end='')
    if output_count % 10 ==0:
        print('\n', end='')
    output_count += 1

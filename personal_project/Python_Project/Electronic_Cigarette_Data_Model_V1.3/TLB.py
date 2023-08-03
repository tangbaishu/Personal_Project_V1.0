
# 函数名称：从字符串中提取连续数
# 注：输入的字符串中不可以存在多段数据，否则会导致提取异常。
def string_open_sql(string_data):
    string_data = str(string_data)
    num_data = [0]*len(string_data)
    # print(num_data)
    # print(string_data)
    ram_data = 0
    num = 0
    j = 0
    k = 1
    n = 0
    m = 1
    minus = 0   # 负数符号
    for num in range(0, len(string_data), 1):   # len()获取字符串长度
        # print(string_data[num])    # ord()将字符转换成ASCII码，例如 ord('d')将转换成100放回
        if ord(string_data[num]) == 45 and j == 0:     # 检索是否存在负号
            minus = 1
        if (ord(string_data[num]) >= 48) and (ord(string_data[num]) <= 57):     # 提取数字
            num_data[j] = string_data[num]
            # print(num_data[j], j, num)
            j += 1
        elif ord(string_data[num]) == 46:
            n = j
            # print("n=", n)
    if n != 0:
        for num in range(n, j, 1):
            m *= 10
        # print("m=", m)
    if j != 0:
        while 1:
            j -= 1
            # print(num_data[j], "j=", j)
            ram_data += int(num_data[j]) * int(k)
            # print(num_data[m])
            if j == 0:
                break
            k *= 10
        if m != 0:
            ram_data /= m
        if minus == 1:
            ram_data = 0 - ram_data
    else:
        ram_data = 0
    return ram_data


def Effective_Length(*num):
    for x in range(0, len(num), 1):
        if num[x] == 0:
            return x


if __name__ == '__main__':
    data = "hdfg6.-0ff4fgdsg6"
    print("start")
    print(string_open_sql(data))

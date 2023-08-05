
# 函数名称：从字符串中提取连续数据
# 注：输入的字符串中不可以存在多段数据，否则会导致提取异常。
def string_open_sql(string_data):
    num_data = [0]*len(string_data)
    num = 0
    j = 1
    k = 1
    n = 0
    m = 1
    for num in range(0, len(string_data), 1):   # len()获取字符串长度
        # print(string_data[num])    # ord()将字符转换成ASCII码，例如 ord('d')将转换成100放回
        if (ord(string_data[num]) >= 48) and (ord(string_data[num]) <= 57):
            num_data[j] = string_data[num]
            # print(num_data[j])
            j += 1
        elif ord(string_data[num]) == 46:
            n = j-1
            # print("n=", n)
    j -= 1
    if n != 0:
        for num in range (n, j, 1):
            m *= 10
        # print("m=", m)
    while 1:
        # print(num_data[j], "j=", j)
        num_data[0] += int(num_data[j]) * int(k)
        # print(num_data[m])
        j -= 1
        if j == 0:
            break
        k *= 10
    if m != 0:
        num_data[0] /= m
    # print(num_data[0])
    return num_data[0]


def Effective_Length(*num):
    for x in range(0, len(num), 1):
        if num[x] == 0:
            return x


if __name__ == '__main__':
    data = "wsifjisj8765.3fgfz456"
    print("start")
    string_open_sql(data)

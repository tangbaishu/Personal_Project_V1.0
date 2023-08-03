import xlrd     # 引入Excel库的xlrd
import numpy
import matplotlib
import scipy
import xlutils.copy

import matplotlib.pyplot as plt
import numpy as np

import TLB

Array_Len = 114

# Excel_Data=xlrd.open_workbook(r'C:\Users\WX\Desktop\工作文件\项目\内研项目\防干烧\\2S—20230210.xls')
# 'C:\Users\WX\Desktop\工作文件\项目\内研项目\防干烧\2S—20230210.xls'
Excel_Data = xlrd.open_workbook(r'C:\Users\WX\Desktop\2S—20230210.xls')
Excel_Sheets0_Data = Excel_Data.sheets()[0]

# import xlrd

# #打开一个workbook
# filename = r'C:\Users\WX\Desktop\2S—20230210.xls'
# rb = xlrd.open_workbook(filename, encoding_override="utf-8")
# wb = xlutils.copy.copy(rb)
# #获取sheet对象，通过sheet_by_index()获取的sheet对象没有write()方法
# ws = wb.get_sheet(0)
# #写入数据
# ws.write(1, 1, 'GG')
# #添加sheet页
# wb.add_sheet('sheetnnn2',cell_overwrite_ok=True)
# #利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
# wb.save(filename)

num = 0
excel_char_data = ['A'] * Array_Len
excel_data0 = [0] * Array_Len
excel_data1 = [0] * Array_Len

for num in range(0, Array_Len, 1):
    if Excel_Sheets0_Data[num][0] == '\0':
        break
    excel_char_data[num] = str(Excel_Sheets0_Data[num][0])
    # print(excel_char_data[num])
    excel_data0[num] = TLB.string_open_sql(excel_char_data[num])
    # print(excel_data0[num])

for num in range(0, Array_Len, 1):
    if Excel_Sheets0_Data[num][1] == '\0':
        print("num=", num)
        break
    excel_char_data[num] = str(Excel_Sheets0_Data[num][1])
    # print(excel_char_data[num])
    excel_data1[num] = TLB.string_open_sql(excel_char_data[num])
    # print(excel_data1[num])
# plt.plot(excel_data1, excel_data0, color='r')

x0_len = 0
x_len = [2, 10]
number_of_fits = [1, 3]

for duty in range(0, len(x_len), 1):
    x0_len = x_len[duty]
    x0 = [0] * x0_len
    y0 = [0] * x0_len
    print(x_len[duty])
    for num in range(0, x0_len, 1):
        if duty == 0:
            x0[num] = excel_data1[num]
            y0[num] = excel_data0[num]
        else:
            x0[num] = excel_data1[num+x_len[duty-1]]
            y0[num] = excel_data0[num+x_len[duty-1]]
        # print(x0[num])  # 显示待拟合曲线的X轴数据
    plt.plot(x0, y0, color='b')

    z0 = np.polyfit(x0, y0, number_of_fits[duty])
    k0 = np.poly1d(z0)  # 使用次数合成多项式
    y0 = k0(x0)
    print("k0=", k0)
    plt.plot(x0, y0, color='r')
    plt.show()



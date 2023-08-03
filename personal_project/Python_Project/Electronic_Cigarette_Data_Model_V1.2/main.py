import xlrd  # 引入Excel库的xlrd
import numpy
import matplotlib
import scipy
import xlutils.copy

import matplotlib.pyplot as plt
import numpy as np
import xlsxwriter as xw

import TLB
# import DataBase

Array_Len = 1233

filename = r'C:\Users\WX\Desktop\WorkFile\E-Cigarette_Data Model\Discharge Characteristic Data\RAM_DATA.xls'
Excel_Data = xlrd.open_workbook(r'C:\Users\WX\Desktop\WorkFile\E-Cigarette_Data Model\Discharge Characteristic Data\RAM_DATA.xls')
Excel_Sheets0_Data = Excel_Data.sheets()[0]

# import xlrd

# #打开一个workbook
#
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
    if num == 0:
        excel_char_data[num] = str(Excel_Sheets0_Data[1][0])
        excel_data0[num] = TLB.string_open_sql(excel_char_data[num])
        num += 1
    # if Excel_Sheets0_Data[num][0] == '\0':
    #     break
    excel_char_data[num] = str(Excel_Sheets0_Data[num][0])
    # print(excel_char_data[num])
    excel_data0[num] = TLB.string_open_sql(excel_char_data[num])
    # print(excel_data0[num])

for num in range(0, Array_Len, 1):
    if num == 0:
        excel_char_data[num] = str(Excel_Sheets0_Data[1][1])
        excel_data1[num] = TLB.string_open_sql(excel_char_data[num])
        num += 1
    # if Excel_Sheets0_Data[num][1] == '\0':
    #     print("num=", num)
    #     break
    excel_char_data[num] = str(Excel_Sheets0_Data[num][1])
    # print(excel_char_data[num])
    excel_data1[num] = TLB.string_open_sql(excel_char_data[num])
    # print(excel_data1[num])

plt.plot(excel_data1, excel_data0, '.')   # color 曲线颜色、linestyle曲线样式
# plt.show()

x0_len = 0
x_len = [250, 60, 0]
number_of_fits = [8, 8, 6]
k = [0]*len(x_len)
adr = 0
data_x0 = [0] * Array_Len
data_y0 = [0] * Array_Len


for duty in range(0, len(x_len), 1):
    for num in range(0, Array_Len, 1):
        if duty == 0:
            if excel_data1[num] > x_len[duty]:
                data_x0[num] = excel_data1[num]
                data_y0[num] = excel_data0[num]
            else:
                adr = num
                break
        else:
            if (excel_data1[num + adr] > x_len[duty]) and ((num + adr) < (Array_Len-1)):
                data_x0[num] = excel_data1[num + adr]
                data_y0[num] = excel_data0[num + adr]
            elif excel_data1[num + adr] < x_len[duty]:
                adr = adr + num
                break
            elif (num + adr) == (Array_Len-1):
                data_x0[num] = excel_data1[num + adr]
                data_y0[num] = excel_data0[num + adr]
                num += 1
                break
        # print(data_x0[num], num+adr)  # 显示待拟合曲线的X轴数据
    x0 = [0] * num
    y0 = [0] * num
    length = num
    print("num=", num)
    print("duty=", duty)

    for num in range(0, length, 1):
        x0[num] = data_x0[num]
        y0[num] = data_y0[num]
        # print(x0[num])  # 显示待拟合曲线的X轴数据
    # plt.plot(x0, y0, '-')
    z0 = np.polyfit(x0, y0, number_of_fits[duty])
    k[duty] = np.poly1d(z0)  # 使用次数合成多项式
    print(z0)
    print("y=", k[duty])
    y0 = k[duty](x0)
    # plt.plot(x0, y0, color='r')
    # plt.show()

wb = xlutils.copy.copy(Excel_Data)
# 获取sheet对象，通过sheet_by_index()获取的sheet对象没有write()方法
ws = wb.get_sheet(0)
# 写入数据
for num in range(0, Array_Len, 1):
    if excel_data1[num] == 0:
        data_y0[num] = excel_data0[Array_Len-1]
    else:
        if excel_data1[num] > x_len[0]:
            data_y0[num] = k[0](excel_data1[num])
        elif excel_data1[num] > x_len[1]:
            data_y0[num] = k[1](excel_data1[num])
        elif excel_data1[num] > x_len[2]:
            data_y0[num] = k[2](excel_data1[num])
    # elif excel_data1[num] > x_len[3]:
    #     data_y0[num] = k[3](excel_data1[num])
    # ws.write(num, 2, data_y0[num])

plt.plot(excel_data1, data_y0, color='r')

if __name__ == '__main__':
    # wb.save(filename)
    plt.show()

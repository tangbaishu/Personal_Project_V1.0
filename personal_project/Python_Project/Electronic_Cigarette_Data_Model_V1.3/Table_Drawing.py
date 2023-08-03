# 基于特定.xls文件绘制图表

import xlrd  # 引入Excel库的xlrd
import xlutils.copy
import TLB
import matplotlib.pyplot as plt
import numpy as np

Excel_Data = xlrd.open_workbook(r'C:\Users\WX\Desktop\Python\600V2_V1.1.xls')
Excel_Sheets0_Data = Excel_Data.sheets()[0]
# Excel_Sheets12_Data = Excel_Data.sheets()[12]
Array_Len = 19

x0 = [0] * Array_Len
y0 = [0] * Array_Len
x1 = [0] * Array_Len
y1 = [0] * Array_Len


if __name__ == '__main__':
    t0 = 0
    for num in range(1, Array_Len+1, 1):
        x0[num-1] = str(Excel_Sheets0_Data[num][0])
        x0[num-1] = TLB.string_open_sql(x0[num-1])
        y0[num-1] = str(Excel_Sheets0_Data[num][12])
        y0[num-1] = TLB.string_open_sql(y0[num-1])
        # x1[num] = str(Excel_Sheets0_Data[num][2])
        # x1[num] = TLB.string_open_sql(x1[num])
        # y1[num] = str(Excel_Sheets0_Data[num][3])
        # y1[num] = TLB.string_open_sql(y1[num])
    for num in range(0, Array_Len, 1):
        print(x0[num])
        print(y0[num])
    plt.plot(x0, y0, color='r', linestyle='-')
    plt.plot(x1, y1, color='b', linestyle='-')
    plt.show()


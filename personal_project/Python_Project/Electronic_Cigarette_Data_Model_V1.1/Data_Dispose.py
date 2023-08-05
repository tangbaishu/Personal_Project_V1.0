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

Array_Len = 489

filename = r'C:\Users\WX\Desktop\Python\VBAT_Data_Dispose.xls'
Excel_Data = xlrd.open_workbook(r'C:\Users\WX\Desktop\Python\VBAT_Data_Dispose.xls')
Excel_Sheets0_Data = Excel_Data.sheets()[0]
wb = xlutils.copy.copy(Excel_Data)
ws = wb.get_sheet(0)

Sheets0_2_Data = [0] * Array_Len
Sheets0_3_Data = [0] * Array_Len

if __name__ == '__main__':
    for num in range(0, Array_Len, 1):
        Sheets0_2_Data[num] = str(Excel_Sheets0_Data[num][1])
        Sheets0_2_Data[num] = TLB.string_open_sql(Sheets0_2_Data[num])
        if num == 0:
            Sheets0_3_Data[num] = Sheets0_2_Data[num]
        else:
            Sheets0_3_Data[num] = Sheets0_3_Data[num-1] + Sheets0_2_Data[num]
        print(Sheets0_3_Data[num])
        ws.write(num, 2, Sheets0_3_Data[num])
        wb.save(filename)

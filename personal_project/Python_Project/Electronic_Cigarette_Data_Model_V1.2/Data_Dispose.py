import xlrd  # 引入Excel库的xlrd
import numpy
import matplotlib
import scipy
import xlutils.copy

import matplotlib.pyplot as plt
import numpy as np
import xlsxwriter as xw
import openpyxl
import TLB
# import DataBase

Array_Len = 489

filename = r'D:\Desktop\Python\VBAT_Data_Dispose.xlsx'
Excel_Data = openpyxl.load_workbook(filename)
Excel_Sheets0_Data = Excel_Data['xd']
# wb = xlutils.copy.copy(Excel_Data)
# ws = wb.get_sheet(0)

Sheets0_2_Data = [0] * Array_Len
Sheets0_3_Data = [0] * Array_Len

if __name__ == '__main__':
    for num in range(1, Array_Len, 1):
        Sheets0_2_Data[num] = str(Excel_Sheets0_Data[num][1])
        Sheets0_2_Data[num] = TLB.string_open_sql(Sheets0_2_Data[num])
        if num == 0:
            Sheets0_3_Data[num] = Sheets0_2_Data[num]
        else:
            Sheets0_3_Data[num] = Sheets0_3_Data[num-1] + Sheets0_2_Data[num]
        print(Sheets0_3_Data[num])
        Excel_Sheets0_Data.cell(num, 2).value = Sheets0_3_Data[num]
        Excel_Data.save(filename)

# 功能一：Test_Data() 基于特定的电压点，推导对应功率，保存到对应的.xls表格
# 功能二：基于电池放电特性：容量-电压曲线，推导恒压输出或恒功率输出时对应的电压、功率、口数关系表

import TLB
import main
import xlrd  # 引入Excel库的xlrd
import matplotlib.pyplot as plt
import xlutils.copy

# import numpy as np

Data_Framework = {"初始电压": 4.179592, "电池内阻": 20, "红线线长": 60.0, "黑线线长": 52.0, "蓝线线长": 27.0,
                  "线号线阻": 227.0, "mos内阻": 60.0, "发热丝阻值": 1.2, "恒压输出": 3.6, "目标功率": 0,
                  "每口工作时间(s)": 2.0, "每组口数": 1,
                  "总容量": 317}
# :"发热丝阻值": 1.163
# Data_Framework = {"初始电压": 4.22, "电池内阻": 110.0, "红线线长": 30.0, "黑线线长": 0.0, "蓝线线长": 45.0,
#                   "线号线阻": 143.0, "mos内阻": 30.0, "发热丝阻值": 0.8, "恒压输出": 0.0, "目标功率": 15,
#                   "每口工作时间(s)": 2.0, "每组口数": 20,
#                   "总容量": 289}

Process_Data = {"回路总阻抗": 0.0, "输出端阻抗": 0.0, "输入端阻抗": 0.0, "ON电流": 0.0, "AT_ON电压": 0.0,
                "消耗电量": 0.0, "剩余电量": 0.0, "剩余电压": 0.0,
                "VDD电压": 0.0, "占空比": 0.0, "AT输出功率": 0.0, "AT输出电压": 0.0,
                "工作时间": 0.0, "累计口数": 0}

title = ['电池电压(V)', '电池内阻(mΩ)', '红线线长(mm)', '黑线线长(mm)', '蓝线线长(mm)', '30#线号',
         'MOS内阻(mΩ)', '发热丝阻值(Ω)', '恒压输出', '目标功率(W)', 'AT_ON电压（V）', 'ON电流(I)', '占空比(D)',
         'AT输出功率(W)', '消耗电量(mAh)', '剩余电量', '累计口数', '工作时间(S)']

shuzu_langth = 1233

Capacity_x = [0] * shuzu_langth
Voltage_y = [0] * shuzu_langth

filename = r"D:\Desktop\Python\600V2_V1.1.xlsx"
# #获取sheet对象，通过sheet_by_index()获取的sheet对象没有write()方法
xls_data = xlrd.open_workbook(filename)
wb = xlutils.copy.copy(xls_data)
ws = wb.get_sheet(0)


def Row_Data_Write(tlb_write_list):
    xls_write_row = 1
    ws.write(tlb_write_list, xls_write_row, Data_Framework["电池内阻"])
    xls_write_row += 1
    ws.write(tlb_write_list, xls_write_row, Data_Framework["红线线长"])
    xls_write_row += 1
    ws.write(tlb_write_list, xls_write_row, Data_Framework["黑线线长"])
    xls_write_row += 1
    ws.write(tlb_write_list, xls_write_row, Data_Framework["蓝线线长"])
    xls_write_row += 1
    ws.write(tlb_write_list, xls_write_row, Data_Framework["线号线阻"])
    xls_write_row += 1
    ws.write(tlb_write_list, xls_write_row, Data_Framework["mos内阻"])
    xls_write_row += 1
    ws.write(tlb_write_list, xls_write_row, Data_Framework["发热丝阻值"])
    if Data_Framework["恒压输出"] != 0:
        xls_write_row += 1
        ws.write(tlb_write_list, xls_write_row, Data_Framework["恒压输出"])
    if Data_Framework["目标功率"] != 0:
        xls_write_row += 1
        ws.write(tlb_write_list, xls_write_row, Data_Framework["目标功率"])
    xls_write_row += 1
    ws.write(tlb_write_list, xls_write_row, Process_Data["AT_ON电压"])
    xls_write_row += 1
    ws.write(tlb_write_list, xls_write_row, Process_Data["ON电流"])
    xls_write_row += 1
    ws.write(tlb_write_list, xls_write_row, Process_Data["占空比"])
    xls_write_row += 1
    ws.write(tlb_write_list, xls_write_row, Process_Data["AT输出功率"])
    xls_write_row += 1
    ws.write(tlb_write_list, xls_write_row, Process_Data["消耗电量"])
    xls_write_row += 1
    ws.write(tlb_write_list, xls_write_row, Process_Data["剩余电量"])
    xls_write_row += 1
    ws.write(tlb_write_list, xls_write_row, Process_Data["累计口数"])
    xls_write_row += 1
    ws.write(tlb_write_list, xls_write_row, Process_Data["工作时间"])
    xls_write_row += 1


def xls_Data_Write(init, tlb_write_list):
    xls_write_row = 0
    if init == 1:  # 初始化阶段
        for num in range(0, len(title), 1):
            if num == 8:
                if Data_Framework["恒压输出"] != 0:
                    ws.write(tlb_write_list, xls_write_row, title[num])
                    xls_write_row += 1
                else:
                    num += 1
                    xls_write_row -= 1
            if num == 9:
                if Data_Framework["目标功率"] != 0:
                    ws.write(tlb_write_list, xls_write_row, title[num])
                    xls_write_row += 1
                else:
                    num += 1
                    xls_write_row -= 1
            else:
                ws.write(tlb_write_list, xls_write_row, title[num])
                xls_write_row += 1
        tlb_write_list += 1
        ws.write(tlb_write_list, 0, Data_Framework["初始电压"])
        Row_Data_Write(tlb_write_list)
    else:
        ws.write(tlb_write_list, 0, Process_Data["剩余电压"])
        Row_Data_Write(tlb_write_list)


# 电子烟各项数据推导函数 init==1 第一次推导， init==0 顺推
def Formula(init):
    if init == 0:
        first_voltage = Data_Framework["初始电压"]
    else:
        first_voltage = Process_Data["剩余电压"]

    Process_Data["ON电流"] = first_voltage / Process_Data["回路总阻抗"]
    Process_Data["ON电流"] = round(Process_Data["ON电流"], 2)
    Process_Data["AT_ON电压"] = Process_Data["ON电流"] * Process_Data["输出端阻抗"]
    Process_Data["AT_ON电压"] = round(Process_Data["AT_ON电压"], 3)

    if Data_Framework["恒压输出"] != 0:
        if Process_Data["AT_ON电压"] <= Data_Framework["恒压输出"]:
            Process_Data["VDD电压"] = first_voltage - Process_Data["ON电流"] * Process_Data["输入端阻抗"]
            Process_Data["AT输出功率"] = Process_Data["ON电流"] * Process_Data["AT_ON电压"]
            Process_Data["消耗电量"] = Process_Data["ON电流"] * 1000 * Data_Framework["每口工作时间(s)"] * Data_Framework["每组口数"] / 3600
            Process_Data["占空比"] = 1
        else:
            Process_Data["占空比"] = Data_Framework["恒压输出"] / Process_Data["AT_ON电压"]
            Process_Data["占空比"] = round(Process_Data["占空比"], 6)
            Process_Data["VDD电压"] = first_voltage - Process_Data["ON电流"] * Process_Data["输入端阻抗"]
            Process_Data["VDD电压"] = round(Process_Data["VDD电压"], 3)
            Process_Data["AT输出电压"] = Process_Data["AT_ON电压"] * Process_Data["占空比"]
            Process_Data["AT输出功率"] = Process_Data["ON电流"] * Process_Data["AT_ON电压"] * Process_Data["占空比"]
            Process_Data["消耗电量"] = Process_Data["ON电流"] * 1000 * Process_Data["占空比"] * Data_Framework["每口工作时间(s)"] * Data_Framework["每组口数"] / 3600
    else:
        Process_Data["AT输出功率"] = Process_Data["ON电流"] * Process_Data["AT_ON电压"]
        if Process_Data["AT输出功率"] <= Data_Framework["目标功率"]:
            Process_Data["VDD电压"] = first_voltage - Process_Data["ON电流"] * Process_Data["输入端阻抗"]
            Process_Data["AT输出功率"] = Process_Data["ON电流"] * Process_Data["AT_ON电压"]
            Process_Data["消耗电量"] = Process_Data["ON电流"] * 1000 * Data_Framework["每口工作时间(s)"] * Data_Framework["每组口数"] / 3600
            Process_Data["占空比"] = 1
        else:
            Process_Data["VDD电压"] = first_voltage - Process_Data["ON电流"] * Process_Data["输入端阻抗"]
            Process_Data["占空比"] = Data_Framework["目标功率"] / Process_Data["AT输出功率"]
            Process_Data["占空比"] = round(Process_Data["占空比"], 6)
            Process_Data["AT输出电压"] = Process_Data["AT_ON电压"] * Process_Data["占空比"]
            Process_Data["AT输出功率"] = Process_Data["ON电流"] * Process_Data["AT_ON电压"] * Process_Data["占空比"]
            Process_Data["消耗电量"] = Process_Data["ON电流"] * 1000 * Process_Data["占空比"] * Data_Framework["每口工作时间(s)"] * Data_Framework["每组口数"] / 3600
    # Process_Data["AT输出功率"] = round(Process_Data["AT输出功率"], 3)
    if init == 0:
        Process_Data["剩余电量"] = Data_Framework["总容量"] - Process_Data["消耗电量"]
    else:
        Process_Data["剩余电量"] = Process_Data["剩余电量"] - Process_Data["消耗电量"]
    Process_Data["累计口数"] = Data_Framework["每组口数"] * init
    Process_Data["工作时间"] = Data_Framework["每口工作时间(s)"] * Process_Data["累计口数"]


def Data_Init():
    value0 = 0.0
    value1 = 0.0
    value0 = Data_Framework["红线线长"] * Data_Framework["线号线阻"] / 1000 / 1000
    Process_Data["输入端阻抗"] = Data_Framework["电池内阻"] / 1000 + value0
    value1 = Data_Framework["黑线线长"] + Data_Framework["蓝线线长"]
    Process_Data["输出端阻抗"] = value1 * Data_Framework["线号线阻"] / 1000 / 1000 + Data_Framework["发热丝阻值"]
    Process_Data["回路总阻抗"] = Process_Data["输入端阻抗"] + Process_Data["输出端阻抗"] + Data_Framework["mos内阻"] / 1000
    Formula(0)
    xls_Data_Write(1, 0)
    Capacity_x[0] = Process_Data["剩余电量"]
    Voltage_y[0] = Data_Framework["初始电压"]
    print("回路总阻抗", Process_Data["回路总阻抗"])
    print("输出端阻抗", Process_Data["输出端阻抗"])
    print("输入端阻抗", Process_Data["输入端阻抗"])
    print("ON电流", Process_Data["ON电流"])
    print("AT_ON电压", Process_Data["AT_ON电压"])
    print("AT输出电压", Process_Data["AT输出电压"])
    print("占空比", Process_Data["占空比"])
    print("VDD电压", Process_Data["VDD电压"])
    print("AT输出功率", Process_Data["AT输出功率"])
    print("消耗电量", Process_Data["消耗电量"])
    print("剩余电量", Process_Data["剩余电量"])
    print("\r\n")

# def fitting_function(x, k):
#     y = 0.0
#     if k == 1:
#         y = -3.913e-14 * x + 1.342e-10 * x - 1.788e-07 * x + 0.0001014 * x + 0.001307 * x
#         - 34.43 * x + 1.953e+04 * x - 4.775e+06 * x + 4.546e+08
#     elif k == 2:
#         y = -6.952e-21 * x + 1.7e-17 * x - 1.751e-14 * x + 9.92e-12 * x + 3.393e-09 * x +\
#             7.276e-07 * x - 9.735e-05 * x + 0.008008 * x + 3.203
#     elif k == 3:
#         y = -9.92e-10 * x + 1.469e-07 * x - 8.566e-06 * x + 0.0002547 * x - 0.004401 * x + 0.05688 * x + 2.82
#         yw = main.k[0](x)
#     print(yw)
#     print(y)
#     return y


Test_Voltage = [4.1, 4.0, 3.9, 3.8, 3.7, 3.6, 3.5, 3.4, 3.3, 3.2, 3.1, 3.0]


def Test_Data():
    xls_write_row = 2
    Data_Init()
    for Votage_adr in range(0, len(Test_Voltage), 1):
        Process_Data["剩余电压"] = Test_Voltage[Votage_adr]
        print("剩余电压=", Process_Data["剩余电压"])
        Formula(Votage_adr+1)
        xls_Data_Write(0, xls_write_row+Votage_adr)


def Per_port_Modeing():
    shuzu_adr = 1
    xls_write_row = 2
    while 1:
        if Process_Data["剩余电量"] <= 0:
            break
        if Process_Data["剩余电量"] > main.x_len[0]:
            Process_Data["剩余电压"] = main.k[0](Process_Data["剩余电量"])
        elif Process_Data["剩余电量"] > main.x_len[1]:
            Process_Data["剩余电压"] = main.k[1](Process_Data["剩余电量"])
        elif Process_Data["剩余电量"] > main.x_len[2]:
            Process_Data["剩余电压"] = main.k[2](Process_Data["剩余电量"])
        Formula(shuzu_adr)
        Capacity_x[shuzu_adr] = Process_Data["剩余电量"]
        Voltage_y[shuzu_adr] = Process_Data["剩余电压"]
        shuzu_adr += 1
        # print(Process_Data["消耗电量"])
        # print(Process_Data["剩余电压"], Process_Data["剩余电量"])
        xls_Data_Write(0, xls_write_row)
        xls_write_row += 1


if __name__ == '__main__':
    # Test_Data()
    Data_Init()
    Per_port_Modeing()
    num = TLB.Effective_Length(*Capacity_x)
    print(num)
    Cap_x = [0] * num
    Vol_y = [0] * num
    for x in range(0, num, 1):
        Cap_x[x] = Capacity_x[x]
        Vol_y[x] = Voltage_y[x]
    plt.plot(Cap_x, Vol_y, color='black', linestyle='-')
    plt.show()
    wb.save(filename)

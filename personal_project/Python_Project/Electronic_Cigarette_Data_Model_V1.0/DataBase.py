import TLB
import main
import xlrd  # 引入Excel库的xlrd
import matplotlib.pyplot as plt
import xlutils.copy

# import numpy as np

Data_Framework = {"初始电压": 3.984, "电池内阻": 100.0, "红线线长": 25.0, "黑线线长": 60.0, "蓝线线长": 55.0,
                  "线号线阻": 321.0, "mos内阻": 100.0, "发热丝阻值": 1.4, "恒压输出": 3.6,
                  "每口工作时间(s)": 2.0, "每组口数": 1,
                  "目标功率": 0, "总容量": 600}

Process_Data = {"回路总阻抗": 0.0, "输出端阻抗": 0.0, "ON电流": 0.0, "占空比": 0.0, "AT输出功率": 0.0, "消耗电量": 0.0,
                "剩余电量": 0.0, "剩余电压": 0.0, "工作时间": 0.0, "累计口数": 0}

title = ['电池电压(V)', '电池内阻(mΩ)', '红线线长(mm)', '黑线线长(mm)', '蓝线线长(mm)', '30#线号',
         'MOS内阻(mΩ)', '发热丝阻值(Ω)', '恒压输出', '目标功率(W)', 'ON电流(I)', '占空比(D)',
         'AT输出功率(W)', '消耗电量(mAh)', '剩余电量', '累计口数', '工作时间(S)']

shuzu_langth = 1000

Capacity_x = [0] * shuzu_langth
Voltage_y = [0] * shuzu_langth

filename = r'C:\Users\WX\Desktop\600V2_V1.0.xls'
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


def Data_Init():
    value0 = 0.0
    value1 = 0.0
    Process_Data["回路总阻抗"] = Data_Framework["电池内阻"] / 1000
    value0 = Data_Framework["红线线长"] * Data_Framework["线号线阻"] / 1000 / 1000
    value1 = Data_Framework["黑线线长"] / 2 + Data_Framework["蓝线线长"]
    Process_Data["输出端阻抗"] = value1 * Data_Framework["线号线阻"] / 1000 / 1000 + Data_Framework["发热丝阻值"] + \
                                 Data_Framework["mos内阻"] / 1000
    Process_Data["回路总阻抗"] = Process_Data["回路总阻抗"] + value0 + Process_Data["输出端阻抗"]
    Process_Data["ON电流"] = Data_Framework["初始电压"] / Process_Data["回路总阻抗"]
    if Data_Framework["恒压输出"] != 0:
        Process_Data["AT输出功率"] = Data_Framework["恒压输出"] * Data_Framework["恒压输出"] / Process_Data["输出端阻抗"]
        if Data_Framework["初始电压"] < Data_Framework["恒压输出"]:
            Process_Data["消耗电量"] = Process_Data["ON电流"] * 1000 * Data_Framework["每口工作时间(s)"] * Data_Framework["每组口数"] / 3600
            Process_Data["占空比"] = 1
        else:
            Process_Data["占空比"] = Data_Framework["恒压输出"] / Data_Framework["初始电压"]
            Process_Data["消耗电量"] = Process_Data["ON电流"] * 1000 * Process_Data["占空比"] * \
                                       Data_Framework["每口工作时间(s)"] * Data_Framework["每组口数"] / 3600
    Process_Data["剩余电量"] = Data_Framework["总容量"] - Process_Data["消耗电量"]
    Process_Data["工作时间"] = Data_Framework["每口工作时间(s)"] * Data_Framework["每组口数"]
    Process_Data["累计口数"] = Data_Framework["每组口数"] * 1
    xls_Data_Write(1, 0)
    Capacity_x[0] = Process_Data["剩余电量"]
    Voltage_y[0] = Data_Framework["初始电压"]
    # print(Process_Data["回路总阻抗"])
    # print(Process_Data["输出端阻抗"])
    # print(Process_Data["ON电流"])
    # print(Process_Data["AT输出功率"])
    # print(Process_Data["消耗电量"])
    # print(Process_Data["剩余电量"])
    # print("\r\n")
    # print("\r\n")
    # print("\r\n")


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


def Per_port_Modeing():
    num = 1
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

        Process_Data["ON电流"] = Process_Data["剩余电压"] / Process_Data["回路总阻抗"]
        if Data_Framework["恒压输出"] != 0:
            if Process_Data["剩余电压"] > Data_Framework["恒压输出"]:
                Process_Data["AT输出功率"] = Data_Framework["恒压输出"] * Data_Framework["恒压输出"] / Process_Data["输出端阻抗"]
                Process_Data["占空比"] = Data_Framework["恒压输出"] / Process_Data["剩余电压"]
                Process_Data["消耗电量"] = Process_Data["ON电流"] * Process_Data["占空比"] * 1000 *\
                                           Data_Framework["每口工作时间(s)"] * Data_Framework["每组口数"] / 3600
            else:
                Process_Data["AT输出功率"] = Process_Data["剩余电压"] * Process_Data["剩余电压"] / Process_Data["输出端阻抗"]
                Process_Data["占空比"] = 1
                Process_Data["消耗电量"] = Process_Data["ON电流"] * 1000 * Data_Framework["每口工作时间(s)"] * \
                                           Data_Framework["每组口数"] / 3600
        Process_Data["剩余电量"] = Process_Data["剩余电量"] - Process_Data["消耗电量"]
        Capacity_x[num] = Process_Data["剩余电量"]
        Voltage_y[num] = Process_Data["剩余电压"]
        num += 1
        Process_Data["工作时间"] = Data_Framework["每口工作时间(s)"] * Data_Framework["每组口数"] * num
        Process_Data["累计口数"] = Data_Framework["每组口数"] * num
        # print(Process_Data["消耗电量"])
        # print(Process_Data["剩余电压"], Process_Data["剩余电量"])
        xls_Data_Write(0, xls_write_row)
        xls_write_row += 1


if __name__ == '__main__':
    Data_Init()
    Per_port_Modeing()
    num = TLB.Effective_Length(*Capacity_x)
    print(num)
    Cap_x = [0] * num
    Vol_y = [0] * num
    for x in range(0, num, 1):
        Cap_x[x] = Capacity_x[x]
        Vol_y[x] = Voltage_y[x]
    plt.plot(Cap_x, Vol_y, color='green', linestyle='-')
    plt.show()
    wb.save(filename)
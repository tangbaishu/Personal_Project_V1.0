import numpy as np

import matplotlib.pyplot as plt
import csv
from scipy import optimize
# import xlwt
# import pandas as pd
#  import scipy.optimize as optimize
import random

import operator
from functools import reduce
# file = "E:\\desk\\2021-5-20-19-17-45-SaveData.csv"
file ="E:\\desk\\2022-6-22-19-35-54-SaveData.csv"
# file="E:\\A1semi\\9072DT-M\\2021-8-20-12-1-59-SaveData.csv"
# file="E:\\A1semi\\水位检测\\2022-1-26-19-36-44-SaveData.csv"
# file="E:\\A1semi\\视频\\拓邦咖啡机\\2022-2-9-17-55-19-SaveData.csv"

am = sum(1 for line in open (file))
average =1
amount = int(am/average)
# amount=7000
# amount=70000
# amount=50
print(amount)
average_enable=0               #是否计算平均值
c = [[0] * 3] * amount
t = [0]*amount

channel1 = [0]*amount
channel2 = [0]*amount
channel3 = [0]*amount
channel4 = [0]*amount
channel5 = [0]*amount
channel6 = [0]*amount
channel7 = [0]*amount
channel8 = [0]*amount
channel9 = [0]*amount
channel10 = [0]*amount
channel11 = [0]*amount
channel12 = [0]*amount
channel13 = [0]*amount
channel14 = [0]*amount
channel15 = [0]*amount
c1=[0]*amount
c2=[0]*amount

with open(file) as f:
    reader = csv.reader(f)
    x = [row[0] for row in reader]
with open(file) as f:
    reader = csv.reader(f)
    ch1 = [row[1] for row in reader]
with open(file) as f:
    reader = csv.reader(f)
    ch2 = [row[2] for row in reader]
with open(file) as f:
    reader = csv.reader(f)
    ch3 =[row[3] for row in reader]
with open(file) as f:
    reader = csv.reader(f)
    ch4 =[row[4] for row in reader]
with open(file) as f:
    reader = csv.reader(f)
    ch5 =[row[5] for row in reader]
with open(file) as f:
    reader = csv.reader(f)
    ch6 =[row[6] for row in reader]
# with open(file) as f:
#     reader = csv.reader(f)
#     ch7 =[row[7] for row in reader]
# with open(file) as f:
#     reader = csv.reader(f)
#     ch8 =[row[8] for row in reader]
# with open(file) as f:
#     reader = csv.reader(f)
#     ch9 =[row[9] for row in reader]
# with open(file) as f:
#     reader = csv.reader(f)
#     ch10 =[row[10] for row in reader]

# with open(file) as f:
#     reader = csv.reader(f)
#     ch11 = [row[11] for row in reader]
# with open(file) as f:
#     reader = csv.reader(f)
#     ch12 = [row[12] for row in reader]
# with open(file) as f:
#     reader = csv.reader(f)
#     ch13 =[row[13] for row in reader]
# with open(file) as f:
#     reader = csv.reader(f)
#     ch14 =[row[14] for row in reader]
# with open(file) as f:
#     reader = csv.reader(f)
#     ch15 =[row[15] for row in reader]

# for i in range(0, am):
#         channel1[i] = int(ch1[i])
#         channel2[i] = int(ch2[i])
#         channel3[i] = int(ch3[i])
#
#         channel4[i] = int(ch4[i])
#         channel5[i] = int(ch5[i])
#         channel6[i] = int(ch6[i])


add1=add2=add3=add4=add5=add6=0
if (average_enable==0):
    for i in range(0, amount):
        channel1[i] = 65535-(int(ch1[i]))
        channel2[i] = 65535-(int(ch2[i]))
        channel3[i] =(int(ch3[i]))
        channel4[i] = int(ch4[i])
        channel5[i] = int(ch5[i])
        channel6[i] = int(ch6[i])
        # channel6[i] = int(ch6[i])
        # channel7[i] = int(ch7[i])
        # channel8[i] = int(ch8[i])
        # channel9[i] = int(ch9[i])
        # channel10[i] = int(ch10[i])
        # channel11[i] = int(ch11[i])
        # channel12[i] = int(ch12[i])
        # channel13[i] = int(ch13[i])
        # channel14[i] = int(ch14[i])
        # channel15[i] = int(ch15[i])

        t[i] = i
else:
    for i in range(0, amount):
        for j in range(0,average):
            add1 = add1+int(ch1[i*average+j])
            add2 =add2+(6553 - int((int(ch2[i*average+j])) / 10))
            add3 =add3+(6553 - int((int(ch3[i*average+j])) / 10))
            # add4 =add4+(6553 - int((int(ch4[i*average+j])) / 10))
            #
            # add5 = add5+(int(ch5[i*average+j]))
            # add6= add6+(int(ch6[i*average+j]))
        t[i] = i
        channel2[i]=add1/average
        channel2[i]=add2/average
        channel3[i]=add3/average
        # channel4[i]=add4/average
        # channel5[i]=add5/average
        add1 = add2 = add3 = add4 = add5 = add6 = 0
# for i in range(0, amount):
#     c1[i]=33491-channel1[i]
#     c2[i]=33583-channel2[i]
print("max(channel1)-min(channel1):",max(channel1)-min(channel1))
print("max(channel2)-min(channel2):",max(channel2)-min(channel2))
print("max(channel2)",max(channel2))
print("min(channel2)",min(channel2))

# print("max(channel3)-min(channel3):",max(channel3)-min(channel3))
# print("max(channel4)-min(channel4):",max(channel4)-min(channel4))
# print("max(channel5)-min(channel5):",max(channel5)-min(channel5))
# print("max(channel6)-min(channel6):",max(channel6)-min(channel6))
# print("max(channel7)-min(channel7):",max(channel7)-min(channel7))
# print("max(channel8)-min(channel8):",max(channel8)-min(channel8))
# print("max(channel9)-min(channel9):",max(channel9)-min(channel9))
# print("max(channel10)-min(channel10):",max(channel10)-min(channel10))

# print("max(channel11)-min(channel11):",max(channel11)-min(channel11))
# print("max(channel12)-min(channel12):",max(channel12)-min(channel12))
# print("max(channel13)-min(channel13):",max(channel13)-min(channel13))
# print("max(channel14)-min(channel14):",max(channel14)-min(channel14))
# print("max(channel15)-min(channel15):",max(channel15)-min(channel15))
#

# Ch1_Fil_Num=0
# Ch2_Fil_Num=0
# Ch3_Fil_Num=0
#
#
# t_c1=[0]*amount
# t_c2=[0]*amount
# t_c3=[0]*amount
# t_c4=[0]*amount
# t_c5=[0]*amount
#
# k1=((max(channel6)-min(channel6))/(max(channel10)-min(channel10)))
# k2=((max(channel7)-min(channel7))/(max(channel10)-min(channel10)))
# k3=((max(channel8)-min(channel8))/(max(channel10)-min(channel10)))
# k4=((max(channel9)-min(channel9))/(max(channel10)-min(channel10)))
#
# print("k1:",k1)
# print("k2:",k2)
# print("k3:",k3)
# print("k4:",k4)
# # #
# for i in range(0,amount):
#     t_c1[i]=channel6[i]-(channel10[i]-channel10[0])*k1
#     t_c2[i]=channel7[i]-(channel10[i]-channel10[0])*k2
#     t_c3[i]=channel8[i]-(channel10[i]-channel10[0])*k3
#     t_c4[i]=channel9[i]-(channel10[i]-channel10[0])*k4
#
# print("补偿后：")
# print("max(c1)-min(c1):",max(t_c1)-min(t_c1))
# print("max(c2)-min(c2):",max(t_c2)-min(t_c2))
# print("max(c3)-min(c3):",max(t_c3)-min(t_c3))
# print("max(c4)-min(c4):",max(t_c4)-min(t_c4))

# plt.plot(t,channel1,color='r')
plt.plot(t,channel2,color='r')
# plt.plot(t,channel3,color='b')
# plt.plot(t,channel1,color='g')

# plt.plot(t,channel4,color='k',linestyle='--')
# plt.plot(t,channel5,color='k',linestyle='--')
# #
# plt.plot(t,channel6,color='k',linestyle='--')
# plt.plot(t,channel7,color='b')
# plt.plot(t,channel8,color='b')
# plt.plot(t,channel9,color='b')
# plt.plot(t,channel10,color='b')

# plt.plot(t,channel11,color='g')
# plt.plot(t,channel12,color='g')
# plt.plot(t,channel13,color='g')
# plt.plot(t,channel14,color='g')
# plt.plot(t,channel15,color='g')

# plt.plot(t,t_c1,color='g',linestyle='--')
# plt.plot(t,t_c2,color='g',linestyle='--')
# plt.plot(t,t_c3,color='g',linestyle='--')
# plt.plot(t,t_c4,color='g',linestyle='--')
# plt.plot(t,t_c5,color='g',linestyle='--')

plt.grid()
plt.show()


# channel1=list(map(int,ch1))
# channel2=list(map(int,ch2))
# channel3=list(map(int,ch3))
# difference1=channel1[1]-channel1[0]
# difference2=channel2[1]-channel2[0]
# difference3=channel3[1]-channel3[0]
#
# for i in range(0, amount-1):
#     if(channel1[i+1]-channel1[i]>difference1):
#         difference1=channel1[i + 1] - channel1[i]
#     if (channel2[i + 1] - channel2[i] > difference2):
#         difference2 = channel2[i + 1] - channel2[i]
#     if(channel3[i+1]-channel3[i]>difference3):
#         difference3=channel3[i + 1] - channel3[i]
#
# print("辅助：difference1:",difference1)
# print("低：difference2:",difference2)
# print("高：difference3:",difference3)

# print("流速：max(c4)-min(c4):",max(channel4)-min(channel4))
# sum=0
#
# y1 = [0] * amount
# y2 = [0] * amount
# y3 = [0] * amount
# j = k = l = 0
# y1[0] = channel1[0]
# for i in range(0, amount-1):
#     if (channel1[i + 1] - y1[i]) > 2:
#         y1[i+1] = y1[i] + 2
#     elif (channel1[i + 1] - y1[i])< -2:
#         y1[i+1] = y1[i] - 2
#     else:
#         y1[i + 1] = channel1[i + 1]
# # sum=y1[0]
# for i in range(0, int(amount/10)):
#     for j in range(0, 10):
#         sum=sum+y1[i*10+j]
#     y2[i]=int(sum/10)
#     sum=0
#
# for i in range(0, int(amount/10)):
#     for j in range(0, 10):
#         y3[i*10+j]= y2[i]
# for i in range(0, amount):
#     if(y3[i]==0):
#         y3[i]=y3[i-1]
#
#
#
# y3[amount-1]=y3[amount-2]
# y2[i]=(y1[i+1]+y1[i])/2
    # k=k+1
    # if(k<10):
    # y2[]
    # if ((channel1[i + 1] - y1[i] > 1)or(y1[i]-channel1[i + 1]>1)):
    #     j = j + 1
    #     y1[i+1] = y1[i]
    # else:
    #     j = 0
    #     y1[i+1] = channel1[i+1]
    # if (j > 10):
    #     y1[i+1] = y1[i]+4
    #     j = 0
# y1[amount-1] = channel1[amount-1]
# y2[amount-1]=y2[amount-2]
# print("原始：max(c1)-min(c1):",max(channel1)-min(channel1))
# print("滤波后：max(y1)-min(y1):",max(y1)-min(y1))
# print("滤波后1：max(y1)-min(y1):",max(y3)-min(y3))
# plt.plot(t,channel1,color='k')
# plt.plot(t,y1,color='r')
# plt.plot(t,y3,color='b')






# temperature=[1,2,3,4]
# t_ch2=[1434,1437,1439,1440]
# t_ch3=[1223,1227,1230,1229]
# t_ch7=[1187,1194,1197,1197]
# def nh(temperature,t_ch2,t_ch3,t_ch7):
#     f2 = np.polyfit(temperature, t_ch2, 1)
#     f3 = np.polyfit(temperature, t_ch3, 1)
#     f7 = np.polyfit(temperature, t_ch7, 1)
#     p2 = np.poly1d(f2)
#     p3 = np.poly1d(f3)
#     p7 = np.poly1d(f7)
#     print('p2 is :\n', p2)
#     print('p3 is :\n', p3)
#     print('p7 is :\n', p7)
#     yvals2 = p2(temperature)  # 拟合y值
#     yvals3 = p3(temperature)  # 拟合y值
#     yvals7 = p7(temperature)  # 拟合y值
#
#     plt.scatter(temperature, t_ch2,color='r')
#     plt.plot(temperature, yvals2, 'black')
#
#     plt.scatter(temperature, t_ch3, color='g')
#     plt.plot(temperature, yvals3, 'black')
#
#     plt.scatter(temperature, t_ch7,color='b')
#     plt.plot(temperature, yvals7, 'black')
#
# nh(temperature,t_ch2,t_ch3,t_ch7)
#
# # print((t_ch3[0]-t_ch3[6])/(t_ch2[0]-t_ch2[6]))
# # print((t_ch7[0]-t_ch7[6])/(t_ch2[0]-t_ch2[6]))
#
# # #
# # temperature.extend(temperature_1)
# # t_ch2.extend(t_ch2_1)
# # t_ch3.extend(t_ch3_1)
# # t_ch7.extend(t_ch7_1)
# # temperature.extend(temperature_2)
# # t_ch2.extend(t_ch2_2)
# # t_ch3.extend(t_ch3_2)
# # t_ch7.extend(t_ch7_2)
# #
# # temperature.extend(temperature_3)
# # t_ch2.extend(t_ch2_3)
# # t_ch3.extend(t_ch3_3)
# # t_ch7.extend(t_ch7_3)
# #
# # temperature.extend(temperature_4)
# # t_ch2.extend(t_ch2_4)
# # t_ch3.extend(t_ch3_4)
# # t_ch7.extend(t_ch7_4)
# #

## # nh(temperature_1,t_ch2_1,t_ch3_1,t_ch7_1)
# # print((t_ch3_1[4]-t_ch3_1[0])/(t_ch2_1[4]-t_ch2_1[0]))
# # print((t_ch7_1[4]-t_ch7_1[0])/(t_ch2_1[4]-t_ch2_1[0]))
# #

# # # nh(temperature_3,t_ch2_3,t_ch3_3,t_ch7_3)
# # nh(temperature_4,t_ch2_4,t_ch3_4,t_ch7_4)
# # nh(x,ch_7,ch_8,ch_9)
# #

#
# c1=list(np.array(channel1).flatten())
# c2=list(np.array(channel2).flatten())
# c3=list(np.array(channel3).flatten())
#
# # f2 = np.polyfit(t, c2, 1)
# # f3 = np.polyfit(t, c3, 1)
# # f7 = np.polyfit(t, c7, 1)
# # print('f7 is :\n',f7)
# # p2 = np.poly1d(f2)
# # p3 = np.poly1d(f3)
# # p7 = np.poly1d(f7)
# # print('p2 is :\n',p2)
# # print('p3 is :\n',p3)
# # print('p7 is :\n',p7)
# # yvals2 = p2(t)  #拟合y值
# # yvals3 = p3(t)  #拟合y值
# # yvals7 = p7(t)  #拟合y值
# # plt.plot(t, yvals2, 'y')
# # plt.plot(t, yvals3, 'y')
# # plt.plot(t, yvals7, 'y')
#
#
#
# #
# # temperature_1=[82,77.5,72.5,67.5,62.5,57.5,52.5,47.5,42.5,37.5,34.25]#温度
# # t_ch2_1=[48468.87,47259.17,46025.01,44519.68,43953.07,41964.77,40920.76,39688.79,38703.26,37572.96,37043.81]
# # t_ch3_1=[55237.14,54527.74,53873.52,53019.14,52436.90,51653.87,51102.95,50347.26,49081.97,49102.90,48808.47]
# # t_ch7_1=[57180.57,56556.84,55866.14,54972.95,54332.19,53453.23,52867.11,52085.59,51478.58,50689.78,50325.05]
# #
# # temperature_2=[87.5,82.5,77.5,72.5,67.5,62.5,57.5,52.5,47.5,42.5]#温度
# # t_ch2_2=[50198.22,48780.12,47297.13,46028.43,44720.34,43363.68,42158.50,40926.92,39947.34,38737.58]
# # t_ch3_2=[57550.83,56869.32,56130.89,55486.56,54757.71,53933.67,53244.29,52545.22,51997.95,51255.68]
# # t_ch7_2=[58269.73,57650.32,56860.92,56119.50,55371.54,54564.45,53817.02,53076.83,53477.90,51624.51]
# #
# # temperature_3=[86.7,80.5,75.5,69.5,62,60,55,50,46.9]
# # t_ch2_3=[50011.91,48481.27,46976.61,45269.90,44006.98,42943.86,41462.49,40437.26,39768.48]
# # t_ch3_3=[57253.69,56560.77,55823.72,54822.70,54093.85,53464.63,52524.37,51918.67,51384.42]
# # t_ch7_3=[58293.38,57620.58,56793.47,55788.03,55076.80,54431.97,53448.87,52822.13,52371.71]
# #
# # temperature_4=[87.5,82.5,77.5,72.5,67,62,57.5,52.5,47.5]
# # t_ch2_4=[53331.70,52040.13,50587.60,49207.69,47757.82,46488.43,45122.60,43913.26,42623.62]
# # t_ch3_4=[53148.49,52820.52,52166.50,51463.35,50667.98,50094.97,49446.04,49009.05,48451.98]
# # t_ch7_4=[54479.32,54321.99,53759.29,53138.25,52366.81,51681.24,50845.16,50093.89,49266.69]
# #
# # c7=[]*12
# # c8=[]*12
# # c9=[]*12
# # a=600
# # print(a)
# # for i in range(0,10):
# #     c7[i]=c7_1[a+i*2]
# #
# #
# temperature_1=[0,5,10,15,20,25,30,35,40,45,50,55]
# t_ch2_1=[2769,2770,2772,2782,2813,2835,2860,2885,2893,2904,2872,2900]
# t_ch3_1=[3091,3091,3100,3120,3180,3225,3271,3314,3342,3312,3286,3315]
# t_ch7_1=[3610,3614,3618,3635,3678,3728,3760,3785,3780,3760,3770,3780]
#
# # print((t_ch3_1[5]-t_ch3_1[0])/(t_ch2_1[5]-t_ch2_1[0]))
# # print((t_ch7_1[5]-t_ch7_1[0])/(t_ch2_1[5]-t_ch2_1[0]))
# #
# # print((t_ch3_1[6]-t_ch3_1[0])/(t_ch2_1[6]-t_ch2_1[0]))
# # print((t_ch7_1[6]-t_ch7_1[0])/(t_ch2_1[6]-t_ch2_1[0]))
# #
# # print((t_ch3_1[7]-t_ch3_1[0])/(t_ch2_1[7]-t_ch2_1[0]))
# # print((t_ch7_1[7]-t_ch7_1[0])/(t_ch2_1[7]-t_ch2_1[0]))
# #
# # print((t_ch3_1[11]-t_ch3_1[0])/(t_ch2_1[11]-t_ch2_1[0]))
# # print((t_ch7_1[11]-t_ch7_1[0])/(t_ch2_1[11]-t_ch2_1[0]))
# h=[0]*11
# l=[0]*11
# sl=0
# sh=0
# for i in range(1,11):
#     h[i]=((t_ch7_1[i]-t_ch7_1[0])/(t_ch2_1[i]-t_ch2_1[0]))
#     l[i]=((t_ch3_1[i]-t_ch3_1[0])/(t_ch2_1[i]-t_ch2_1[0]))
#
# for i in range(0,10):
#     if(h[i]==0.0):
#         del h[i]
#     if(l[i]==0.0):
#         del l[i]
# # print(len(h))
# # print(len(l))
# # print(h)
# # print(l)
# for i in range(1, 10):
#     if(h[i]!=min(h) and h[i]!=max(h)):
#         sh=sh+h[i]
#     if(l[i]!=min(l) and l[i]!=max(l)):
#         sl=sl+l[i]
#
# # print(sh/8)
# # print(sl/8)
#
#
#
#
# # temperature=[50,40,30,20,5,0]
# # t_ch2=[2903,2826,2800,2793,2782,2779]
# # t_ch3=[3316,3156,3130,3121,3111,3107]
# # t_ch7=[3789,3660,3650,3647,3637,3636]
#

# #
#
# #数据写入excel
# # data3 = pd.DataFrame(channel3)
# # data2 = pd.DataFrame(channel2)
# # data7 = pd.DataFrame(channel7)
# # writer = pd.ExcelWriter('90_30.xlsx')		# 写入Excel文件
# # data3.to_excel(writer, 'page_3', float_format='%.5f')		# ‘page_1’是写入excel的sheet名
# # data2.to_excel(writer, 'page_2', float_format='%.5f')		# ‘page_1’是写入excel的sheet名
# # # data7.to_excel(writer, 'page_7', float_format='%.5f')		# ‘page_1’是写入excel的sheet名
# # writer.save()
# # writer.close()
#
#
#
# xa=[0]*30
# x=[0]*600
# for i in range(0,30):
#     xa[i]=random.randint(10,600)
# print(xa)
#
# ka2=[0]*600
# kl2=[0]*600
# kh2=[0]*600
#
# for i in range(0,amount-2):
#     kl2[i]=(c2[i]-c2[amount-1])/(c1[i]-c1[amount-1])
#     kh2[i]=(c3[i]-c3[amount-1])/(c1[i]-c1[amount-1])
#     x[i]=i
#
# print(kl2)
# print(kh2)
#
# plt.plot(x,kl2,color='g')
# plt.plot(x,kh2,color='b')

# def Least_squares(x,y):
#     N = len(x)
#     sumx = sum(x)
#     sumy = sum(y)
#     sumx2 = sum(x ** 2)
#     sumxy = sum(x * y)
#
#     A = np.mat([[N, sumx], [sumx, sumx2]])
#     b = np.array([sumy, sumxy])
#
#     return np.linalg.solve(A, b)
#
#
# def f_1(x, A, B):
#     return A * x + B


#降温1次
# temperature_ch1=[47,42,37,35,33,29,27.7]
# t_ch1=[1701,1705,1711,1712,1715,1715,1715]
#
# temperature_ch2=[46,41,36,24.1,32,28.3,27.1]
# t_ch2=[1609,1616,1627,1629,1636,1631,1633]
#
# temperature_ch3=[45,40,35,33,31.5,27.7,26.6]
# t_ch3=[1634,1650,1655,1659,1662,1654,1651]
#

#降温2次
# temperature_ch1=[60.0,59.0,54.3,48.0,41.5,35.9,32,29.1,28.2]
# t_ch1=[1705,1706,1710,1713,1716,1720,1719,1719,1719]
#
# temperature_ch2=[58.3,57.2,52.4,46.6,40.3,35.1,31.5,28.5,27.6]
# t_ch2=[1614,1614,1620,1625,1632,1638,1640,1641,1641]
#
# temperature_ch3=[55.9,54.8,50.3,45,39.1,34.2,30.5,28,27.2]
# t_ch3=[1681,1680,1685,1688,1690,1693,1691,1690,1691]
#

# #升温2次
# temperature_ch1=[34.2,37.3,42.6,47.3,50.5,53.5,56.6,58.2,58.9,59.8,60.3]
# t_ch1=[1713,1712,1706,1707,1707,1705,1706,1704,1705,1704,1706]
#
# temperature_ch2=[33.1,36.7,41.6,46.3,49.3,52.3,55.3,56.8,57.6,58.5,58.8]
# t_ch2=[1628,1627,1620,1619,1618,1614,1613,1610,1612,1610,1611]
#
# temperature_ch3=[33,36.9,41.6,46.2,48.7,51.6,54.5,55.5,56.1,56.0,56.3]
# t_ch3=[1684,1683,1680,1681,1682,1682,1678,1678,1679,1677,1681]

# 直线拟合与绘制
# A1, B1 = optimize.curve_fit(f_1, temperature_ch1, t_ch1)[0]
# x1 = np.arange(temperature_ch1[0],temperature_ch1[len(temperature_ch1)-1],0.01)
# y1 = A1 * x1 + B1
# print("y1=%f*X1+%f"%(A1,B1))
#
# # 直线拟合与绘制
# A2, B2 = optimize.curve_fit(f_1, temperature_ch2, t_ch1)[0]
# x2 = np.arange(temperature_ch2[0],temperature_ch2[len(temperature_ch2)-1],0.01)
# y2 = A2 * x2 + B2
# print("y2=%f*X2+%f"%(A2,B2))
#
#
# # 直线拟合与绘制
# A3, B3 = optimize.curve_fit(f_1, temperature_ch3, t_ch3)[0]
# x3 = np.arange(temperature_ch3[0],temperature_ch3[len(temperature_ch3)-1],0.01)
# y3 = A3 * x3 + B3
# print("y3=%f*X3+%f"%(A3,B3))
#
# print(A2/A1)
# print(A3/A1)
#
# plt.plot(temperature_ch1,t_ch1,'rp',label="point")
# plt.plot(temperature_ch2,t_ch2,'gp',label="point")
# plt.plot(temperature_ch3,t_ch3,'bp',label="point")
#
# plt.plot(x1, y1,color="r")
# plt.plot(x2, y2,color= "g")
# plt.plot(x3, y3,color= "b")
# plt.show()
#
#
#

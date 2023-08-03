/*
 * Time_Date.c
 *
 *  Created on: 2022年9月21日
 *      Author: WX
 */

#include <iostream>
#include <ctime>
#include <string>
#include "Time_Date.h"

using namespace std;

void Get_Time_Date(void)
{
	time_t	Time_Gather=0;
	struct tm*	tm_data=0;
	string str;
	string str_asc;
	clog<<"Get_Time_Date:"<<endl;
	time(&Time_Gather);
	str=ctime(&Time_Gather);
	clog<<"本地时间和日期->:"<<str;//ctime()函数返回的字符串自带换行符'/n'
	tm_data=gmtime(&Time_Gather);
	str_asc=asctime(tm_data);
	clog<<"UTC时间和日期->:"<<str_asc;

	clog<<"tm_data->tm_hour="<<(tm_data->tm_hour)<<endl;
	clog<<endl;
}



#include "TimeDate.h"
#include <iostream>
#include <ctime>

using namespace std;

void Get_Time(void)
{
	time_t a=time(0);
	char *b=ctime(&a);
	
	cout <<"本地日期和时间:"<<b<<endl;
}

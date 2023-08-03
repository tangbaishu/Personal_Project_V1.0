#include <iostream>
#include <string.h>
#include "Struct_Test.h"

using namespace std;

struct time
{
	int sec=0;//second
	int minute=0;
	int hour=0;
	int month=0;
	int year=0;
};



void Struct_time_clog(time bj)
{
	clog<<"bj.sec="<<bj.sec<<endl;
	clog<<"bj.minute="<<bj.minute<<endl;
	clog<<"bj.hour="<<bj.hour<<endl;
	clog<<"bj.month="<<bj.month<<endl;
	clog<<"bj.year="<<bj.year<<endl;
}


void Struct_Test_Ture(void)
{
	time bj;
	time *sz=&bj;

	bj.sec=59;
	bj.minute=45;
	bj.hour=17;
	bj.month=9;
	bj.year=2022;
	clog<<"Struct_Test_Ture"<<endl;
	Struct_time_clog(bj);
	sz->sec=40;
	sz->minute=25;
	sz->hour=18;
	sz->month=10;
	sz->year=2021;
	Struct_time_clog(bj);


	clog<<endl;
}




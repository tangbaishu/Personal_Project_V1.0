/*
 * Mclass.cpp
 *
 *  Created on: 2022年9月26日
 *      Author: WX
 */
#include <iostream>
#include "Mclass.h"

using namespace std;

class mclass
{
public://公有成员
	void city_clog(mclass city);
	string city_Evaluate;//Evaluate 评价
	static void country(void);
private://私有成员
	string city_name;
protected://保护成员
	string Author;
};

class test_class//未声明继承方式（基类）/成员类型，默认为私有继承/私有成员
{
	string test;
public:
	void clog_test_class();
};

void test_class::clog_test_class()
{
	test_class str;
	str.test="默认私有";
	clog<<"test="<<str.test<<endl;
}

void mclass::city_clog(mclass city)
{
	city.city_name="Shen Zhen";
	city.Author="TLB";
	clog<<"city_name="<<city.city_name<<endl;
	clog<<"city_Evaluate="<<city.city_Evaluate<<endl;
	clog<<"Author="<<city.Author<<endl;
}

void mclass::country(void)
{
	clog<<"zhong guo"<<endl;
}

void Mclass_Functon(void)
{
	mclass shenzhen;
	test_class test;
	clog<<"Mclass_Functon:"<<endl;
	shenzhen.city_Evaluate="Very Good";
	shenzhen.city_clog(shenzhen);
//	test.test_class;//无效使用
	test.clog_test_class();
	shenzhen.country();
	clog<<endl;
}






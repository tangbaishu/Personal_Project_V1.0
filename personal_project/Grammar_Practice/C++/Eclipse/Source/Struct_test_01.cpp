/*
 * Struct_test_01.cpp
 *
 *  Created on: 2022年10月13日
 *      Author: WX
 */

#include "Struct_Test_01.h"
#include <iostream>

using namespace std;

//若未定义构造函数时，系统会自动定义构造函数，但此时构造函数未空，没有参数和函数体，不执行任何操作
typedef struct book
{
	string  book_name;
	int	 	number;
	int		test;
//	//构造函数的变量赋值顺序与结构体成员变量定义顺序有关，与赋值顺序无关
//	//例如
//	book(string a,int b):book_name(a),test(b),number(test)
//	{
//		clog<<"test="<<test<<endl;
//		clog<<"number="<<number<<endl;
//		//若按照构造函数变量赋值顺序执行，则number=test，但实际是按照结构体变量定义顺序执行。因此number=未知数（test未初始化，值未知），test=b
//		clog<<"book_name="<<book_name<<endl;
//
//	}
	book(string a,int b,int c):book_name(a),number(b),test(c)
	{
		clog<<"book_name="<<book_name<<endl;
		clog<<"number="<<number<<endl;
		clog<<"test="<<test<<endl;
	}
}books;

void books_clog(books books_clog)
{
	clog<<"book_name="<<books_clog.book_name<<endl;
	clog<<"number="<<books_clog.number<<endl;
}

void Struct_Test_01_Dispose(void)
{
	books book0("英语",15,6);

	book0.book_name="C++语法";
	book0.number=1;
	books_clog(book0);
}

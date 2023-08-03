#include <iostream>
#include "quote.h"

using namespace std;

//函数名称：引用的实际应用 
int& Quote_RealEffect(int& d,int& e)
{
	int f=0;
	int	&h=d; 
	f=d;
	d=e;
	e=f;
/*	return f;//无语法错误，但存在逻辑错误或与预期不符.
				原因如下:引用变量实质可以理解为其所引用的变量名称的另一个别名.
				因此,在该例中,因f是局部变量,当函数结束后地址会被清除或被占用.
				导致数据失真 */
	return h;//与return d 等效;返回引用变量时,实际是返回一个指向返回值的隐式指针 
}

void Quote_Test(void)
{
	int a=5; 
	int& b=a;//创建一个引用变量b，b引用a
	int	c=15,g=0;
//	int& d=0;语法错误，引用变量初始化时必须指定要引用的变量名称  
	cout<<"C++引用语法测试开始:"	<<endl;  
	
	cout<<"a="<<a<<endl;
	b=10;//通过给引用变量b赋值，从而修改实际变量a的值。 
	cout<<"a="<<a<<endl;
	b=c;//该部分仅将变量C的值赋给b，并未改变引用变量b所引用的变量 
	cout<<"b="<<b<<endl;
	cout<<"a="<<a<<endl;
	
	cout<<"引用的实际应用："<<endl; 
	
	a=5,c=10;
	g=Quote_RealEffect(a,c);
	cout<<"a="<<a<<endl;
	cout<<"c="<<c<<endl;
	cout<<"g="<<g<<endl;
	
	cout<<"C++引用语法测试结束！"<<endl;
}

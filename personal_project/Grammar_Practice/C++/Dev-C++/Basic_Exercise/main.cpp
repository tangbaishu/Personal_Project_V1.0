#include <iostream>
#include "string.h"
#include <stdio.h>

using namespace std;

class Test_Class
{
	//访问修饰符： 
	public:	//公有的
		//对应的成员变量 
		int public_data;
		//类方法（）；
		int Test_Class_Way(int data);//测试类方法（）；
	private: //私有的
		int	private_data;
	protected: //受保护的
		int	protected_data;
	 	
};

int Test_Class :: Test_Class_Way(int data)
{
	cout << "Test_Class_Way() import data ->" << data <<endl;
	return data;
}

/*
 * 函数名称： void Test_Quote(int& x,int y)
 * 作用：测试C++ 引用功能
 */
void Test_Quote(int& x,int y)
{
    x = 200;
    y = 100;
    cout << "Test_Quote()->x=" << x << ";y=" << y <<endl;
}

void Printf_Out(void)
{
	Test_Class	entity_0;//声明一个类类型的变量 
    cout <<"hello Qt!" << endl;//endl 相当于换行输出，可以用"\n"代替。实例： cout <<"hello Qt!" << "\n";
    cout <<"int = " << sizeof(int) << endl;//sizeof()
    char test_data[]={"test"};
    cout <<"test_data数组长度 = " << sizeof(test_data) << endl;//sizeof() 单目运算符 计算数据类型所占空间的大小，单位为字节（因此包含空字符）
    cout <<"test_data数组长度 = " << strlen(test_data) << endl;//strlen()实际是一个函数，需要包含string.h头文件，用于计算字符串长度
    int quote_x = 100;
    int data_y=50;
    cout << "Test_Quote_after_before    quote_x=" << quote_x << ";data_y=" << data_y <<endl;
    Test_Quote(quote_x,data_y);
    cout << "Test_Quote_after_later     quote_x=" << quote_x << ";data_y=" << data_y <<endl;
	clog << "C++ 类&对象 实列" <<endl; 
    entity_0.public_data=100;
    entity_0.Test_Class_Way(entity_0.public_data);
}

void cin_input(void)
{
	char one_char=0;
	cout << "输入一个字符" << endl;
	cin >> one_char;
	cout << "输入字符为：" << one_char <<endl; 
}


int main(void)
{
	Printf_Out();
	cin_input();
	return 0;
}

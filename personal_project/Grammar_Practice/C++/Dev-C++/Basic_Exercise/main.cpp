#include <iostream>
#include "string.h"
#include <stdio.h>

using namespace std;

class Test_Class
{
	//�������η��� 
	public:	//���е�
		//��Ӧ�ĳ�Ա���� 
		int public_data;
		//�෽��������
		int Test_Class_Way(int data);//�����෽��������
	private: //˽�е�
		int	private_data;
	protected: //�ܱ�����
		int	protected_data;
	 	
};

int Test_Class :: Test_Class_Way(int data)
{
	cout << "Test_Class_Way() import data ->" << data <<endl;
	return data;
}

/*
 * �������ƣ� void Test_Quote(int& x,int y)
 * ���ã�����C++ ���ù���
 */
void Test_Quote(int& x,int y)
{
    x = 200;
    y = 100;
    cout << "Test_Quote()->x=" << x << ";y=" << y <<endl;
}

void Printf_Out(void)
{
	Test_Class	entity_0;//����һ�������͵ı��� 
    cout <<"hello Qt!" << endl;//endl �൱�ڻ��������������"\n"���档ʵ���� cout <<"hello Qt!" << "\n";
    cout <<"int = " << sizeof(int) << endl;//sizeof()
    char test_data[]={"test"};
    cout <<"test_data���鳤�� = " << sizeof(test_data) << endl;//sizeof() ��Ŀ����� ��������������ռ�ռ�Ĵ�С����λΪ�ֽڣ���˰������ַ���
    cout <<"test_data���鳤�� = " << strlen(test_data) << endl;//strlen()ʵ����һ����������Ҫ����string.hͷ�ļ������ڼ����ַ�������
    int quote_x = 100;
    int data_y=50;
    cout << "Test_Quote_after_before    quote_x=" << quote_x << ";data_y=" << data_y <<endl;
    Test_Quote(quote_x,data_y);
    cout << "Test_Quote_after_later     quote_x=" << quote_x << ";data_y=" << data_y <<endl;
	clog << "C++ ��&���� ʵ��" <<endl; 
    entity_0.public_data=100;
    entity_0.Test_Class_Way(entity_0.public_data);
}

void cin_input(void)
{
	char one_char=0;
	cout << "����һ���ַ�" << endl;
	cin >> one_char;
	cout << "�����ַ�Ϊ��" << one_char <<endl; 
}


int main(void)
{
	Printf_Out();
	cin_input();
	return 0;
}

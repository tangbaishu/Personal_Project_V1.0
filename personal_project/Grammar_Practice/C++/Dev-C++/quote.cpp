#include <iostream>
#include "quote.h"

using namespace std;

//�������ƣ����õ�ʵ��Ӧ�� 
int& Quote_RealEffect(int& d,int& e)
{
	int f=0;
	int	&h=d; 
	f=d;
	d=e;
	e=f;
/*	return f;//���﷨���󣬵������߼��������Ԥ�ڲ���.
				ԭ������:���ñ���ʵ�ʿ������Ϊ�������õı������Ƶ���һ������.
				���,�ڸ�����,��f�Ǿֲ�����,�������������ַ�ᱻ�����ռ��.
				��������ʧ�� */
	return h;//��return d ��Ч;�������ñ���ʱ,ʵ���Ƿ���һ��ָ�򷵻�ֵ����ʽָ�� 
}

void Quote_Test(void)
{
	int a=5; 
	int& b=a;//����һ�����ñ���b��b����a
	int	c=15,g=0;
//	int& d=0;�﷨�������ñ�����ʼ��ʱ����ָ��Ҫ���õı�������  
	cout<<"C++�����﷨���Կ�ʼ:"	<<endl;  
	
	cout<<"a="<<a<<endl;
	b=10;//ͨ�������ñ���b��ֵ���Ӷ��޸�ʵ�ʱ���a��ֵ�� 
	cout<<"a="<<a<<endl;
	b=c;//�ò��ֽ�������C��ֵ����b����δ�ı����ñ���b�����õı��� 
	cout<<"b="<<b<<endl;
	cout<<"a="<<a<<endl;
	
	cout<<"���õ�ʵ��Ӧ�ã�"<<endl; 
	
	a=5,c=10;
	g=Quote_RealEffect(a,c);
	cout<<"a="<<a<<endl;
	cout<<"c="<<c<<endl;
	cout<<"g="<<g<<endl;
	
	cout<<"C++�����﷨���Խ�����"<<endl;
}

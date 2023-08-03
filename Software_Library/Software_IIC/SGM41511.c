#include "SYS_Init.h"

void Register_Write(uchar register_Adr, uchar writer_data)
{
	IIc_Start();
	IIc_Send_Byte(SLAVE_ADR_WRITE);//���� ������ַ д
	if(IIc_Wait_Ack())
	{
		return;
	}
	IIc_Send_Byte(register_Adr); 		//�Ĵ�����ַ
	if(IIc_Wait_Ack())
	{
		return;
	}
	IIc_Send_Byte(writer_data);			//�Ĵ�������
	if(IIc_Wait_Ack())
	{
		return;
	}
	IIc_Stop();
	Delay_X100us(100);//��ʱ10ms
	printf("register_Adr->%d,writer_data->%d\r\n",(uint)register_Adr,(uint)writer_data);
}

uchar Register_Read(uchar register_Adr)
{
	uchar read_data;
	IIc_Start();
	IIc_Send_Byte(SLAVE_ADR_WRITE);//���� ������ַ д
	if(IIc_Wait_Ack())
	{
		return 0;
	}
	IIc_Send_Byte(register_Adr); 		//�Ĵ�����ַ
	if(IIc_Wait_Ack())
	{
		return 0;
	}
	IIc_Start();
	IIc_Send_Byte(SLAVE_ADR_READ);		//���� ������ַ ��
	if(IIc_Wait_Ack())
	{
		return 0;
	}
	read_data = IIc_Read_Byte(0);			//��ȡ ������ַ��Ӧ�ļĴ�����ַ����
	IIc_Stop();
	Delay_X100us(100);//��ʱ10ms
	printf("register_Adr->%d,read_data->%d\r\n",(uint)register_Adr,(uint)read_data);
	return read_data;
}

uchar Continue_Adr_Read(uchar start_Adr, uchar read_num)
{
	uchar Read_Adr_Data=0;//ʵ��Ӧ��ʱ�����黺��
	IIc_Start();
	IIc_Send_Byte(SLAVE_ADR_WRITE);//��������/�ӻ���ַ д
	if(IIc_Wait_Ack())
	{
		return 0;
	}
	IIc_Send_Byte(start_Adr);//���Ͷ�Ӧ����/�ӻ��ڵļĴ�����ַ
	if(IIc_Wait_Ack())
	{
		return 0;
	}
	
	IIc_Start();
	IIc_Send_Byte(SLAVE_ADR_READ);//��������/�ӻ���ַ ��
	if(IIc_Wait_Ack())
	{
		return 0;
	}
	
	while(1)
	{
		if(read_num!=0)
		{
			Read_Adr_Data = IIc_Read_Byte(1);//����SGM41511�߼���������ȡӦ��ʱ����ȡ״̬����
		}
		else
		{
			Read_Adr_Data = IIc_Read_Byte(0);//���һ�β�Ӧ���˳�
		}
		printf("Read_Adr->%d,Adr_Data->%d\r\n",(uint)start_Adr,(uint)Read_Adr_Data);
		start_Adr++;
		if(read_num==0)
		{
			break;
		}
		read_num--;
	}
	IIc_Stop();
	return 1;
}

void	Input_Electricity(void)
{
	if(Register_Read(0)!=0x01)
	{
		Register_Write(0,0x01);
	}
}
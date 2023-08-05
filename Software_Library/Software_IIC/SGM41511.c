#include "SYS_Init.h"

void Register_Write(uchar register_Adr, uchar writer_data)
{
	IIc_Start();
	IIc_Send_Byte(SLAVE_ADR_WRITE);//发送 器件地址 写
	if(IIc_Wait_Ack())
	{
		return;
	}
	IIc_Send_Byte(register_Adr); 		//寄存器地址
	if(IIc_Wait_Ack())
	{
		return;
	}
	IIc_Send_Byte(writer_data);			//寄存器数据
	if(IIc_Wait_Ack())
	{
		return;
	}
	IIc_Stop();
	Delay_X100us(100);//延时10ms
	printf("register_Adr->%d,writer_data->%d\r\n",(uint)register_Adr,(uint)writer_data);
}

uchar Register_Read(uchar register_Adr)
{
	uchar read_data;
	IIc_Start();
	IIc_Send_Byte(SLAVE_ADR_WRITE);//发送 器件地址 写
	if(IIc_Wait_Ack())
	{
		return 0;
	}
	IIc_Send_Byte(register_Adr); 		//寄存器地址
	if(IIc_Wait_Ack())
	{
		return 0;
	}
	IIc_Start();
	IIc_Send_Byte(SLAVE_ADR_READ);		//发送 器件地址 读
	if(IIc_Wait_Ack())
	{
		return 0;
	}
	read_data = IIc_Read_Byte(0);			//读取 器件地址对应的寄存器地址数据
	IIc_Stop();
	Delay_X100us(100);//延时10ms
	printf("register_Adr->%d,read_data->%d\r\n",(uint)register_Adr,(uint)read_data);
	return read_data;
}

uchar Continue_Adr_Read(uchar start_Adr, uchar read_num)
{
	uchar Read_Adr_Data=0;//实际应用时用数组缓存
	IIc_Start();
	IIc_Send_Byte(SLAVE_ADR_WRITE);//发送器件/从机地址 写
	if(IIc_Wait_Ack())
	{
		return 0;
	}
	IIc_Send_Byte(start_Adr);//发送对应器件/从机内的寄存器地址
	if(IIc_Wait_Ack())
	{
		return 0;
	}
	
	IIc_Start();
	IIc_Send_Byte(SLAVE_ADR_READ);//发送器件/从机地址 读
	if(IIc_Wait_Ack())
	{
		return 0;
	}
	
	while(1)
	{
		if(read_num!=0)
		{
			Read_Adr_Data = IIc_Read_Byte(1);//基于SGM41511逻辑，主机读取应答时，读取状态延续
		}
		else
		{
			Read_Adr_Data = IIc_Read_Byte(0);//最后一次不应答退出
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
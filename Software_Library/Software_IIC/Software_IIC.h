#ifndef __IIC_H__
#define __IIC_H__

#include <REGtenxTM52F1376.h>
#include <intrins.h>

#define SDA_PP_Out_En	1

#define SDA_IO		P3_1
#define SCL_IO		P3_0

//IO操作函数	 
#define IIC_SCL_H()    	SCL_IO=1
#define IIC_SCL_L()    	SCL_IO=0	
#define IIC_SDA_H()    	SDA_IO=1	 
#define IIC_SDA_L()   	SDA_IO=0		 
#define READ_SDA()     	SDA_IO     //输入SDA 


#if SDA_PP_Out_En
	#define SDA_IN()				SET_REG(PORTIDX, 3);SET_REG_BITS(PINMOD10, PINMOD1, PIN_H_MODE_OD);P3_1=1
	#define SDA_OUT() 			SET_REG(PORTIDX, 3);SET_REG_BITS(PINMOD10, PINMOD1, PIN_H_MODE_PP);P3_1=1
#else
	#define SDA_IN()			SDA_IO=1
	#define SDA_OUT()
#endif


//IIC所有操作函数			
void IIc_init(void);				                    //IIC引脚初始化
void IIc_Start(void);				                    //发送IIC开始信号
void IIc_Stop(void);	  			                  //发送IIC停止信号
void IIc_Wait(void);
void IIc_Send_Byte(unsigned char txd);			    //IIC发送一个字节
unsigned char IIc_Read_Byte(unsigned char ack); //IIC读取一个字节
unsigned char IIc_Wait_Ack(void); 				      //IIC等待ACK信号
void IIc_Ack(void);					                    //IIC发送ACK信号
void IIc_NAck(void);				                    //IIC不发送ACK信号

#endif

#ifndef __IIC_H__
#define __IIC_H__

#include <REGtenxTM52F1376.h>
#include <intrins.h>

#define SDA_PP_Out_En	1

#define SDA_IO		P3_1
#define SCL_IO		P3_0

//IO��������	 
#define IIC_SCL_H()    	SCL_IO=1
#define IIC_SCL_L()    	SCL_IO=0	
#define IIC_SDA_H()    	SDA_IO=1	 
#define IIC_SDA_L()   	SDA_IO=0		 
#define READ_SDA()     	SDA_IO     //����SDA 


#if SDA_PP_Out_En
	#define SDA_IN()				SET_REG(PORTIDX, 3);SET_REG_BITS(PINMOD10, PINMOD1, PIN_H_MODE_OD);P3_1=1
	#define SDA_OUT() 			SET_REG(PORTIDX, 3);SET_REG_BITS(PINMOD10, PINMOD1, PIN_H_MODE_PP);P3_1=1
#else
	#define SDA_IN()			SDA_IO=1
	#define SDA_OUT()
#endif


//IIC���в�������			
void IIc_init(void);				                    //IIC���ų�ʼ��
void IIc_Start(void);				                    //����IIC��ʼ�ź�
void IIc_Stop(void);	  			                  //����IICֹͣ�ź�
void IIc_Wait(void);
void IIc_Send_Byte(unsigned char txd);			    //IIC����һ���ֽ�
unsigned char IIc_Read_Byte(unsigned char ack); //IIC��ȡһ���ֽ�
unsigned char IIc_Wait_Ack(void); 				      //IIC�ȴ�ACK�ź�
void IIc_Ack(void);					                    //IIC����ACK�ź�
void IIc_NAck(void);				                    //IIC������ACK�ź�

#endif

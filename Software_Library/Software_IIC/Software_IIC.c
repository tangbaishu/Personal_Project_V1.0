#include "TM52F1376_sfr_config.h"
#include <REGtenxTM52F1376.h>
#include "SYS_Init.h"
#include "IIC.h"

#define  TIM_CNT  30     //该宏控制IIC速率

/*******************************************************************************
** 函数名称: Delay_us
** 函数描述: 毫秒延时函数
** 输入参数: 延时的毫秒时间
** 输出参数: 无 
** 说    明：不是很精确的延时，基于FRC/2的系统时钟
********************************************************************************/
void Delay_us(unsigned int us)
{
  unsigned int i;
  unsigned char delay_cnt;
  for(i = 0;i<us;i++)
  {	
    delay_cnt++;
  }
}

/******************************************************************************************
** 函数名称: IIc_init
** 函数描述: IIc引脚初始化  
** 输入参数: 无
** 输出参数: 无 
*******************************************************************************************/
void IIc_init(void)
{		
	SET_REG(PORTIDX, 3);                              //选择PORT0端口  
	#if	SDA_PP_Out_En==1	
		SET_REG_BITS(PINMOD10, PINMOD1, PIN_H_MODE_PP);	//P31脚设置为开漏+上拉    SDA引脚 
		SET_REG_BITS(PINMOD10, PINMOD0, PIN_L_MODE_OD);	//P30脚设置为开漏+上拉    SCL引脚 
	#else
		SET_REG_BITS(PINMOD10, PINMOD1, PIN_H_MODE_OD);	//P31脚设置为开漏+上拉    SDA引脚 
		SET_REG_BITS(PINMOD10, PINMOD0, PIN_L_MODE_OD);	//P30脚设置为开漏+上拉    SCL引脚
	#endif
	P3_0=1;        //必须置一，开启输入模式
	P3_1=1;
}

/******************************************************************************************
** 函数名称: IIc_Start
** 函数描述: IIc起始信号
** 输入参数: 无
** 输出参数: 无 
*******************************************************************************************/
void IIc_Start(void)
{
	SDA_OUT();     //SDA线输出，输出高
  IIC_SDA_H();	  	  
  IIC_SCL_H();
  Delay_us(TIM_CNT);
  IIC_SDA_L();//起始信号： 数据线SDA在时钟线为高时，SDA从高电平转变为低电平
  Delay_us(TIM_CNT);
  IIC_SCL_L();//钳住I2C总线，准备发送或接收数据(注：在每个IIC通讯阶段完成后（停止位除外），将时钟线拉低钳住总线) 
	Delay_us(TIM_CNT);
}	  

/******************************************************************************************
** 函数名称: IIc_Stop
** 函数描述: IIc停止信号
** 输入参数: 无
** 输出参数: 无 
*******************************************************************************************/
void IIc_Stop(void)
{
	IIC_SCL_L();
  Delay_us(TIM_CNT/2);
	SDA_OUT();//SDA线输出，输出高
	Delay_us(TIM_CNT/2);
  IIC_SDA_L();//拉低SDA总线，准备发送结束/停止信号
  Delay_us(TIM_CNT/2);
  IIC_SCL_H();//时钟线输出高，准备发送结束/停止信号
	Delay_us(TIM_CNT);	
  IIC_SDA_H();//结束/停止信号：	在时钟线为高期间内，SDA从低电平转变为高电平
  Delay_us(TIM_CNT/2);		
}

 /******************************************************************************************
** 函数名称: IIc_Wait_Ack
** 函数描述: IIc等待应答信号
** 输入参数: 无
** 输出参数: 1：接收应答失败   0：接收应答成功
*******************************************************************************************/
unsigned char IIc_Wait_Ack(void)
{
  unsigned int ucErrTime=0;
	IIC_SCL_L(); 
	Delay_us(TIM_CNT/2);	 
	SDA_IN();      //SDA设置为输入 
	Delay_us(TIM_CNT/2);	
  while(READ_SDA())
  {
		CLRWDT = 1;//喂狗 
    ucErrTime++;
    if(ucErrTime>5000)
    {
      IIc_Stop();
      return 1;
    }
  }
  IIC_SCL_H();//必要项：SCL输出高，锁住从机应答标志（自我理解：告知从机已接收到应答信号，从而时从机释放SDA总线）
  Delay_us(TIM_CNT);
	IIC_SCL_L();//钳住总线
	Delay_us(TIM_CNT);
  return 0;  
} 

/******************************************************************************************
** 函数名称: IIc_Ack
** 函数描述: IIc应答函数
** 输入参数: 无
** 输出参数: 无 
*******************************************************************************************/
void IIc_Ack(void)
{
  IIC_SCL_L();
	Delay_us(TIM_CNT/2);
  SDA_OUT();
  Delay_us(TIM_CNT);
  IIC_SDA_L();
  Delay_us(TIM_CNT);
  IIC_SCL_H();
  Delay_us(TIM_CNT);
  IIC_SCL_L();
  Delay_us(TIM_CNT);
}

/******************************************************************************************
** 函数名称: IIc_NAck
** 函数描述: IIc不应答函数
** 输入参数: 无
** 输出参数: 无 
*******************************************************************************************/
void IIc_NAck(void)
{
  IIC_SCL_L();
	Delay_us(TIM_CNT/2);
  SDA_OUT();
  Delay_us(TIM_CNT/2);
  IIC_SDA_H();
  Delay_us(TIM_CNT);
  IIC_SCL_H();
  Delay_us(TIM_CNT);
  IIC_SCL_L();
  Delay_us(TIM_CNT);
}					 				     
	
/******************************************************************************************
** 函数名称: IIc_Send_Byte
** 函数描述: IIc发送一个字节
** 输入参数: 1：有应答    0：无应答	
** 输出参数: 无 
*******************************************************************************************/
void IIc_Send_Byte(unsigned char txd)
{                        
  unsigned char t;   
	IIC_SCL_L();    
	Delay_us(TIM_CNT/2);
	SDA_OUT(); 	
	Delay_us(TIM_CNT/2);
  for(t=0;t<8;t++)
  { 
		IIC_SCL_L();	
    Delay_us(TIM_CNT/2);
		
    if(txd&0x80)//高位在前
    {
      IIC_SDA_H();
    } 
    else 
    {
      IIC_SDA_L();
    }
    txd<<=1;
 	  
    Delay_us(TIM_CNT/2);   
    IIC_SCL_H();
    Delay_us(TIM_CNT); 
  }
	IIC_SCL_L();
  Delay_us(TIM_CNT/2);
	IIC_SDA_H();//SDA输出高电平，为接收应答做准备
	Delay_us(TIM_CNT/2);
}
 

/******************************************************************************************
** 函数名称: IIc_Read_Byte
** 函数描述: IIc读取一个字节
** 输入参数: 1：发送ACK    0：发送nACK 	
** 输出参数: 无 
*******************************************************************************************/
unsigned char IIc_Read_Byte(unsigned char ack)
{
  unsigned char i,receive=0;
	IIC_SCL_L();
	Delay_us(TIM_CNT/2);
  SDA_IN();//SDA设置为输入
	Delay_us(TIM_CNT/2);
  for(i=0;i<8;i++ )
  {
    IIC_SCL_L(); 
    Delay_us(TIM_CNT);
    IIC_SCL_H();
    receive<<=1;//高位在前
    if(READ_SDA())receive++;   
    Delay_us(TIM_CNT); 
  }		
	IIC_SCL_L();
	Delay_us(TIM_CNT);
  if (!ack)
    IIc_NAck();//发送nACK
  else
    IIc_Ack(); //发送ACK   
  return receive;
}


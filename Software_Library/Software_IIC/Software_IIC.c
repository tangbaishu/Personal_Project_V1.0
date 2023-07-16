#include "TM52F1376_sfr_config.h"
#include <REGtenxTM52F1376.h>
#include "SYS_Init.h"
#include "IIC.h"

#define  TIM_CNT  30     //�ú����IIC����

/*******************************************************************************
** ��������: Delay_us
** ��������: ������ʱ����
** �������: ��ʱ�ĺ���ʱ��
** �������: �� 
** ˵    �������Ǻܾ�ȷ����ʱ������FRC/2��ϵͳʱ��
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
** ��������: IIc_init
** ��������: IIc���ų�ʼ��  
** �������: ��
** �������: �� 
*******************************************************************************************/
void IIc_init(void)
{		
	SET_REG(PORTIDX, 3);                              //ѡ��PORT0�˿�  
	#if	SDA_PP_Out_En==1	
		SET_REG_BITS(PINMOD10, PINMOD1, PIN_H_MODE_PP);	//P31������Ϊ��©+����    SDA���� 
		SET_REG_BITS(PINMOD10, PINMOD0, PIN_L_MODE_OD);	//P30������Ϊ��©+����    SCL���� 
	#else
		SET_REG_BITS(PINMOD10, PINMOD1, PIN_H_MODE_OD);	//P31������Ϊ��©+����    SDA���� 
		SET_REG_BITS(PINMOD10, PINMOD0, PIN_L_MODE_OD);	//P30������Ϊ��©+����    SCL����
	#endif
	P3_0=1;        //������һ����������ģʽ
	P3_1=1;
}

/******************************************************************************************
** ��������: IIc_Start
** ��������: IIc��ʼ�ź�
** �������: ��
** �������: �� 
*******************************************************************************************/
void IIc_Start(void)
{
	SDA_OUT();     //SDA������������
  IIC_SDA_H();	  	  
  IIC_SCL_H();
  Delay_us(TIM_CNT);
  IIC_SDA_L();//��ʼ�źţ� ������SDA��ʱ����Ϊ��ʱ��SDA�Ӹߵ�ƽת��Ϊ�͵�ƽ
  Delay_us(TIM_CNT);
  IIC_SCL_L();//ǯסI2C���ߣ�׼�����ͻ��������(ע����ÿ��IICͨѶ�׶���ɺ�ֹͣλ���⣩����ʱ��������ǯס����) 
	Delay_us(TIM_CNT);
}	  

/******************************************************************************************
** ��������: IIc_Stop
** ��������: IIcֹͣ�ź�
** �������: ��
** �������: �� 
*******************************************************************************************/
void IIc_Stop(void)
{
	IIC_SCL_L();
  Delay_us(TIM_CNT/2);
	SDA_OUT();//SDA������������
	Delay_us(TIM_CNT/2);
  IIC_SDA_L();//����SDA���ߣ�׼�����ͽ���/ֹͣ�ź�
  Delay_us(TIM_CNT/2);
  IIC_SCL_H();//ʱ��������ߣ�׼�����ͽ���/ֹͣ�ź�
	Delay_us(TIM_CNT);	
  IIC_SDA_H();//����/ֹͣ�źţ�	��ʱ����Ϊ���ڼ��ڣ�SDA�ӵ͵�ƽת��Ϊ�ߵ�ƽ
  Delay_us(TIM_CNT/2);		
}

 /******************************************************************************************
** ��������: IIc_Wait_Ack
** ��������: IIc�ȴ�Ӧ���ź�
** �������: ��
** �������: 1������Ӧ��ʧ��   0������Ӧ��ɹ�
*******************************************************************************************/
unsigned char IIc_Wait_Ack(void)
{
  unsigned int ucErrTime=0;
	IIC_SCL_L(); 
	Delay_us(TIM_CNT/2);	 
	SDA_IN();      //SDA����Ϊ���� 
	Delay_us(TIM_CNT/2);	
  while(READ_SDA())
  {
		CLRWDT = 1;//ι�� 
    ucErrTime++;
    if(ucErrTime>5000)
    {
      IIc_Stop();
      return 1;
    }
  }
  IIC_SCL_H();//��Ҫ�SCL����ߣ���ס�ӻ�Ӧ���־��������⣺��֪�ӻ��ѽ��յ�Ӧ���źţ��Ӷ�ʱ�ӻ��ͷ�SDA���ߣ�
  Delay_us(TIM_CNT);
	IIC_SCL_L();//ǯס����
	Delay_us(TIM_CNT);
  return 0;  
} 

/******************************************************************************************
** ��������: IIc_Ack
** ��������: IIcӦ����
** �������: ��
** �������: �� 
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
** ��������: IIc_NAck
** ��������: IIc��Ӧ����
** �������: ��
** �������: �� 
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
** ��������: IIc_Send_Byte
** ��������: IIc����һ���ֽ�
** �������: 1����Ӧ��    0����Ӧ��	
** �������: �� 
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
		
    if(txd&0x80)//��λ��ǰ
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
	IIC_SDA_H();//SDA����ߵ�ƽ��Ϊ����Ӧ����׼��
	Delay_us(TIM_CNT/2);
}
 

/******************************************************************************************
** ��������: IIc_Read_Byte
** ��������: IIc��ȡһ���ֽ�
** �������: 1������ACK    0������nACK 	
** �������: �� 
*******************************************************************************************/
unsigned char IIc_Read_Byte(unsigned char ack)
{
  unsigned char i,receive=0;
	IIC_SCL_L();
	Delay_us(TIM_CNT/2);
  SDA_IN();//SDA����Ϊ����
	Delay_us(TIM_CNT/2);
  for(i=0;i<8;i++ )
  {
    IIC_SCL_L(); 
    Delay_us(TIM_CNT);
    IIC_SCL_H();
    receive<<=1;//��λ��ǰ
    if(READ_SDA())receive++;   
    Delay_us(TIM_CNT); 
  }		
	IIC_SCL_L();
	Delay_us(TIM_CNT);
  if (!ack)
    IIc_NAck();//����nACK
  else
    IIc_Ack(); //����ACK   
  return receive;
}


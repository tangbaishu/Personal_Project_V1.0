#ifndef _SGM41511_H_
#define _SGM41511_H_

#include "SYS_Init.h"

#define	SLAVE_ADDRESS				0x6B								//�ӻ���ַ
#define	SLAVE_ADR_WRITE			((0x6B<<1)| 0x00)		//�ӻ���ַд��
#define	SLAVE_ADR_READ			((0x6B<<1)| 0x01)		//�ӻ���ַ��ȡ

void Register_Write(uchar register_Adr, uchar writer_data);
uchar Register_Read(uchar register_Adr);
void	Input_Electricity(void);
uchar Continue_Adr_Read(uchar start_Adr, uchar read_num);
#endif

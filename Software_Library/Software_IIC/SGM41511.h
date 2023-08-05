#ifndef _SGM41511_H_
#define _SGM41511_H_

#include "SYS_Init.h"

#define	SLAVE_ADDRESS				0x6B								//从机地址
#define	SLAVE_ADR_WRITE			((0x6B<<1)| 0x00)		//从机地址写入
#define	SLAVE_ADR_READ			((0x6B<<1)| 0x01)		//从机地址读取

void Register_Write(uchar register_Adr, uchar writer_data);
uchar Register_Read(uchar register_Adr);
void	Input_Electricity(void);
uchar Continue_Adr_Read(uchar start_Adr, uchar read_num);
#endif

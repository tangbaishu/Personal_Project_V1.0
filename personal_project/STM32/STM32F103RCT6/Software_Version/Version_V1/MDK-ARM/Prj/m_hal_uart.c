#include "m_hal_prj.h"
#include "stdio.h"

UART_HandleTypeDef	uart_config;


void m_hal_uart_init(void)
{
	__HAL_RCC_USART1_CLK_ENABLE();
	uart_config.Instance = USART1;
	uart_config.Init.Mode = UART_MODE_TX_RX;
//	uart_config.Init.HwFlowCtl=SDIO_CLKCR_HWFC_EN;//硬件流使能
	uart_config.Init.BaudRate=115200;
	uart_config.Init.OverSampling=UART_OVERSAMPLING_16;//ͨ
	uart_config.Init.Parity=UART_PARITY_NONE;
	uart_config.Init.StopBits=UART_STOPBITS_1;
	uart_config.Init.WordLength=UART_WORDLENGTH_8B;
	HAL_UART_Init(&uart_config);
	
	
	HAL_UART_IRQHandler(&uart_config);//中断
	HAL_NVIC_SetPriorityGrouping(NVIC_PRIORITYGROUP_0);
	
}

void HAL_UART_MspInit(UART_HandleTypeDef *huart)
{
	GPIO_InitTypeDef uart_gpio_init;
	uart_gpio_init.Mode=GPIO_MODE_AF_OD;
	uart_gpio_init.Pin=GPIO_PIN_10;
	uart_gpio_init.Pull=GPIO_PULLUP;
	uart_gpio_init.Speed=GPIO_SPEED_HIGH;
	HAL_GPIO_Init(GPIOA,&uart_gpio_init);//RX
	uart_gpio_init.Mode=GPIO_MODE_AF_PP;
	uart_gpio_init.Pin=GPIO_PIN_9;
	HAL_GPIO_Init(GPIOA,&uart_gpio_init);//TX
}

//void uchar(uint8_t p)
//{
//	
//}

int fputc(int c, FILE *p)
{
	uart_config.Instance->DR = (uint8_t)c;
	while((uart_config.Instance->DR & 0x40) == 0)
	{
		
	}
	uart_config.Instance->DR = 0;
	return 0;
}

void USART1_IRQHandler(void)
{
	
}

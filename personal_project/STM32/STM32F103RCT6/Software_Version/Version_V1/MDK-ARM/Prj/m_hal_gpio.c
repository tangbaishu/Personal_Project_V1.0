#include "m_hal_prj.h"

GPIO_InitTypeDef m_gpio_init;

void m_hal_gpio_init(void)
{
	__GPIOD_CLK_ENABLE();
	m_gpio_init.Mode=GPIO_MODE_OUTPUT_PP;
	m_gpio_init.Pin=GPIO_PIN_2;
	m_gpio_init.Pull=GPIO_PULLUP;
	m_gpio_init.Speed=GPIO_SPEED_HIGH;
	HAL_GPIO_DeInit(GPIOD,GPIO_PIN_2);
	HAL_GPIO_Init(GPIOD,&m_gpio_init);
	HAL_GPIO_WritePin(GPIOD,GPIO_PIN_2,GPIO_PIN_SET);
}





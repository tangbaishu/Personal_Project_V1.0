#include "m_hal_prj.h"

void m_hal_prj_init(void)
{
	m_hal_gpio_init();
	m_hal_uart_init();
}


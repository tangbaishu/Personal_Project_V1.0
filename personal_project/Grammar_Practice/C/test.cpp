#include <stdio.h>

typedef unsigned int uint;

int main(void)
{
	uint raw_data[1]={12345};
	uint RAM_Data=0;
	RAM_Data=65535-raw_data[0];
	printf("RAM_Data=%d\r\n",RAM_Data);
} 

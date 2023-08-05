#include <stdio.h>

int main(void)
{
	char a[1]={1};
	char First_CFGW[]="WS_V132D";
	char b=0; 
	char *p =a;
	printf("a[0]->&:%d\r\n",a);
	printf("b->&:%d\r\n",&b);
	printf("p->&:%d\r\n",p);	
	p++;
	printf("p->&:%d\r\n",p);
}

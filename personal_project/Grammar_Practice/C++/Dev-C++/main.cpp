#include <iostream>
#include "printf_out.h"
#include "out.h"
#include "quote.h"
#include "TimeDate.h"
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace tlb;

int main(int argc, char** argv) 
{
	printf_out();
	tlb_Printf();
	Quote_Test();
	Get_Time(); 
	return 0;
}

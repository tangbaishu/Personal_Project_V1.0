/*
 * main.cpp
 *
 *  Created on: 2022年9月21日
 *      Author: WX
 */
#include <iostream>
#include <stdio.h>
#include <string>
#include <ctime>
#include <Mclass.h>

#include "Struct_Test.h"
#include "Time_Date.h"
#include "namespace_test.h"
#include "Struct_Test_01.h"

using namespace std;
using namespace tlb;

int main(void)
{
	Get_Time_Date();
	Struct_Test_Ture();
	Mclass_Functon();
	namespace_test();
	Struct_Test_01_Dispose();
}





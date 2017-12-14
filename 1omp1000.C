#include <stdio.h>
#include <omp.h>
#include <stdlib.h>
int main()
{
int i;int j;
double a[1000],b[1000],c[1000];

#pragma omp parallel for
for(i=0;i<1000;i++)
a[i]=rand()%1000000/1000.0; //产生各个随机数 
#pragma omp parallel for
for(j=0;j<1000;j++)
b[j]=rand()%1000000/1000.0; //产生各个随机数 　
#pragma omp parallel for
for(i=0;i<1000;i++)
{

c[i]=a[i]*b[i];
}}

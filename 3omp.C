#include<stdio.h>
#include<stdlib.h>
#include<omp.h>
int main(){
FILE *fp2;
fp2 = fopen("素数","w");
int i=0,a=0,k=0;
#pragma omp parallel for private(a)
for(i=2;i<=1000000;i++)
{
for(a=2;a<=i/2;a++)
{
if(i%a==0)
{
break;
}
}
if(2*a>i)
{fprintf(fp2,"%d\n",i);k++;}
}
printf("素数的个数是：%d\n",k);
fclose(fp2);
return 0;
}

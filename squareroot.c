#include <stdio.h>
double squareroot(double num,double precision){
	double root,y = num;
	while(1){
		root = 1/2 * (y+num/y)
		if(root - y < precision && root - y > -precision){
			break;
		}
		y = root
	}
	return root;
}
int main(int argc, char **argv)
{
	double x,l=0.00000000001,result;
	printf("Donner un nombre : ");
	scanf(&x)
	result = squareroot(x,l)
	printf("The result is =  %lf \n",result)
}

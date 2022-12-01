#include <stdio.h>
double absol(double n){
	if(n<0) return -n;
	return n;
}
double squareroot(double num,double precision){
	double root,y = num;
	while(1){
		root = 0.5*(y+num/y) ;
		if(absol(root - y) < precision){
			break;
		}
		y = root ;
	}
	return root;
}
int main(int argc, char **argv)
{
	double x,l=0.0000000000001,result;
	printf("Donner un nombre : ");
	scanf("%lf",&x);
	result = squareroot(x,l);
	printf("The result is =  %lf \n",result);
}

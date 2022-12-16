#include <stdio.h>

int main(){
	//solving dy/dx  = y with euler method
	//y(0) = 1
	//h = 0.1
	//x = 0.1, 0.2, 0.3, 0.4, 0.5
	//y = 1.10517, 1.2214, 1.34986, 1.49182, 1.64872
	double y = 1;
	double x = 1.3;
	double h = 0.1;
	double y1;
	int i;
	for(i = 0; i < 10; i++){
		y1 = y + h * y;
		y = y1;
		x = x + h;
		printf("y(%lf) = %lf", x, y);
	}
		//write test to check if y is correct
		//if(y == 1.64872){
		//	printf("y(%lf) = %lf", x, y);
		//}
		//else{
		//	printf("y(%lf) = %lf", x, y);
		//}
	return 0;
}

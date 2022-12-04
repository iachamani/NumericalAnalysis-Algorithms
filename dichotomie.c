#include <stdio.h>
#include <math.h>

double func(double t){
    return tan(t*t)-t;
}
double average(double a,double b){
    return a+b/2;
}
int main(){
    double precision=0.0000000001,x,y,result;
    printf("Donner la borne minimum pour l'intervalle [x,y] :");
    scanf("%lf",&x);
    printf("Donner la borne superieur pour l'intervalle [x,y] :");
    scanf("%lf",&y);
    for(int i=0;i<floor(log(y-x)-log(precision)/log(2));i++){
        if(func(x)*func(average(x,y))>0) x = average(x,y);
        else if(func(x)*func(average(x,y))<0) y = average(x,y);
        else result = average(x,y);
    }
    printf("The root is = %.7lf\n",result);
    return 0;
}
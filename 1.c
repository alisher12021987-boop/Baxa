#include <stdio.h>
int main(){
int a,b;
scanf("%d%d", &a, &b);
int sum=0;
if(a!=b){
    sum=a+b;
    printf("%d", sum);

}else{
    printf("0");
}
}
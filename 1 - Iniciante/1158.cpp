/*
Wrong answer (5%)
*/

#include <iostream>

using namespace std;

int testes,x,y,soma=0,cont=0;

int main()
{
    cin >> testes;
    for(int i = 0;i < testes;i += 1){
       cin >> x >> y;
       cont = 0;
    
       if(x % 2 == 0){
          cont = 0;
       }else{
          cont = 1;
          soma += x;
       }
       x+= 1;
       while(cont != y){
           if(x % 2 == 1){
               soma += x;
               cont += 1;
           }
           x += 1;
       }
       cout << soma << endl;
       soma = 0;
    }
    return 0;
}

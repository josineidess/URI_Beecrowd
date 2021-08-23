#include <iostream>
#include <iomanip>

using namespace std;

float salario,reajuste;
double percentual=0;

int perc;
int main()
{
    cin >> salario;    
    if(salario >= 0 && salario <= 400.00){
        reajuste = (salario * 15)/100;
        salario = salario + reajuste;
        perc = 15;
    }else if(salario >= 400.01 && salario <= 800.00){
        reajuste = (salario * 12)/100;
        salario = salario + reajuste;
        perc = 12;
    }else if(salario >= 800.01 && salario <= 1200.00){
        reajuste = (salario * 10)/100;
        salario = salario + reajuste;
        perc = 10;
    }else if(salario >= 1200.01 && salario <= 2000.00){
        reajuste = (salario * 7)/100;
        salario = salario + reajuste;
        perc = 7;
    }else if(salario > 2000){
        reajuste = (salario * 4)/100;
        salario = salario + reajuste;
        perc = 4;
    }
    cout <<fixed << setprecision(2);
    cout << "Novo salario: " << salario << endl;
    cout <<fixed << setprecision(2);
    cout << "Reajuste ganho: " << reajuste << endl;
    cout << "Em percentual: " << perc << " %" << endl;
    return 0;
}
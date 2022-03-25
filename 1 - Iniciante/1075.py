#include <iostream>

using namespace std;

int main()
{
   int n;
   cin >> n;
   for(int e = 1; e < 10000; e++){
       if(e % n == 2){
          cout << e << endl;
       }
   }

   return 0;
}

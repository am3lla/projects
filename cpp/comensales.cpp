#include <iostream>
#include <cstdlib>
#include <thread>
#include <vector>
#include <mutex>
#include <chrono>

using namespace std;
//mutex para sincronizar
mutex mu;
//total de platos a cocinar/comer
const int TOTAL_PLATOS = 10;

//th1 come platos impares (consumidor)
void th1(vector<int> *platos, int *platoEnLaMesa, int *platosCocinados) {
    //mientras no se han cocinado los 10 platos
    while(*platosCocinados <= TOTAL_PLATOS) {
        //obtenemos el acceso    
        mu.lock();   
            //Si hay un plato en la mesa y es impar, comerlo
            if(*platoEnLaMesa != 0 && *platoEnLaMesa % 2 != 0) {
                //Avisar que no molesten, estamos comiendo
                cout<<"Th1 esta comiendo"<<endl;                   
                //agregar a nuestros platos  
                (*platos).push_back(*platoEnLaMesa);   
                //comer nos toma 2 segundos  
                this_thread::sleep_for(chrono::milliseconds(2000));
                //ya comimos, limpiamos el plato
                *platoEnLaMesa = 0;
                 
            } 
        //liberamos el acceso
        mu.unlock();
        //le damos tiempo de comer a otros  
        this_thread::sleep_for(chrono::milliseconds(2000));

    }

}
//th2 come platos pares (consumidor)
void th2(vector<int> *platos, int *platoEnLaMesa, int *platosCocinados) {
    //mientras no se han cocinado los 10 platos 
    while(*platosCocinados <= TOTAL_PLATOS) {
        //obtenemos el acceso
        mu.lock();
            //Si hay un plato en la mesa y es par, comerlo  
            if(*platoEnLaMesa!=0 && *platoEnLaMesa % 2 == 0) {
                //Avisar que no molesten, estamos comiendo   
                cout<<"Th2 esta comiendo"<<endl;
                //agregar a nuestros platos 
                (*platos).push_back(*platoEnLaMesa);   
                //comer nos toma 2 segundo
                this_thread::sleep_for(chrono::milliseconds(2000));
                //ya comimos, limpiamos el plato  
                *platoEnLaMesa = 0; 

            }
        //liberamos el acceso  
        mu.unlock();
        //le damos tiempo de comer a otros
        this_thread::sleep_for(chrono::milliseconds(2000));

    }

}

//obtener el numero de plato
int siguientePlato() {

    int plato = rand()%10+1;
    
    return plato;

}

//colocar el plato en la mesa (productor)
void ponerPlato(int *platoEnLaMesa, int *platosCocinados) {
    //mientras no se han cocinado 10 platos  
    while(*platosCocinados <= TOTAL_PLATOS) {
        //obtenemos el acceso 
    	mu.lock();        
            //solo si ya se comieron el plato anterios  
            if(*platoEnLaMesa == 0) { 
                //colocar el siguiente plato  
                (*platoEnLaMesa) = siguientePlato();
                //agregar 1 plato mas a los cocinados
	        (*platosCocinados)++;  
            }
        //liberar el acceso 
	mu.unlock();
        //darles tiempo de comer
        this_thread::sleep_for(chrono::milliseconds(2000));

    }

}

int main() {

    srand((unsigned)time(NULL));  
    //platos de los comensales   
    vector<int> platosTh1;
    vector<int> platosTh2;
    //platos cocinados y platos en la mesa inicialmente
    int platosCocinados = 0; 
    int platoEnLaMesa = 0;
     
    //threads 
    thread t1(th1,&platosTh1,&platoEnLaMesa,&platosCocinados);
    thread t2(th2,&platosTh2,&platoEnLaMesa,&platosCocinados);
    thread t3(ponerPlato,&platoEnLaMesa,&platosCocinados);
    //unir al main
    t1.join();
    t2.join();
    t3.join();
    //Imprimir platos
    cout<<"\nTh1 comio: ";
    for(vector<int>::const_iterator i = platosTh1.begin(); i!=platosTh1.end();++i) {
        cout<<*i<<" ";
    }
 
    cout<<"\nTh2 comio: ";      
    for(vector<int>::const_iterator i = platosTh2.begin(); i!=platosTh2.end();++i) {
       cout<<*i<<" ";
    }

    cout<<endl;  

    return EXIT_SUCCESS;

}

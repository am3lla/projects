#include <iostream>
#include <cstdlib>

using namespace std;

class SecuenciaCaracteres {

	private:
		static const int TAMANIO = 100;
  		char vector_privado[TAMANIO];
  		int total_utilizados;
	
	public:
	
    	SecuenciaCaracteres ():total_utilizados (0) {}
    	
  		int capacidad () { return TAMANIO; }
  		
		int totalUtilizados () { return total_utilizados; }		

		char elemento (int indice) { return vector_privado[indice]; }

		void modifica (int indice_componente, char nuevo) {
		
			if (indice_componente >= 0 && indice_componente < total_utilizados) {
			
			  vector_privado[indice_componente] = nuevo;
			  
			}
			
		}
		
		void aniade (char nuevo) {

			if (total_utilizados < TAMANIO) {

				vector_privado[total_utilizados++] = nuevo;

			}

		}

		void imprimir () {						    
		    
			for (int i = 0; i < total_utilizados; i++) {
			
				cout << vector_privado[i] << ", ";
				
			}
						
		}

		void Elimina (int posicion) {

			if (posicion >= 0 && posicion < total_utilizados) {
			
				int tope = total_utilizados-1;
				//Recorrer los elementos
				for (int i = posicion ; i < tope ; i++) {
				
					vector_privado[i] = vector_privado[i+1];
					
				}
				
				total_utilizados--;
				
			}			
			
		}

		void eliminarOcurrencias (char a_borrar) {
		
			for (int i=0; i<total_utilizados; i++) {
			
   				if (vector_privado[i] == a_borrar)
	   			Elimina (i--);
   		
	 		}
/*
		    //Inicialmente no sabemos cuantas veces esta repetido el valor
            bool parar = false;
            //indice
            int i = 0;
            
            //Mientras no parar
            while(!parar) {
            
            	//Si el elemento en la posición i es igual al caracter a eliminar
            	if (vector_privado[i] == a_borrar) {
            	
            	  Elimina(i);
				  continue;
				  
				}
				
				//si alcanzamos el final del vector
				if(i == total_utilizados) {
				    //paramos
					parar = true;
					continue;
				}
				
				//Incrementar el indice
				i++;
				
            }   */         			

		}

};


int main () {

  const char TERMINADOR = '#';
  int total_introducidos;
  char caracter;
  char caracter_a_borrar;
  int capacidad_secuencia;
  
  SecuenciaCaracteres secuencia;

  total_introducidos = 0;
  capacidad_secuencia = secuencia.capacidad ();
  
  cout << "Introduzca los caracteres(Terminador: #): " << endl;
  caracter = cin.get ();

  while (caracter != TERMINADOR && total_introducidos < capacidad_secuencia) {
      secuencia.aniade (caracter);
      caracter = cin.get ();
  }

  cout << "Introduzca el caracter a borrar: " << endl;
  cin >> caracter_a_borrar;

  secuencia.eliminarOcurrencias (caracter_a_borrar);
  secuencia.imprimir ();
  
  return EXIT_SUCCESS;

}


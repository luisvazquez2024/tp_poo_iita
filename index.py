"""
		Trabajo Practico 3: "El Reproductor"
"""

class Reproductor:
		def __init__(self):
				self._fuente=MP3(); 
	
		def reproducir(self):  
			print(self._fuente.reproducir());

		def cambiar_fuente(self,nueva_fuente):
				self._fuente=nueva_fuente;    


class MP3():
		def reproducir(self):  
			return 'Sonando MP3';
   
   
  
class CD():	
	def reproducir(self):  
			return 'Sonando CD';
   
   
class Consola():	
		def reproducir(self):  
			return 'Sonando Consola';

  
  
  


repro = Reproductor();
repro.reproducir()
repro.cambiar_fuente(CD());
repro.reproducir()
repro.cambiar_fuente(Consola());
repro.reproducir()


 
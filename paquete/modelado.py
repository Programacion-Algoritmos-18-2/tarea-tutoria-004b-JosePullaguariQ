class Persona(object):#Creamos la clase object Persona

	#Definimos el constructor de la clase Persona
	def __init__(self):
		self.nombres = " "
		self.edad = 0

	#Metodos de agregar para los atributos
	def agregar_nombres(self,n):
		self.nombres = n

	def agregar_edad(self,n):
	    self.edad = n

	#Metodos de obtener para los atributos
	def obtener_edad(self):
		return self.edad

	#Metodo para presentar datos
	def presentar_datos(self):
		c="%s-%s"%(self.obtener_edad(),self.nombres)
		return c


class Estudiante(Persona):#Creamos la clase Estudiante con herencia de Persona

	#Definimos el constructor de la clase Estudiante
	def __init__(self):

		#Definimos la palabra super para heredar de la clase Persona
		super(Estudiante,self).__init__()
		self.nota = 0

	#Metodo para agregar nota
	def agregar_nota(self,n):
		self.nota = n

	#Metodo para obtener nota
	def obtener_nota(self):
		return nota

	#Metodo para presentar datos con herencia con la palabra reservada super
	def presentar_datos(self):
		#c="%s-%s-%s"%(self.nombres,self.edad,self,nota)
		c="%s-%s"%(super(Estudiante,self).presentar_datos(),
					self.nota)
		return c
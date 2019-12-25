""" Permite colocar los modulos que se necesite importar """
# .nombreModulo ---> el "." indique mismo nivel "./"
from .suma import Suma
from .resta import Resta

# Subpaquete
# from .advanced import Multiplication
from .advanced import Div

CONST = 'Algo constante'

# Tambien se puede colocar alguna logica necesaria
def create_operation(num, num2):
	return Suma(num, num2)
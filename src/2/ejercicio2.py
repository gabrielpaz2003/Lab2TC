# UNIVERSDIDAD DEL VALLE DE GUATEMALA
# Teoria de la Computacion
# Gabriel Alberto Paz González - 221087
# Fecha: 26/07/2024

# Ejercicio #2
# Descripción: Programa que verifica si una expresión matemática está balanceada o no, además de mostrar los pasos de la pila.

class balanceo:
    def __init__(self):
        self.abrir = "({["
        self.cerrar = ")}]"
        self.simbolos = {")": "(", "}": "{", "]": "["}

    def es_balanceado(self, expression):
        pila = []
        registro_pila = []
        for caracter in expression:
            if caracter in self.abrir:
                pila.append(caracter)
                registro_pila.append(f"Apila {caracter}: {pila}")
            elif caracter in self.cerrar:
                if pila and pila[-1] == self.simbolos[caracter]:
                    pila.pop()
                    registro_pila.append(f"Desapila {caracter}: {pila}")
                else:
                    registro_pila.append(f"Error con {caracter}: {'' if not pila else 'se esperaba ' + self.simbolos[caracter] + ', encontró ' + pila[-1]}")
                    return False, registro_pila

        if pila:
            registro_pila.append(f"Error: faltan cerrar {pila}")
            return False, registro_pila
        return True, registro_pila

def leerArchivo(ruta_archivo):
    verificador = balanceo()
    with open(ruta_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    for numero, linea in enumerate(lineas, start=1):
        expresion = linea.strip()
        balanceado, registro_pila = verificador.es_balanceado(expresion)
        resultado = "balanceada" if balanceado else "no balanceada"
        print(f"Línea {numero}: {expresion} -> {resultado}")
        print("Pasos de la pila:")
        for paso in registro_pila:
            print(paso)
        print("-" * 40)

if __name__ == "__main__":
    leerArchivo('resources\expressions.txt')

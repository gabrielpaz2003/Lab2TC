# UNIVERSDIDAD DEL VALLE DE GUATEMALA
# Teoria de la Computacion
# Gabriel Alberto Paz González - 221087
# Fecha: 26/07/2024

# Ejercicio #3
# Descripción: Programa que convierte una expresión regular a su forma postfija y muestra los pasos de la pila.

archivo = 'resources/inregex.txt'
log = 'resources/outregex.txt'

class AnalizadorRegex:
    def __init__(self):
        self.precedencias = {
            '(': 1,
            '|': 2,
            '.': 3,
            '?': 4,
            '*': 4,
            '+': 4,
        }
        self.simbolos = {'|', '?', '+', '*', '(', ')'}

    def prioridad(self, simbolo):
        return self.precedencias.get(simbolo, 6)

    def preparar_regex(self, regex):
        resultado = []
        i = 0
        while i < len(regex):
            actual = regex[i]
            resultado.append(actual)

            if actual == '\\':
                i += 1
                resultado.append(regex[i])
            elif actual not in self.simbolos and i + 1 < len(regex):
                siguiente = regex[i + 1]
                if siguiente not in self.simbolos and siguiente not in {'\\', '(', ')'}:
                    resultado.append('.')

            i += 1

        return ''.join(resultado)

    def convertir_a_postfijo(self, regex):
        salida = []
        pila = []
        detalles = []
        regex_procesado = self.preparar_regex(regex)

        i = 0
        while i < len(regex_procesado):
            simbolo = regex_procesado[i]
            if simbolo.isalnum() or simbolo == '\\':
                salida.append(simbolo)
                if simbolo == '\\' and i + 1 < len(regex_procesado):
                    i += 1
            elif simbolo == '(':
                pila.append(simbolo)
            elif simbolo == ')':
                while pila and pila[-1] != '(':
                    salida.append(pila.pop())
                pila.pop()
            else:
                while pila and self.prioridad(pila[-1]) >= self.prioridad(simbolo):
                    salida.append(pila.pop())
                pila.append(simbolo)

            detalles.append(f"Elemento: {simbolo}, Pila: {list(pila)}, Salida: {list(salida)}")
            i += 1

        while pila:
            salida.append(pila.pop())
            detalles.append(f"Vaciar pila, Pila: {list(pila)}, Salida: {list(salida)}")

        return ''.join(salida), detalles

def procesar_expresiones(archivo_entrada, archivo_salida):
    analizador = AnalizadorRegex()
    with open(archivo_entrada, 'r') as entrada, open(archivo_salida, 'w') as salida:
        for expresion in entrada:
            expresion_postfijo, transformaciones = analizador.convertir_a_postfijo(expresion.strip())
            salida.write(f"Expresion Postfijo: {expresion_postfijo}\nDetalle de pasos:\n")
            for transformacion in transformaciones:
                salida.write(transformacion + "\n")
            salida.write("\n")

# Ejemplo de uso
procesar_expresiones(archivo, log)

operandoA = 1
operandoB = 2
suma = operandoA + operandoB
print(f'El resultado de la suma es: {suma}')
resta = operandoA - operandoB
print(f'El resultado de la resta es: {resta}')
multiplicacion: int = operandoA * operandoB
print(f'El resultado de la multiplicación es: {multiplicacion}')
division = operandoA / operandoB
print(f'El resultado de la División es: {division}')
division2 = operandoA // operandoB
print(f'La division con número entero es: {division2}')
modulo = operandoA % operandoB
print(f'El residuo o modulo de la división es: {modulo}')
exponente = operandoA ** operandoB
print(f'El resultado del exponente es: {exponente}')

# ejercicio de calcular el rectangulo

print('***Calcular el area de un rectangulo***')
alto = int(input('Ingresa el alto en cms: '))
ancho = int(input('Ingresa el ancho en cms: '))
area = alto * ancho
print(f'El area es: {area} cms')
perimetro = (alto + ancho) * 2
print(f'El perimetro es: {perimetro} cms')
print('Fin del programa...')

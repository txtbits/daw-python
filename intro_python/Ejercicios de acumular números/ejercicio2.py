
'''
Modifica el programa para que calcule la suma entre dos números que introducirá el usuarios.
'''

# Etiqueta resultado inicializada a 0
resultado = 0
num1 = int(raw_input('Introduce el número menor: '))
num2 = int(raw_input('Introduce el número mayor: '))

# for ...range para recorrer del num1 al num2
for num in range(num1,num2+1): #+1 porque no coge el valor final

# Incrementando resultado en cada iteración
    resultado += num 

# Mostrar resultado
print 'El resultado es %d' %resultado
    
    

'''Escribe un programa que cree estas figuras:
*
**
***
****
   *
  **
 ***
****
   *
  ***
 *****
*******

'''

estrellas = int(raw_input('Introduce el numero de estrellas que quieras: '))



for x in range(1, estrellas+1):
    print '*'* x


for x in range(1, estrellas+1):
    print "%s%s" %(' ' * (estrellas-x), '*' * x)


for x in range(1, estrellas+1):
    n = x
    n = n * 2 - 1
    print "%s%s" %(' ' * (estrellas-x), '*' * n)


    

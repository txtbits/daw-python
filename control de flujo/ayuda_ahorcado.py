while True:
    x = raw_input('> ')
    if x == 'x':
        break



for l in oculta:
    if l in letras_introducidas:
        print l, #la coma es para que salgan las palabras en horizontal
    else:
        print '_',

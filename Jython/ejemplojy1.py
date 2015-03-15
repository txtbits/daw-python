from javax.swing import JButton, JFrame

frame = JFrame("Hola, Jython",
                defaultCloseOperation = JFrame.EXIT_ON_CLOSE,
                size = (300,300))

def cambiar_texto(evento):
    print "pulsado"

boton = JButton("Pulsame!", actionPerformed = cambiar_texto)


frame.add(boton)
frame.setVisible(True)
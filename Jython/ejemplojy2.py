
"""
Swing JList example in Jython.

Creates a simple list of cities and then updates a JLabel based on the
the city selected.

Greg Moore
Sept 2007
"""

# Using import * is bad form but since this is just a example I'll take the
# easy way out instead of specifing each package.
from javax.swing import *
from java.awt import *

class JListExample:

    def listSelect(self,event):
        # Process the events from the list box and update the label
        selected = self.list.selectedIndex
        if selected >= 0:
            cityName = self.data[selected]
            self.label.text = cityName
    
    def __init__(self):
    
        # These lines setup the basic frame, size and layout
        # the setDefaultCloseOperation is required to completely exit the app
        # when you click the close button
        frame = JFrame("Jython JList Example")
        frame.setSize(200, 225)
        frame.setLayout(BorderLayout())
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
    
        # set up the list and the contents of the list
        # the python typle get converted to a Java vector
        self.data = ('Portland','San Francisco','Madrid','Venice','Starnberg','New York','Paris','London')
        self.list = JList(self.data)
        spane = JScrollPane()
        spane.setPreferredSize(Dimension(100,125))
        spane.getViewport().setView((self.list))
    
        # a panel is a bit over kill but this is a demo. :)
        panel = JPanel()
        panel.add(spane)
        frame.add(panel,BorderLayout.CENTER)
    
        # create the button, and city label and the show our work
        # with Jython only one line is needed create a button and attach an
        # event handler.
        btn = JButton('Select',actionPerformed=self.listSelect)
        frame.add(btn,BorderLayout.SOUTH)
        self.label = JLabel(' Select City and click select')
        frame.add(self.label,BorderLayout.NORTH)
        frame.pack()
        frame.setVisible(True)


if __name__ == '__main__':
        #start things off.
        JListExample()
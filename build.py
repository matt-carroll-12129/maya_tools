import maya.cmds as mc 

class newShelf():
	def __init__(self, name):
		self.name=name 
		self.labelbackground = (0,0,0,0)
		self.labelColour = (.9, .9, .9)
		mc.shelfLayout(self.name, p="ShelfLayout")
		mc.setParent(self.name)
		self.build()
		
	def build(self):
	    pass

	def addButton(self, label, icon="commandButton.png"):
		mc.setParent(self.name)
		mc.shelfButton(width=37, height=37, image=icon, l=label)

class myShelf(newShelf):
    def build(self):
        self.addButton("testing")
        self.addButton("testing2")
        self.addButton("testing3")

myShelf("custom")
myShelf("custom2")
myShelf("custom3")
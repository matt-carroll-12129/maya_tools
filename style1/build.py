import maya.cmds as mc
import os
from subprocess import call
import submit_maya

def rush_dash():
	call('/usr/local/rush/bin/irush')

def rush_submit():
	submit_maya.MAIN_Input(())
	

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

	def addButton(self, label, command, icon="commandButton.png", flat=0):
		mc.setParent(self.name)
		mc.shelfButton(width=50, height=35, image=icon, l=label, c=command, fla=flat)

class myShelf(newShelf):
    def build(self):
        self.addButton("testing", rush_dash)
        self.addButton("testing2", rush_submit)

myShelf("custom")

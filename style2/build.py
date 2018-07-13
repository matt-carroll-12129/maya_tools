import maya.cmds as mc
import os
from subprocess import call
import submit_maya

def rush_dash(*args):
    call('/usr/local/rush/bin/irush')

def rush_submit(*args):
    submit_maya.MAIN_Input(())
    

class newShelf():
    def __init__(self, name):
        self.name=name 
        self.labelBackground = (0,0,0,0)
        self.labelColour = (.9, .9, .9)
        mc.shelfLayout(self.name, p="ShelfLayout")
        mc.setParent(self.name)
        self.build()

    def addButton(self, label, icon="commandButton.png", flat=0):
        mc.setParent(self.name)
        mc.shelfButton(width=50, height=35, image=icon, l=label, fla=flat)
        
    def addMenuItem(self, parent, label, command):
        return mc.menuItem(p=parent, l=label, c=command)
    
    def build(self):
        pass
    


class myShelf(newShelf):
    def build(self):
        self.addButton("testing")
        p=mc.popupMenu(b=1)
        self.addMenuItem(p, "rush dashboard", rush_dash)
        self.addMenuItem(p, "submit rush", rush_submit)

myShelf("custom")
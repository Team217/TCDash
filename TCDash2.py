import sys
import time
from networktables import NetworkTable
import logging
logging.basicConfig(level=logging.DEBUG)

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class main(GridLayout):
    cols=6
    def __init__(self,**kwargs):
        super(main,self).__init__(**kwargs)
        
        sd = NetworkTable.getTable("SmartDashboard")
        self.add_widget(Label(text='Auton',size_hint_x=None,size_hint_y=None, width=200,height=50))
		
        self.Nothing = ToggleButton(text='Nothing',group='auton',size_hint_x=None,size_hint_y=None, width=100,height=50)
        self.Nothing.bind(on_press=self.sendNothing)
        self.add_widget(self.Nothing)
		
        self.Rockwall = ToggleButton(text='Rockwall',group='auton',size_hint_x=None,size_hint_y=None, width=100,height=50)
        self.Rockwall.bind(on_press=self.sendRockwall)
        self.add_widget(self.Rockwall)
        
        self.RoughTerrain = ToggleButton(text='RoughTerrain',group='auton',size_hint_x=None,size_hint_y=None, width=100,height=50)
        self.RoughTerrain.bind(on_press=self.sendRoughTerrain)
        self.add_widget(self.RoughTerrain)

        self.Moat = ToggleButton(text='Moat',group='auton',size_hint_x=None,size_hint_y=None, width=100,height=50)
        self.Moat.bind(on_press=self.sendMoat)
        self.add_widget(self.Moat)

        self.Ramparts = ToggleButton(text='Ramparts',group='auton',size_hint_x=None,size_hint_y=None, width=100,height=50)
        self.Ramparts.bind(on_press=self.sendRamparts)
        self.add_widget(self.Ramparts)

        self.Hoodlabel = Label(text = 'Hood: N/A',size_hint_x=None,size_hint_y=None, width=100,height=50)
        self.add_widget(self.Hoodlabel)
        
        self.Update = Button(text='update',size_hint_x=None,size_hint_y=None, width=100,height=50)
        self.Update.bind(on_press=self.update)
        self.add_widget(self.Update)
    
    def update(self,value):
        self.Hoodlabel.text = 'Hood: ' + str(sd.getNumber('HOODPOS',217))
    
    def sendNothing(self,value):
        sd.putString('AUTON','Nothing')
		
    def sendRockwall(self,value):
        sd.putString('AUTON','RockWall')

    def sendRoughTerrain(self,value):
        sd.putString('AUTON','RoughTerrain')

    def sendMoat(self,value):
        sd.putString('AUTON','Moat')

    def sendRamparts(self,value):
        sd.putString('AUTON','Ramparts')
        
class TCDash(App):
    NetworkTable.setIPAddress("127.0.0.1")#for robot will be 10.2.17.2 aka ip of rio
    NetworkTable.setClientMode()
    NetworkTable.initialize()

    sd = NetworkTable.getTable("SmartDashboard")
    
    def build(self):
       return main()

if __name__ == '__main__':
    sd = NetworkTable.getTable("SmartDashboard")
    TCDash().run()

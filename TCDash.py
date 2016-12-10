import sys
import time
from networktables import NetworkTable
import logging
logging.basicConfig(level=logging.DEBUG)

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class TCDash(App):
    NetworkTable.setIPAddress("127.0.0.1")#for robot will be 10.2.17.2 aka ip of rio
    NetworkTable.setClientMode()
    NetworkTable.initialize()

    sd = NetworkTable.getTable("SmartDashboard")
    
    def build(self):
        sd = NetworkTable.getTable("SmartDashboard")
        parent = GridLayout(cols=6)
        parent.add_widget(Label(text='Auton',size_hint_x=None,size_hint_y=None, width=200,height=50))
		
        Nothing = ToggleButton(text='Nothing',group='auton',size_hint_x=None,size_hint_y=None, width=100,height=50)
        Nothing.bind(on_press=self.sendNothing)
        parent.add_widget(Nothing)
		
        Rockwall = ToggleButton(text='Rockwall',group='auton',size_hint_x=None,size_hint_y=None, width=100,height=50)
        Rockwall.bind(on_press=self.sendRockwall)
        parent.add_widget(Rockwall)
        
        RoughTerrain = ToggleButton(text='RoughTerrain',group='auton',size_hint_x=None,size_hint_y=None, width=100,height=50)
        RoughTerrain.bind(on_press=self.sendRoughTerrain)
        parent.add_widget(RoughTerrain)

        Moat = ToggleButton(text='Moat',group='auton',size_hint_x=None,size_hint_y=None, width=100,height=50)
        Moat.bind(on_press=self.sendMoat)
        parent.add_widget(Moat)

        Ramparts = ToggleButton(text='Ramparts',group='auton',size_hint_x=None,size_hint_y=None, width=100,height=50)
        Ramparts.bind(on_press=self.sendRamparts)
        parent.add_widget(Ramparts)
        return parent

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

if __name__ == '__main__':
    sd = NetworkTable.getTable("SmartDashboard")
    TCDash().run()

# Developed By Sundar Balamurugan

import kivy
kivy.require('1.9.0')


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
import pickle
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
import angry_birds
import car_race

a=0
b=0
Window.pos=(0,0)
Window.size = (1366,738)

Builder.load_string("""
#: import ListAdapter kivy.adapters.listadapter.ListAdapter
#: import ListItemButton kivy.uix.listview.ListItemButton 

    
<MButton@Button>:
    font_size: 20
    color: 0, 0, 0, 1
    size: 700, 700
    background_normal: ''
    background_down: ''
    background_color:0,0,0,1
    size_hint: 1, 1
<M1Button@Button>:
    font_size: 20
    color: 0, 0, 0, 1
    size: 700, 700
    background_normal: ''
    background_down: ''
    background_color:0,0,0,1
    size_hint: 1, 1

<Cust7Button@Button>:
    font_size: 20
    color: 0, 0, 0, 1
    size: 350, 30
    background_normal: ''
    background_down: '1.jpg'
    background_color: .88, .88, .88, 1
    size_hint: .2, .2
<CButton@Button>:
    font_size: 20
    color: 0, 0, 0, 1
    size: 350, 30
    background_normal: ''
    background_down: ''
    background_color: .88, .88, .88, 1
    size_hint: 1,1
 
<Custom4Popup>:
    size_hint: .5, .5
    height: 30
    spacing: 10
    auto_dismiss: False
    title: "The Popup"
   
    Button:
        text: "Close"
        on_press: root.dismiss() 
<CustButton@Button>:
    font_size: 15
    color: 0, 0, 0, 1
    height:20
    width:300
    background_normal: ''
    background_down: 'bkgrd-down-color.png'
    background_color:0,0,0,1
    spacing :10

<screen1>:
   
    MButton:
        pos:0,0
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.transition.duration = 1
            root.manager.current = 'Screenlo'
    Image:
        source: "images/radssoon-logo.png"
    
        Label:
            font_size: 20
            text:"Press here to start"
            
            pos:650,150
            
<Screenlo>:
    M1Button:
        pos:0,0
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.transition.duration = 1
            root.manager.current = 'Screen2'
    Image:
        source: "images/playstem.png"
    
        Label:
            font_size: 15
            
            text:"Press on screen to start"
            pos:635,250
        
        
<Screen2>:
    
    CButton:
        pos: 0,0
        background_normal:"images/joystick.png"

    CustButton:
        text: "Demo version Games available"
        color:1,1,1,1
        pos: 550,670
        size_hint_x:None
        size_hint_y:None
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.transition.duration = 1
            root.manager.current = 'screen4'
        
    Button:
        background_normal:"images/ab.png"
        pos: 110,450
        size_hint_x:0.15
        size_hint_y:0.25
        color: 0,0,0,1
        on_press: root.open_popupab()
    Button:
        background_normal:"images/car.png"
        pos: 410,450
        size_hint_x:0.15
        size_hint_y:0.25
        color: 0,0,0,1
        on_press: root.open_popupcar()   
    Button:  
        background_normal:"images/ss.png"
        size:(300,300)
        pos: 710,450
        size_hint_x:0.15
        size_hint_y:0.25
        color: 0,0,0,1
        on_press: 
            root.open_popup1()
    Button:
        background_normal:"images/sports.png"
        pos: 1020,450
        size_hint_x:0.15
        size_hint_y:0.25
        color: 0,0,0,1
        on_press: root.open_popup2()
    Button:
        background_normal:"images/arcade.png"
        pos: 110,150
        size_hint_x:0.15
        size_hint_y:0.25
        color: 0,0,0,1
        on_press: root.open_popup3()
    Button:
        background_normal:"images/gta.png"
        pos: 410,150
        size_hint_x:0.15
        size_hint_y:0.25
        color: 0,0,0,1
        on_press: root.open_popup4()
    Button:
        background_normal:"images/wwe.png"
        pos: 710,150
        size_hint_x:0.15
        size_hint_y:0.25
        color: 0,0,0,1
        on_press: root.open_popup5()
    
    Button:
        text: ""
        background_normal:"images/3d.png"
        pos: 1020,150
        size_hint_x:0.15
        size_hint_y:0.25
        color: 0,0,0,1  
        on_press: root.open_popup6()
""")



class CustomPopup(Popup):
    pass
class Screen1(Screen):
    pass
class Screenlo(Screen):
    pass
class Screen2(Screen):
    def open_popup1(self):
        the_popup =Popup(title='Radssoon', content=Image(source='images/minion1.png'),
                    size_hint=(0.15, 0.38), size=(400, 400))
        #the_popup= CustomPopup()
        the_popup.open()
    def open_popup2(self):
        the_popup =Popup(title='Radssoon', content=Image(source='images/minion2.png'),
                    size_hint=(0.15, 0.38), size=(400, 400))
        #the_popup= CustomPopup()
        the_popup.open()
    def open_popup3(self):
        the_popup =Popup(title='Radssoon', content=Image(source='images/minion3.png'),
                    size_hint=(0.15, 0.38), size=(400, 400))
        #the_popup= CustomPopup()
        the_popup.open()
    def open_popup4(self):
        the_popup =Popup(title='Radssoon', content=Image(source='images/mini4.png'),
                    size_hint=(0.15, 0.38), size=(400, 400))
        #the_popup= CustomPopup()
        the_popup.open()
    def open_popup5(self):
        the_popup =Popup(title='Radssoon', content=Image(source='images/mini5.png'),
                    size_hint=(0.15, 0.38), size=(400, 400))
        #the_popup= CustomPopup()
        the_popup.open()
    def open_popup6(self):
        the_popup =Popup(title='Radssoon', content=Image(source='images/mini6.png'),
                    size_hint=(0.15, 0.38), size=(500, 500))
        #the_popup= CustomPopup()
        the_popup.open()
    def open_popupab(self):
        # the_popup =Popup(title='Radssoon', content=Image(source='1.jpg'),
        #             size_hint=(None, None), size=(500, 500))
        angry_birds.video_start()
        #the_popup= CustomPopup()
        #the_popup.open()
    def open_popupcar(self):
        # the_popup =Popup(title='Radssoon', content=Image(source='1.jpg'),
        #             size_hint=(None, None), size=(500, 500))
        car_race.video_start()
screen_manager = ScreenManager()
screen_manager.add_widget(Screen1(name="screen1"))
screen_manager.add_widget(Screen2(name="Screen2"))
screen_manager.add_widget(Screenlo(name="Screenlo"))  
class PlayStemApp(App):  
    def build(self):
        return screen_manager        
    icon = "images/ps.jpg"
def scr1():
    sample_app = PlayStemApp()
    sample_app.run()
scr1()
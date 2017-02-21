###Commited by Shannon

###This file is for the horizontal screen

import sys
import os
sys.path.append(os.getcwd() + "/lib/garden.tei_knob/")

import kivy
from kivy.app import App
from kivy.properties     import *
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scatter    import Scatter
from kivy.uix.image      import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.config import Config

from tei_knob import  Knob

import kivy
from kivy.lib.osc         import oscAPI 
from kivy.app import App
# Import clock (required by osc listener)
from kivy.clock           import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class sender(App):

    def build(self):
        oscAPI.init()

    def sendMessage(self, tokenNum):
        # ip = '198.21.242.1'
        ip = '198.21.196.89'

        port = 5000
        print("Sending Message! " + tokenNum)
        oscAPI.sendMsg( '0', [tokenNum], ipAddr= ip, port= port)
        
    pass

sender().run()

class MyKnob(Knob):
    # Object property that receives the image
    obj = ObjectProperty()

    # on_knob is called if value, token_id or token_placed chage
    def on_knob(self, value, pattern_id):
        angle = value
        self.obj.rotation = angle
        # sender.sendMessage(self, str(int(self.obj.rotation)))
        # print("Token #: " + str(self.knobimg_source) + "\nRotation Value: " + str(self.obj.rotation))

    def on_token_placed(self, instance, value):
        videoNum = 0

        if self.knobimg_source == "knob1.png":
            videoNum = 0
        elif self.knobimg_source == "knob2.png":
            videoNum = 1
        elif self.knobimg_source == "knob3.png":
            videoNum = 2
        else:
            videoNum = 3

        sender.sendMessage(self, str(videoNum))
        print("Token Number: " + str(videoNum))

class TeiKnobApp(App):
    def build(self):
        Config.set('graphics', 'width', '950')
        Config.set('graphics', 'height', '540')
        # creates a float layout
        root = FloatLayout(size=(1920,1080), pos = (0,0))
        # Creates a scatter widget
        scatter = Scatter()
       
                 # Creates an image widget
        root_image = Image(source='Bottom_Screen1.jpeg', size_hint_x=None, width=1920,
                                              size_hint_y=None, height=1080,
                                              allow_stretch = True,
                                              keep_ratio = True)
        root.add_widget(root_image)

        # Creates a MyKnob object
        knob1 = MyKnob(size = (300, 300),
                         min = 0, max = 360,
                         step = 1,
                         show_marker = True,
                         knobimg_source = "knob1.png",
                         marker_img = "img/bline.png",
                         markeroff_color = (0.3, 0.3, .3, 1),
                         pattern_id= 99, #(ids 1 to 8, or 99 for no id)
                         debug = False,
                         obj = scatter) # Passes the object to the knob

        knob2 = MyKnob(size = (300, 300),
                         min = 0, max = 360,
                         step = 1,
                         show_marker = True,
                         knobimg_source = "knob2.png",
                         marker_img = "img/bline.png",
                         markeroff_color = (0.3, 0.3, .3, 1),
                         pattern_id= 99, #(ids 1 to 8, or 99 for no id)
                         debug = False,
                         obj = scatter) # Passes the object to the knob

        knob3 = MyKnob(size = (300, 300),
                         min = 0, max = 360,
                         step = 1,
                         show_marker = True,
                         knobimg_source = "knob3.png",
                         marker_img = "img/bline.png",
                         markeroff_color = (0.3, 0.3, .3, 1),
                         pattern_id= 99, #(ids 1 to 8, or 99 for no id)
                         debug = False,
                         obj = scatter) # Passes the object to the knob

        knob4 = MyKnob(size = (300, 300),
                         min = 0, max = 360,
                         step = 1,
                         show_marker = True,
                         knobimg_source = "knob4.png",
                         marker_img = "img/bline.png",
                         markeroff_color = (0.3, 0.3, .3, 1),
                         pattern_id= 99, #(ids 1 to 8, or 99 for no id)
                         debug = False,
                         obj = scatter) # Passes the object to the knob

        widget1 = RelativeLayout(size_hint = (None, None), 
                                 size = (300,300),
                                 pos = (94,29))
        widget1.add_widget(knob1)


        widget2 = RelativeLayout(size_hint = (None, None), 
                                 size = (300,300),
                                 pos = (572,29))
        widget2.add_widget(knob2)


        widget3 = RelativeLayout(size_hint = (None, None), 
                                 size = (300,300),
                                 pos = (1048,29))
        widget3.add_widget(knob3)


        widget4 = RelativeLayout(size_hint = (None, None), 
                                 size = (300,300),
                                 pos = (1526,29))
        widget4.add_widget(knob4)
        
        
        # Adds knob to the root
        root.add_widget(widget1)

        root.add_widget(widget2)

        root.add_widget(widget3)

        root.add_widget(widget4)



        return root

TeiKnobApp().run()

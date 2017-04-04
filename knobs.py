### This file was adapted from the original example file
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
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.uix.relativelayout import RelativeLayout
from kivy.config import Config
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from tei_knob import  Knob
from kivy.uix.video import Video

import kivy
from kivy.lib.osc         import oscAPI 
from kivy.app import App
# Import clock (required by osc listener)
from kivy.clock           import Clock
#Wade made all changes related to resolution
from win32api import GetSystemMetrics

class sender():

    def build(self):
        oscAPI.init()

    def sendMessage(self, tokenNum):
        # ip = '198.21.242.1'
        #ip = '192.168.43.151'
        ip = '198.21.199.110'

        port = 5000
        print("Sending Message! " + tokenNum)
        oscAPI.sendMsg( '0', [tokenNum], ipAddr= ip, port= port)
        


#videoHS = Video(source='transition1.mp4')


class MyKnob(Knob):
    # Object property that receives the image
    obj = ObjectProperty()
    o2 = ObjectProperty()
    send = sender();
    send.build()
    count = 0; 
 

    degrees = 0
    # on_knob is called if value, token_id or token_placed chage
    def getDegrees():
        return degrees

    def on_knob(self, value, pattern_id):
        angle = value
        degrees = angle
        self.obj.rotation = angle
        
        degrees = int(degrees*1000)
        print(degrees)
        if degrees % 1 == 0:
            self.o2.seek(float(degrees)/360000.0)
            print(float(degrees/360000.0))
         
        #sender.sendMessage(self, str(int(self.obj.rotation)))
         #print("Token #: " + str(self.knobimg_source) + "\nRotation Value: " + str(self.obj.rotation))

    # on_token_place is called when the token is detected, sends the message
    def on_token_placed(self, instance, value):
        videoNum = 0

        if self.count == 500:
            count = 0

       
        
        if self.knobimg_source == "knob1.png":
            videoNum = 0
            if self.count % 2 == 0:
                self.o2.source = 'HS1.mp4'
                #videoHS = Video(source='HS1.mp4')

        elif self.knobimg_source == "knob2.png":
            videoNum = 1
            if self.count % 2 == 0:
                self.o2.source = 'HS2.mp4'
                
        elif self.knobimg_source == "knob3.png":
            videoNum = 2
            if self.count % 2 == 0:
                self.o2.source = 'HS1.mp4'    
        else:
            videoNum = 3
            if self.count % 2 == 0:
                self.o2.source = 'HS2.mp4'

        print value
        print "value"
        if value == False:
            self.o2.state = 'stop'

        self.count = self.count + 1
        # sends the number of the knob to the verticle screen so it knows
        # what video to play
        sender.sendMessage(self.send, str(videoNum))
        print("Token Number: " + str(videoNum))   


    def pauseVid(self):
        print "Pause this video!!"
        self.o2.state = 'pause'

#done by wade
resolution = [GetSystemMetrics(0), GetSystemMetrics(1)]
def scale_to_res(val, i, j):
        
        return (int(float(val) / float(i) * float(resolution[j])))


class TeiKnobApp(App): 
    count = 0
    cHolder = None
    videoHS =  None
    knob1 = knob2 = knob3 = knob4 = None

    def build(self):

        Config.set('graphics', 'width', str(resolution[0]))
        Config.set('graphics', 'height', str(resolution[1]))
        Config.set('graphics', 'borderless', 1)
        Config.set('graphics', 'fullscreen', 1)
        # creates a float layout
        root = FloatLayout(size=(resolution[0],resolution[1]), pos = (0,0))
        # Creates a scatter widget
        scatter = Scatter()
       
        # Creates an image widget
        root_image = Image(source='Bottom_Screen1.png', size_hint_x=None, width=resolution[0],
                                              size_hint_y=None, height=resolution[1],
                                              allow_stretch = True,
                                              keep_ratio = True)

        
        self.cHolder = RelativeLayout(size_hint = (None, None), 
                                 size = (scale_to_res(500, 500, 0),scale_to_res(500, 500, 0)),
                                 pos = (scale_to_res(0, 1980, 0), scale_to_res(-310, 800, 1))) #1610



        self.videoHS = Video(source='HS1.mp4', play = False, options={'allow_stretch':True})
    
        #videoHS = Video(source='HS1.mp4', play = False)
        #videoHS = Video(source='transition1.mp4')

        self.videoHS.play = True
        
        self.videoHS.position = 2
        #videoHS.state = 'pause'

        #cHolder.size = (scale_to_res(500, 500, 0),scale_to_res(500, 500, 0))


        videolist = []
        videolist.insert(0, self.videoHS)
        
        self.cHolder.add_widget(self.videoHS)
        root.add_widget(self.cHolder)
        root.add_widget(root_image)

        # Creates the knob objects - creates first knob
        self.knob1 = MyKnob(size = (scale_to_res(315, 1980, 0),scale_to_res(315, 1980, 0)),
                         min = 0, max = 360,
                         step = 1,
                         show_marker = True,
                         knobimg_source = "knob1.png",
                         marker_img = "img/bline.png",
                         markeroff_color = (0.3, 0.3, .3, 1),
                         pattern_id= 99, #(ids 1 to 8, or 99 for no id)
                         debug = False,
                         obj = scatter, o2 = self.videoHS) # Passes the object to the knob

        # Creates second knob object
        self.knob2 = MyKnob(size = (scale_to_res(315, 1980, 0),scale_to_res(315, 1980, 0)),
                         min = 0, max = 360,
                         step = 1,
                         show_marker = True,
                         knobimg_source = "knob2.png",
                         marker_img = "img/bline.png",
                         markeroff_color = (0.3, 0.3, .3, 1),
                         pattern_id= 99, #(ids 1 to 8, or 99 for no id)
                         debug = False,
                         obj = scatter, o2 = self.videoHS) # Passes the object to the knob

        # Creates third knob
        self.knob3 = MyKnob(size = (scale_to_res(315, 1980, 0),scale_to_res(315, 1980, 0)),
                         min = 0, max = 360,
                         step = 1,
                         show_marker = True,
                         knobimg_source = "knob3.png",
                         marker_img = "img/bline.png",
                         markeroff_color = (0.3, 0.3, .3, 1),
                         pattern_id= 99, #(ids 1 to 8, or 99 for no id)
                         debug = False,
                         obj = scatter, o2 = self.videoHS) # Passes the object to the knob

        # Creates fourth knob
        self.knob4 = MyKnob(size = (scale_to_res(315, 1980, 0),scale_to_res(315, 1980, 0)),
                         min = 0, max = 360,
                         step = 1,
                         show_marker = True,
                         knobimg_source = "knob4.png",
                         marker_img = "img/bline.png",
                         markeroff_color = (0.3, 0.3, .3, 1),
                         pattern_id= 99, #(ids 1 to 8, or 99 for no id)
                         debug = False,
                         obj = scatter, o2 = self.videoHS) # Passes the object to the knob




        


        # These functions place the konbs on the screen in the right position
        widget1 = RelativeLayout(size_hint = (None, None), 
                                 size = (scale_to_res(315, 1980, 0),scale_to_res(315, 1980, 0)),
                                 pos = (scale_to_res(96, 1980, 0), scale_to_res(40, 1080, 1))) #152
        widget1.add_widget(self.knob1)


        widget2 = RelativeLayout(size_hint = (None, None), 
                                 size = (scale_to_res(315, 1980, 0),scale_to_res(315, 1980, 0)),
                                 pos = (scale_to_res(585, 1980, 0), scale_to_res(40, 1080, 1))) #880
        widget2.add_widget(self.knob2)


        widget3 = RelativeLayout(size_hint = (None, None), 
                                 size = (scale_to_res(315, 1980, 0),scale_to_res(315, 1980, 0)),
                                 pos = (scale_to_res(1080, 1980, 0), scale_to_res(40, 1080, 1))) #1610
        widget3.add_widget(self.knob3)


        widget4 = RelativeLayout(size_hint = (None, None), 
                                 size = (scale_to_res(315, 1980, 0),scale_to_res(315, 1980, 0)),
                                 pos = (scale_to_res(1574, 1980, 0), scale_to_res(40, 1080, 1))) #2340
        widget4.add_widget(self.knob4)


                #done by wade
        widgetobj1 = Widget(pos = (scale_to_res(-220, 1980, 0), scale_to_res(-260, 1080, 1)), size_hint_x=None, width=425, size_hint_y=None, height=425)
        arrows1 = Image(source='arrows.png', size_hint_x=None, width=425,
                                              size_hint_y=None, height=425,
                                              pos = (0,0),
                                              allow_stretch = True,
                                              keep_ratio = True)
        scatter1 = Scatter(do_translation = False, do_scale = False, do_rotation = False, rotation = 0, size = widgetobj1.size, center = widgetobj1.center)
        scatter1.add_widget(arrows1)
        widgetobj1.add_widget(scatter1) 
        root.add_widget(widgetobj1) 

        widgetobj2 = Widget(pos = (scale_to_res(270, 1980, 0), scale_to_res(-260, 1080, 1)), size_hint_x=None, width=425, size_hint_y=None, height=425)
        arrows2 = Image(source='arrows.png', size_hint_x=None, width=425,
                                              size_hint_y=None, height=425,
                                              pos = (0,0),
                                              allow_stretch = True,
                                              keep_ratio = True)
        scatter2 = Scatter(do_translation = False, do_scale = False, do_rotation = False, rotation = 0, size = widgetobj2.size, center = widgetobj2.center)
        scatter2.add_widget(arrows2)
        widgetobj2.add_widget(scatter2) 
        root.add_widget(widgetobj2) 

        widgetobj3 = Widget(pos = (scale_to_res(765, 1980, 0), scale_to_res(-260, 1080, 1)), size_hint_x=None, width=425, size_hint_y=None, height=425)
        arrows3 = Image(source='arrows.png', size_hint_x=None, width=425,
                                              size_hint_y=None, height=425,
                                              pos = (0,0),
                                              allow_stretch = True,
                                              keep_ratio = True)
        scatter3 = Scatter(do_translation = False, do_scale = False, do_rotation = False, rotation = 0, size = widgetobj3.size, center = widgetobj3.center)
        scatter3.add_widget(arrows3)
        widgetobj3.add_widget(scatter3) 
        root.add_widget(widgetobj3) 

        widgetobj4 = Widget(pos = (scale_to_res(1267, 1980, 0), scale_to_res(-260, 1080, 1)), size_hint_x=None, width=425, size_hint_y=None, height=425)
        arrows4 = Image(source='arrows.png', size_hint_x=None, width=425,
                                              size_hint_y=None, height=425,
                                              pos = (0,0),
                                              allow_stretch = True,
                                              keep_ratio = True)
        scatter4 = Scatter(do_translation = False, do_scale = False, do_rotation = False, rotation = 0, size = widgetobj4.size, center = widgetobj4.center)
        scatter4.add_widget(arrows4)
        widgetobj4.add_widget(scatter4) 
        root.add_widget(widgetobj4) 


        anim1 = (Animation(rotation = -360, duration = 100) + Animation(rotation = 0, duration = 0))
        anim1.repeat = True
        anim1.start(scatter1);
        anim2 = (Animation(rotation = -360, duration = 100) + Animation(rotation = 0, duration = 0))
        anim2.repeat = True
        anim2.start(scatter2);
        anim3 = (Animation(rotation = -360, duration = 100) + Animation(rotation = 0, duration = 0))
        anim3.repeat = True
        anim3.start(scatter3);
        anim4 = (Animation(rotation = -360, duration = 100) + Animation(rotation = 0, duration = 0))
        anim4.repeat = True
        anim4.start(scatter4);
        
        
        # Adds knob to the root
        root.add_widget(widget1)

        root.add_widget(widget2)

        root.add_widget(widget3)

        root.add_widget(widget4)

        Clock.schedule_interval(lambda *x: self.cl(), 2)

        return root

    def cl(self):
        print "run clock"
        self.knob1.pauseVid()
        self.knob2.pauseVid()
        self.knob3.pauseVid()
        self.knob4.pauseVid()            
            
        

TeiKnobApp().run()




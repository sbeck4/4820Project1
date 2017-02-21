#Joshua Moore
#2/13/17

from kivy.app import App
from kivy.uix.video import Video
from kivy.uix.boxlayout import BoxLayout
from kivy.lib.osc import oscAPI 
from kivy.uix.actionbar import ActionBar
from kivy.core.window import Window
import time

class VideoPlayer(App):
    currentVid = '-1'	
    Vlayout =  BoxLayout(orientation='vertical')
    video1 = Video(source='transition1.mp4')
    video2 = Video(source='transition2.mp4') 
    video3 = Video(source='transition3.mp4') 
    video4 = Video(source='transition4.mp4')    

    Window.borderless = True
    def build(self):	
        return self.Vlayout

    def scrubVideo(self, vidNum, vidPos):
        if vidNum != self.currentVid: 
            if self.currentVid != '-1':
                self.video1.play = False
                self.video2.play = False
                self.video3.play = False
                self.video4.play = False
                self.Vlayout.clear_widgets()

            if vidNum == '0':
                self.Vlayout.add_widget(self.video1)
                self.video1.state = 'play'
            elif vidNum == '1':
                self.Vlayout.add_widget(self.video2)
                self.video2.state = 'play'
            elif vidNum == '2':
                self.Vlayout.add_widget(self.video3)
                self.video3.state = 'play'
            elif vidNum == '3':
                self.Vlayout.add_widget(self.video4)
                self.video4.state = 'play'
            self.currentVid = vidNum
            self.run()
    
    def closeVid(self):
        self.Vlayout.remove_widget(self.video)
        
#VideoPlayer().run()

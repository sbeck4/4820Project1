#Joshua Moore
#2/13/17

from kivy.app import App
from kivy.uix.video import Video
from kivy.uix.boxlayout import BoxLayout
from kivy.lib.osc         import oscAPI 

import time

# Warning, have a global Vlayout may cause an error. 

class VideoPlayer(App):
    currentVid = -1	
    Vlayout =  BoxLayout(orientation='vertical')
    start = 0
    video1 = Video(source='transition1.mp4')
    video2 = Video(source='transition2.mp4') 
    video3 = Video(source='transition3.mp4') 
    video4 = Video(source='transition4.mp4')    
    
    def build(self):	
	
       # start = time.time()
        
       ## self.scrubVideo(0,.9)

  
       ## self.scrubVideo(0,.9)

       
        return self.Vlayout

    def scrubVideo(self, vidNum, vidPos):
        
        if vidNum != self.currentVid:
            print 'lol'
            if self.currentVid >= 0:
                self.Vlayout.clear_widgets()
            if vidNum == 0:
                self.Vlayout.add_widget(self.video1)
                self.video1.state = 'play'
                #self.video.source = 'transition1.mp4'
                #print 'lol2'
            elif vidNum == 1:
                self.Vlayout.add_widget(self.video2)
                self.video2.state = 'play'
                #self.video = Video(source='transition3.mp4')
            elif vidNum == 2:
                self.Vlayout.add_widget(self.video3)
                self.video3.state = 'play'
                #self.video = Video(source='transition3.mp4')
            elif vidNum == 3:
                self.Vlayout.add_widget(self.video4)
                self.video4.state = 'play'
                #self.video = Video(source='transition4.mp4')
            currentVid = vidNum
            #self.Vlayout.add_widget(self.video)
        
        #self.video.unload()
        #self.video.state = 'play'




    def closeVid(self):
        self.Vlayout.remove_widget(self.video)

       
		
#VideoPlayer().run()


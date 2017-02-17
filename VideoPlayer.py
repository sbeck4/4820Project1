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
    
    def build(self):	
	
       # start = time.time()
        
       ## self.scrubVideo(0,.9)

  
       ## self.scrubVideo(0,.9)

       
        return self.Vlayout

    def scrubVideo(self, vidNum, vidPos):
        
        if vidNum != self.currentVid:

            print 'lol'
            if vidNum == 0:
                self.video = Video(source='transition1.mp4')
                print 'lol2'
            elif vidNum == 1:
                self.video = Video(source='transition3.mp4')
            elif vidNum == 2:
                self.video = Video(source='transition3.mp4')
            elif vidNum == 3:
                self.video = Video(source='transition4.mp4')
            currentVid = vidNum
            self.Vlayout.add_widget(self.video)

        #self.video.unload()
        self.video.state = 'play'




    def closeVid(self):
        self.Vlayout.remove_widget(self.video)

       
		
#VideoPlayer().run()


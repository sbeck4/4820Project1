#Joshua Moore
#2/13/17

from kivy.app import App
from kivy.uix.video import Video
from kivy.uix.boxlayout import BoxLayout
from kivy.lib.osc         import oscAPI 



# Warning, have a global Vlayout may cause an error. 

class VideoPlayer(App):
    currentVid = -1	
    Vlayout =  BoxLayout(orientation='vertical')
    def build(self):
        self.scrubVideo(0,.9)
        return self.Vlayout

    def scrubVideo(self, vidNum, vidPos):
        if vidNum != self.currentVid:
            if vidNum == 0:
                self.video = Video(source='vid2.mp4')
            elif vidNum == 1:
                self.video = Video(source='transition1.m4v')
            elif vidNum == 2:
                self.video = Video(source='transition3.m4v')
            elif vidNum == 3:
                self.video = Video(source='transition4.m4v')
            currentVid = vidNum
            self.Vlayout.add_widget(self.video)

        self.video.state = 'play'

		#while (self.video.loaded == -1): 
			
		#self.video.seek(vidPos)
		
VideoPlayer().run()











#Joshua Moore
#2/13/17

from kivy.app import App
from kivy.uix.video import Video
from kivy.uix.boxlayout import BoxLayout
from kivy.lib.osc         import oscAPI 



# Calling scrubVideo before VideoPlayer is instantiated might be the cause of an error/future errors

class VideoPlayer(App):
    #Set IP and port of receiver
	currentVid = -1
	Vlayout =   BoxLayout(orientation='vertical') 
	
	def build(self):		
		self.scrubVideo(0,.9)
		return self.Vlayout

	def scrubVideo(self, vidNum, vidPos):
		if vidNum != self.currentVid:
			if self.currentVid != -1:
				self.video.unload()

			if vidNum == 0:
				self.video = Video(source='vid0.m4v')
			elif vidNum == 1:
				self.video = Video(source='vid1.m4v')
			elif vidNum == 2:
				self.video = Video(source='vid2.m4v')
			elif vidNum == 3:
				self.video = Video(source='vid3.m4v')
			currentVid = vidNum
			
			self.Vlayout.add_widget(self.video)
			
		self.video.state = 'play'

		#while (self.video.loaded == -1): 
			
		#self.video.seek(vidPos)
		
VideoPlayer().run()











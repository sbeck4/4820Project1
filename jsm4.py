#Joshua Moore
#2/13/17

from kivy.app import App
from kivy.uix.video import Video
from kivy.uix.boxlayout import BoxLayout

# Import kivy osc library
from kivy.lib.osc         import oscAPI 

class VideoPlayer(App):
    #Set IP and port of receiver

	currentVid = -1
	Vlayout =   BoxLayout(orientation='vertical') 
	
	def build(self):
		vidNum = 0;
		
		Vlayout =  BoxLayout(orientation='vertical') 
		# self.video = Video(source
		# layout.add_widget(self.btn)

     	# self.label = Label(text="------------", font_size=50)
        # layout.add_widget(btn)
        # layout.add_widget(self.label)
		#self.scrubVideo(0,.2)

		self.scrubVideo(0,.9)
		return self.Vlayout

	def scrubVideo(self, vidNum, vidPos):
	
		if vidNum != self.currentVid:
			if vidNum == 0:
				self.video = Video(source='vid0.m4v')
			elif vidNum == 1:
				self.video = Video(source='vid1.m4v')
			elif vidNum == 2:
				self.video = Video(source='vid2.m4v')
			elif vidNum == 3:
				self.video = Video(source='vid3.m4v')

			self.Vlayout.add_widget(self.video)
	
		self.video.state = 'play'

		#while (self.video.loaded == -1): 
			

		#self.video.seek(vidPos)
		


VideoPlayer().run()











#Joshua Moore
#2/13/17

from kivy.app import App
from kivy.uix.video import Video
from kivy.uix.boxlayout import BoxLayout
from kivy.lib.osc         import oscAPI 



from kivy.uix.relativelayout import RelativeLayout
 
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.videoplayer import VideoPlayer
from kivy.config import Config
from random import randint

     
parent= Widget()
button= Button()
         
class MyApp(App):

    def build(self):
         Config.set('graphics', 'width', '1920')
         Config.set('graphics', 'height', '1000')

         button = Button(text='Play video', font_size=14)
         button.bind(on_press=on_button_press)  
         parent.add_widget(button) #add button 
         return parent
               
def on_button_press(self):
        
        rand = randint(1,4)

        if rand == 1:
            video = VideoPlayer(source='transition1.mp4', state='play')
        else:
            video = VideoPlayer(source='transition2.mp4', state='play')


        widget1 = RelativeLayout(size_hint = (None, None), 
                                 size = (1920,1080),
                                 pos = (0,0))
        widget1.add_widget(video)
        parent.add_widget(widget1) #add videoplayer
        return parent
     
if __name__ == '__main__':
    MyApp().run()











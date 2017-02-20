#Wade King implemented this!
from kivy.app           import App
from kivy.uix.button    import Button
from kivy.uix.label     import Label
from kivy.uix.boxlayout import BoxLayout

# Import kivy osc library
from kivy.lib.osc         import oscAPI 
# Import clock (required by osc listener)
from kivy.clock           import Clock

import VideoPlayer
class receiver(App):
    # Set ip and port to listen to
    ip = '0.0.0.0' # listens to any sender IP
    port = 5000    # listens only to this port
    play = VideoPlayer.VideoPlayer()

    def build(self):
        # Starts OSC
        oscAPI.init()  
        # Instanciates OSC listener
        oscid = oscAPI.listen(ipAddr=self.ip, port= self.port) 
        # listens for osc messages every screen refresh
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)

        # binds messages - this listens to messages if prefix /1/tok
        oscAPI.bind(oscid, self.receivedegrees, '0')

        # add a label to the screen
        #root = BoxLayout(orientation='vertical')
        #self.label = Label(text="This is our vertical sceen!", font_size='50sp')
        #root.add_widget(self.label)

        # console message - ready!
        print "Ready to receive!"
        #self.receivedegrees(0,0)
        #self.receivedegrees(90,1)
     #   self.receivedegrees(180)
     #   self.receivedegrees(270)
        # return root
        #return root
#if __name__ == "__main__":
    def receivedegrees(self, vidnum, instance):
        print "received data from sender"
        print "%s" % vidnum[2]
        vid_num = vidnum[2] #int(degrees[3])
        #time = float(degrees[2]) / 360;
        print "vidnum = %s" % vid_num
        #play = VideoPlayer.VideoPlayer()
        self.play.scrubVideo(vid_num, 0)
         
        return self.play


receiver().run()

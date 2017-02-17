#Wade King implemented this!
from kivy.app           import App
from kivy.uix.button    import Button
from kivy.uix.label     import Label
from kivy.uix.boxlayout import BoxLayout
#import Project1
# Import kivy osc library
from kivy.lib.osc         import oscAPI 
# Import clock (required by osc listener)
from kivy.clock           import Clock
#import jsm4
class receiver(App):
    # Set ip and port to listen to
    ip = '0.0.0.0' # listens to any sender IP
    port = 5000    # listens only to this port

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
        root = BoxLayout(orientation='vertical')
        self.label = Label(text="This is our vertical sceen!", font_size='50sp')
        root.add_widget(self.label)

        # console message - ready!
        print "Ready to receive!"
        #self.receivedegrees(0)
        #self.receivedegrees(90)
        #self.receivedegrees(180)
        #self.receivedegrees(270)
        # return root
        return root
#if __name__ == "__main__":
    def receivedegrees(self, degrees, instance):
        #print str(degrees[0])
        print "received data from sender"
        print "token degrees turned: %s" % degrees[2]

        percenttime = (float(degrees[2]) / 360) * 100;
        print "percent of way through video: %f" % percenttime
        #play = jsm4.VideoPlayer()
        #play.scrubVideo(1, time)
        #return play
        #print "opening video at timestamp"
        #scrubvideo(0, time)
    #OSC callback function
   # def cb_tok(self, value, instance): 
        # print message received to console
       # print "Message received: "
      #  print value
        #self.label.text = "Messages received: " + str(value[2])

receiver().run()
import threading
from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.graph import Graph, LinePlot
from kivy.uix.button import Button
import numpy as np

from tools import AudioPlayer


import time
import wave
#from audiostream import get_input

frames = []

'''
def mic_callback(buf):
    print('got', len(buf))
    frames.append(buf)

# get the default audio input (mic on most cases)


mic = get_input(callback=mic_callback)
mic.start()

time.sleep(5)

mic.stop()

wf = wave.open("test.wav", 'wb')
wf.setnchannels(mic.channels)
wf.setsampwidth(2)
wf.setframerate(mic.rate)
wf.writeframes(b''.join(frames))
wf.close()




def mic_callback(buf):
    print('got', len(buf))
    frames.append(buf)
    print('size of frames: ' + len(frames))

def bcallback(instance):
    print("we at bcallback")
    #mic = get_input(callback=mic_callback, source='mic')
    #mic = get_input(callback=mic_callback, source='default')
    mic = get_input(callback=mic_callback)
    print("we at mic = ")
    mic.start()
    print("mic.start")
    mic.poll()
    time.sleep(5)
    print("time.sleep")
    mic.stop()
    print("mic.stop")
    btn2 = Button(text='Audio Record End')
    btn2.bind(on_press=bcallback)
    return btn2

class MyApp(App):
    def build(self):
        btn1 = Button(text='Audio Record')
        btn1.bind(on_press=bcallback)
        return btn1


'''


from time import sleep
from audiostream import get_input
from audiostream import get_output, AudioSample

#get speakers, create sample and bind to speakers
stream = get_output(channels=2, rate=22050, buffersize=1024)
sample = AudioSample()
stream.add_sample(sample)


#define what happens on mic input with arg as buffer
def mic_callback(buf):
    print 'got', len(buf)
    #HERE: How do I manipulate buf?
    #modified_buf = function(buf)
    #sample.write(modified_buf)
    sample.write(buf)


# get the default audio input (mic on most cases)
mic = get_input(callback=mic_callback)
mic.start()
sample.play()
sleep(3)  #record for 3 seconds
mic.stop()
sample.stop()





#if name == 'main':
if __name__=='__main__':
    MyApp().run()

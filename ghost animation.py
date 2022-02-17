import opc
import time
import random

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

led = 0
while led<60:
    for led in range (60):
        leds = [(0,0,0)]*360
        leds[100-led] = (0,255,255)
        leds[160-led] = (0,255,255) 
        leds[220-led] = (0,255,255)
        leds[280-led] = (0,255,255)
        leds[340-led] = (0,255,255)
        leds[101-led] = (0,255,255)
        leds[102-led] = (0,255,255)
        leds[103-led] = (0,255,255)
        leds[163-led] = (0,255,255)
        leds[220-led] = (0,255,255)
        leds[221-led] = (0,255,255)
        leds[222-led] = (0,255,255)
        leds[223-led] = (0,255,255)
        
        leds[46+60-led] = (0,255,255)
        leds[106+60-led] = (0,255,255)
        leds[166+60-led] = (0,255,255)#this is the middle of the k 
        leds[226+60-led] = (0,255,255)
        leds[286+60-led] = (0,255,255)
        leds[46+60-led] = (0,255,255)
        leds[167+60-led] = (0,255,255)
        leds[168+120-led] = (0,255,255)
        leds[288-led] = (0,255,255)
        leds[349-led] = (0,255,255)
        leds[166+2-led] = (0,255,255)
        leds[106+3-led] = (0,255,255)

        leds[351-led] = (0,255,255)
        leds[351-60-led] = (0,255,255)
        leds[352-60-60-led] = (0,255,255)
        leds[352-180-led] = (0,255,255)
        leds[353-240-led] = (0,255,255)
        leds[354-60-60-led] = (0,255,255)
        leds[353-60-60-led] = (0,255,255)
        leds[354-60-60-led] = (0,255,255)
        leds[356-60-led] = (0,255,255)
        leds[356-led] = (0,255,255)
        leds[114+60-led] = (0,255,255)





        
      #  leds[293-led] = (255,255,255)
       # leds[352-led] = (255,255,255)
       # leds[230-led] = (255,255,255)
       # leds[230-led] = (255,255,255)
       # leds[120-led] = (255,255,255)
        #leds[110-led] = (255,255,255)
        #leds[170-led] = (255,255,255)
       ## leds[171-led] = (255,255,255)
        #leds[172-led] = (255,255,255)
        #leds[173-led] = (255,255,255)
       # leds[114-led] = (255,255,255)
        
        client.put_pixels(leds)
        time.sleep(.1)
    break
    

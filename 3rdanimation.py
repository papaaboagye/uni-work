import opc
import time
import random

leds = [(255,255,255)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

#for led in range(60):
 #   leds[led] = (255,204,255)
  #  time.sleep(.1)
   # client.put_pixels(leds)

#led = 0
#while led<60:
 #   leds[59 - led] = (255,153,255)
  #  time.sleep(.1)
   # client.put_pixels(leds)
    #led = led + 1


#led = 0
#while led<60:
#    leds[59 - led] = (255,153,255)
#    time.sleep(.01)
#    client.put_pixels(leds)
#   led = led + 1
led = 0
while led<60:
    leds[led] = (153, 153, 255)
    leds[led+60] = (255, 51, 51 )
    leds[led+120] = (255, 51, 51)
    leds[led+180] = (0, 0, 255)
    leds[led+240] = (0, 0, 153)
    leds[led+300] = (0, 0, 77)
    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1
while led<360:
    leds[led] = (255, 255, 25)
    leds[led+60] = (51, 51, 255)
    leds[led+120] = (51, 51, 255)
    leds[led+180] = (51, 51, 255)
    leds[led+240] = (51, 51, 255)
    leds[led+120] = (51, 51, 255)
    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1

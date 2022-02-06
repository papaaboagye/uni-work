# uni-work
my work
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
#    time.sleep(.1)
#    client.put_pixels(leds)
#    led = led + 1
led = 0
#while led<60:
#    leds[led] = (0, 0, 255)
#    leds[led+60] = (0, 0, 255)
#    leds[led+120] = (0, 0, 255)
#    leds[led+180] = (0, 0, 255)
#    leds[led+240] = (0, 0, 255)
#    leds[led+300] = (0, 0, 255)
    #client.put_pixels(leds)
    #time.sleep(.1)
    #led = led + 1
led = 0
while led<60:
    for rows in range (6): 
     leds[led + rows*60] = (59, 0, 179)
    for rows in range  (6):
        leds[59-led + rows*60] = (255,25,255)
    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1
led=30 
while led<60:
    for rows in range (6): 
     leds[led + rows*49] = (59, 0, 179)
    for rows in range  (6):
        leds[59-led + rows*49] = (255,25,255)
    client.put_pixels(leds)
    time.sleep(.1)
    led = led - 1
led=60




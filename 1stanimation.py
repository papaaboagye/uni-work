import opc
import time
import random

leds = [(255,255,255)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

#for led in range(60):
#    leds[led] = (255,204,255)
#    time.sleep(.1)
#    client.put_pixels(leds)

#led = 0
#while led<60:
#   leds[59 - led] = (255,153,255)
#time.sleep(.1)
#client.put_pixels(leds)
#led = led + 1


#led = 0
#while led<60:
 #   leds[59 - led] = (0,0,102)
 #   leds[120 + led] = (0, 0, 153)
 #   leds[180 + led] = (0, 0, 255)
 #   leds[240 - led] = (102, 102, 255)
 #   time.sleep(.1)
 #   client.put_pixels(leds)
 #   led = led + 1
led = 0
while led<60:
    leds[led] = (0, 51, 102)
    leds[led+60] = (0, 76, 153)
    leds[led+120] = (0, 102, 240)
    leds[led+180] = (0, 128, 255)
    leds[led+240] = (51, 153, 255)
    leds[led+300] = (102, 178, 255)
    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1
led = 0
while led<60:
    for rows in range (6): 
     leds[led + rows*60] = (59, 0, 179)
    for rows in range  (6):
        leds[59-led + rows*60] = (0,25,255)
    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1
led=30


while led<60:
    for rows in range (6): 
     leds[led + rows*60] = (59, 0, 179)
    for rows in range  (6):
        leds[45-led + rows*60 ] = (255,25,255)
        if led > 360:
break 
    client.put_pixels(leds)
    time.sleep(.1)
    led = led - 1
led=60


    

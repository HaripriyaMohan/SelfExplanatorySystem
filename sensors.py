import RPi.GPIO as GPIO
import time
import subprocess
import MySQLdb 
import os

GPIO.setmode(GPIO.BCM)
#used for sensing the customers
TRIG1 = 23 
ECHO1 = 24

TRIG2 = 20
ECHO2 = 21

#used for sensing the language
TRIG3 = 19
ECHO3 = 26

TRIG4 = 8
ECHO4 = 13

print "Distance Measurement In Progress"

while(true):

  GPIO.setup(TRIG1,GPIO.OUT)
  GPIO.setup(ECHO1,GPIO.IN)
  GPIO.setup(TRIG2,GPIO.OUT)
  GPIO.setup(ECHO2,GPIO.IN)

  GPIO.output(TRIG1, False)
  GPIO.output(TRIG2, False)
  print "Waiting For Sensor To Settle"

  time.sleep(2)

  GPIO.output(TRIG1, True)
  GPIO.output(TRIG2, True)
  time.sleep(0.00001)
  GPIO.output(TRIG1, False)
  GPIO.output(TRIG2, False)

  while GPIO.input(ECHO1)==0:
    pulse_start1 = time.time()
  while GPIO.input(ECHO2)==0:
    pulse_start2 = time.time()

  while GPIO.input(ECHO1)==1:
    pulse_end1 = time.time()
  while GPIO.input(ECHO2)==1:
    pulse_end2 = time.time()

  pulse_duration1 = pulse_end1 - pulse_start1
  pulse_duration2 = pulse_end2 - pulse_start2

  distance1 = pulse_duration1 x 17150
  distance2 = pulse_duration2 x 17150

  if(distance1<20 and distance2<20):
    subprocess.call('echo '+'please select your language by placing your hand over the sensors'+'|festival --tts', shell=True)
    GPIO.setup(TRIG3,GPIO.OUT)
    GPIO.setup(ECHO3,GPIO.IN)
    GPIO.setup(TRIG4,GPIO.OUT)
    GPIO.setup(ECHO4,GPIO.IN)

    GPIO.output(TRIG3, False)
    GPIO.output(TRIG4, False)
    print "Waiting For Sensor To Settle"

    time.sleep(2) 

    GPIO.output(TRIG3, True)
    GPIO.output(TRIG4, True)
    time.sleep(0.00001)
    GPIO.output(TRIG3, False)
    GPIO.output(TRIG4, False)

    while GPIO.input(ECHO3)==0:
      pulse_start3 = time.time()
    while GPIO.input(ECHO4)==0:
      pulse_start4 = time.time()

    while GPIO.input(ECHO3)==1:
      pulse_end3 = time.time()
    while GPIO.input(ECHO4)==1:
      pulse_end4 = time.time()

    pulse_duration3 = pulse_end3 - pulse_start3
    pulse_duration4 = pulse_end4 - pulse_start4

    distance3 = pulse_duration3 x 17150
    distance4 = pulse_duration4 x 17150
  
    #first language i.e., english is selected
    if(distance3 < 20): 
      subprocess.call('echo '+'you have selected english'+'|festival --tts', shell=True) 
      db = MySQLdb.connect(host="localhost",user="root",passwd="spaceman1236",db="self_explanatory_system")
      cur =db.cursor()
      cur.execute("select speak from data")
      data = cur.fetchall()
      text = str(data)
      subprocess.call('echo '+text+'|festival --tts', shell=True)
      time.sleep(1)
      subprocess.call('echo '+'thank you'+'|festival --tts', shell=True)
    #second available language i.e., english is selected
    if(distance4 < 20): 
      subprocess.call('echo '+'you have selected hindi'+'|festival --tts', shell=True) 
      os.system('aplay /home/pi/sound.wav')
      time.sleep(1)
      subprocess.call('echo '+'thank you'+'|festival --tts', shell=True)
  time.sleep(1)
GPIO.cleanup()
import socket
import fcntl
import struct
import RPi.GPIO
import time

#ip address read from rpi
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

ip = get_ip_address('wlan0');

client.bind((ip,8080))

#need to add a while loop to make sure the connection


#LED seeting. GPIO pins will be varied.
R,G,B=15,18,14

RPi.GPIO.setmode(RPi.GPIO.BCM)

RPi.GPIO.setup(R, RPi.GPIO.OUT)
RPi.GPIO.setup(G, RPi.GPIO.OUT)
RPi.GPIO.setup(B, RPi.GPIO.OUT)

pwmR = RPi.GPIO.PWM(R, 70)
pwmG = RPi.GPIO.PWM(G, 70)
pwmB = RPi.GPIO.PWM(B, 70)

pwmR.start(0)
pwmG.start(0)
pwmB.start(0)

try:

    t = 0.4
    while True:
        # Red only
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(100)
        pwmB.ChangeDutyCycle(100)
        time.sleep(t)
        
        # Green only
        pwmR.ChangeDutyCycle(100)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(100)
        time.sleep(t)
        
        # Blue only
        pwmR.ChangeDutyCycle(100)
        pwmG.ChangeDutyCycle(100)
        pwmB.ChangeDutyCycle(0)
        time.sleep(t)
        
        # Red+Green = yellow
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(100)
        time.sleep(t)
        
        # red+blue
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(100)
        pwmB.ChangeDutyCycle(0)
        time.sleep(t)
        
        # green+blue
        pwmR.ChangeDutyCycle(100)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(0)
        time.sleep(t)
        
        # all = white
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(0)
        time.sleep(t)
        
        # combination
        for r in xrange (0, 101, 20):
            pwmR.ChangeDutyCycle(r)
            for g in xrange (0, 101, 20):
                pwmG.ChangeDutyCycle(g)
                for b in xrange (0, 101, 20):
                    pwmB.ChangeDutyCycle(b)
                    time.sleep(0.01)

except KeyboardInterrupt:
    pass

pwmR.stop()
pwmG.stop()
pwmB.stop()

RPi.GPIO.cleanup()

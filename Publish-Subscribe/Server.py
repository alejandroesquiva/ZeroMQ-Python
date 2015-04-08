import zmq
from random import randrange
import time
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

while True:
    #zipcode = randrange(1, 100000)
    zipcode = 10001
    timestamp = time.time()
    #temperature = randrange(-80, 135)
    #relhumidity = randrange(10, 60)
    #print(zipcode)
    socket.send_string("%i %i" % (zipcode,timestamp))
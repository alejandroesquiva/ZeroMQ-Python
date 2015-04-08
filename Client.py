#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq
import time

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

start_time = time.time()

#  Do 10 requests, waiting each time for a response
for request in range(10000):
    #print("Sending request %s …" % request)
    socket.send(b"Hkhaslkfjhaklsjfhalksjhfalkjsfhalksjfhalksjfhlasfkjasdflkjasghdlfkjgasdlkfjgalksjdgflaksjdgflkasdgflkasdgflkajsdgflakjsdf")

    #  Get the reply.
    message = socket.recv()
    #print("Received reply %s [ %s ]" % (request, message))

# Time
elapsed_time = time.time() - start_time
print(elapsed_time)
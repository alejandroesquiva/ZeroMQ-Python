#
#   Weather update client
#   Connects SUB socket to tcp://localhost:5556
#   Collects weather updates and finds avg temp in zipcode
#

import sys
import zmq
import time

#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from weather server…")
socket.connect("tcp://localhost:5556")

# Subscribe to zipcode, default is NYC, 10001
zip_filter = sys.argv[1] if len(sys.argv) > 1 else "10001"

# Python 2 - ascii bytes to unicode str
if isinstance(zip_filter, bytes):
    zip_filter = zip_filter.decode('ascii')
socket.setsockopt_string(zmq.SUBSCRIBE, zip_filter)

start_time = time.time()

# Process 5 updates
total_temp = 0

for update_nbr in range(45000):
    string = socket.recv_string()
    zipcode, temperature, relhumidity = string.split()
    #print(zipcode)
    total_temp += int(temperature)

elapsed_time = time.time() - start_time
print(elapsed_time)
'''
total_msg = 0
for update_nbr in range(1000000):
    if (time.time() - start_time) < 1.0:
        string = socket.recv_string()
        zipcode, temperature, relhumidity = string.split()
        print(temperature)
        total_msg += 1
    else: break
elapsed_time = time.time() - start_time
print(elapsed_time)
print(total_msg)
'''
#print("Average temperature for zipcode '%s' was %dF" % (
 #     zip_filter, total_temp / update_nbr)
#)
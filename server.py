###########################################
#
# server.py
#
# This application listens and responds to
# a single messagea from a client
#
# usage: server.py <port>
#
#   - port: The port number the application
#           should listen on
#
#   NOTE: This application does not check for
#         improper input.
#
############################################

import sys
import socket

# Print out usage statement, if the user has provided commandline arguments
if len(sys.argv) != 2:
    print 'usage:', sys.argv[0], '<port>'
    sys.exit(0)

# Gather PORT number from commandline argument
HOST = ''
PORT = int(sys.argv[1])

# Create a socket using IPv4, and bind and listen on given port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

# Accept an incomming connection, then recv and print its message
conn, addr = s.accept()
print 'Connection by:', addr
data = conn.recv(1024)
print 'msg:      ', data

# Get return message from the user and send it to the client
data = raw_input('send back: ')
conn.sendall(data)

# Close the socket and connection
conn.close()




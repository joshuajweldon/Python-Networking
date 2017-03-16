###########################################
#
# client.py
#
# This application allows you to send
# and recieve a single message from a
# listening server.py
#
# usage: client.py <server IP> <port>
#
#   - server IP: The IP address of the
#                host running the server.py
#                application
#
#   - port:      The port number the host is
#                listening on
#
#   NOTE: This application does not check for
#         improper input.
#
############################################

import sys
import socket

# Print out usage statement, if the user has provided commandline arguments
if len(sys.argv) != 3:
    print 'usage:', sys.argv[0], '<server IP> <port>'
    sys.exit(0)


# Gather the HOST IP and PORT number from commandline arguments
HOST = sys.argv[1]
PORT = int(sys.argv[2])

# Create a socket using IPv4, and connect to the host
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Get message from the user and send it to the host
data = raw_input('what to send: ')
s.sendall(data)

# Recv and print return message from host
data = s.recv(1024)
print 'return msg:  ', data

# Close the socket and connection
s.close()


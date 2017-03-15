# Echo server program
import sys
import socket

if len(sys.argv) != 3:
    print 'usage:', sys.argv[0], '<server IP> <port>'
    sys.exit(0)

HOST = sys.argv[1]
PORT = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

data = raw_input('what to send: ')
s.sendall(data)
data = s.recv(1024)
print 'return msg:  ', data

s.close()



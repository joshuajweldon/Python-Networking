# Echo server program
import sys
import socket

if len(sys.argv) != 2:
    print 'usage:', sys.argv[0], '<port>'
    sys.exit(0)

HOST = ''
PORT = int(sys.argv[1])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

print 'Connected by', addr

data = conn.recv(1024)
print 'msg:      ', data

data = raw_input('send back: ')
conn.sendall(data)

conn.close()




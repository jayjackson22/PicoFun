import network
import socket
ssid = 'ClubMorty'
password = 'Morningpoop69'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)
status = wlan.ifconfig()
print(status[0])

#Listen for Connections
while True:
    try:
        cl, addr = s.accept()
        print('client connected from', addr)
        request = cl.recv(1024)
        print(request)
      
        response = "Hello"
      
        cl.send('HTTP/1.0 200 OK/r/nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
    
    except OSError as e:
        cl.close()
        print('connection closed')
import pyaudio, socket ,threading
port1 =8023
port2 = port1+1
ip = '127.0.0.1'
#ip = '192.168.43.142'z

chunk = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
index = 0

#def streamhandler():
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, output=True, frames_per_buffer=chunk)

# connecting to the server:
print 'thread 1 before conn'
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port1))
print 'thread 1 after conn'
length = int(client_socket.recv(8))

print length
print length/chunk

while index < length/1024:
    # Recieve data from the server:
    #index = index + 5
    #if index == 560:
     #   break
	data = client_socket.recv(1024)#1024
	stream.write(data, chunk)
	index = index + 1
    #print data
stream.stop_stream()
client_socket.close()
stream.close()
p.terminate()
#def messagehandler():
print 'thread 2 before conn'
client_socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket2.connect((ip, port2))
print 'thread 2 after conn'
question = client_socket2.recv(100)
print question
inp = raw_input('guess here: ')
client_socket2.send(inp)
client_socket2.close

#print 'before starting threads'
#print 'thread 1 called'
#thread1 = threading.Thread(target=streamhandler)
#print 'thread 1 called'
#thread2 = threading.Thread(target=messagehandler)
#thread1.start()
#thread1.join()
#thread2.start()
#thread2.join()

#t1 = thread.start_new_thread(streamhandler,())
#t2 = thread.start_new_thread(messagehandler,())
#t1.join()
#t2.join()

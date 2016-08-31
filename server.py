import pyaudio,socket,thread,time
from random import randint
import signal

signal.signal(signal.SIGBREAK, signal.default_int_handler)
chunk = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
host = '127.0.0.1'
#host=socket.gethostbyname(socket.gethostname())#'172.16.109.112'#socket.gethostname()
port1 = 25218
port2 =port1+1
songs = []
filename = ""



#just a function as to what to do when connection is established 
#with a client
def handleclientstream(conn,length):
	index=0
	score = 0
	conn.send(str(length))
	p = pyaudio.PyAudio()
	stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, output=True, frames_per_buffer=chunk)
	#while index < length/(512):
	conn.sendall(myfile)
		#try:
	conn.sendall(stream.read(chunk))
		#except IOError, e:
		#if e[1] == pyaudio.paInputOverflowed:
		#	print e
		#	x = '\x00' * 16 * 256 * 2  # value*format*chunk*nb_channels

	#	index = index + 1
	print 'while ends'
	stream.stop_stream()
	stream.close()
	conn.close()
	p.terminate()

	#try:
	#	stream.stop_stream()
	#	stream.close()
	#	conn.close()
	#	p.terminate()
	#except:
	#	pass

        #Sending Question after reading from file,,,,,,,
	
	print 'yoyoyoyo'
	conn2,addr=m.accept()
	print 'm accepted'

	conn2.send('Your response?')
	data = conn2.recv(1024)
	print 'recieved response from',addr
	print data
	#if not data:
		#break
	
try:
        s=socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host,port1))
        m=socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        m.bind((host,port2))

        s.listen(5)
        m.listen(5)

        print 'server listening..on ',host 





        while True:
                conn1,addr=s.accept()
                print 's accepted'
                print 'connected to',addr
	#handleclientstream(conn1,length)
	#print 'yoyoyoyo'
	#conn2,addr=m.accept()
	#print 'm accepted'
	#conn2.send('Your response?')
	#data = conn2.recv(1024)
	#print 'recieved response from',addr
	#if not data:
		#break
	
	#thread1 = threading.Thread(target=handleclientstream, args=(conn,length))
	#thread2 = threading.Thread(target=handleclientmessage, args=(conn2,addr))
	#thread1.start()
	#thread1.join()
	#thread2.start()
	#thread2.join()
                random = randint(0,4)
                filename = "filename" + str(random) + ".wav"
                myfile = open(filename, "rb").read()
                length = len(myfile)
                thread.start_new_thread(handleclientstream,(conn1,length))
	#t2 = thread.start_new_thread(handleclientmessage,(conn2,addr))
	#t1.join()
	#t2.join()
                
except KeyboardInterrupt:
        print 'hello'

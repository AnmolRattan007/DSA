
# str = '    X-DSPAM-Confidence: 0.8475'
# # startIndex = str.find('0')
# # fValue = float(str[startIndex:])
# # print(fValue)
# # sStr = str.strip()
# # print(sStr)


# fHandle = open('romeo.txt')
# garr = []
# for line in fHandle:
#     arr = line.split()
#     for val in arr:
#         if garr.__contains__(val):
#             continue
#         else:garr.append(val)
#
# print(len(garr))

# import socket
#
# mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysocket.connect(('data.pr4e.org',80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
# mysocket.send(cmd)
#
# while True:
#     data = mysocket.recv(512)
#     if(len(data)<1):
#         break
#     print(data.decode())
# mysocket.close()

import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# fhandle = urllib.request.urlopen('http://www.dr-chuck.com/')
# for line in fhandle:
#     print(line.decode().rstrip())

html = urllib.request.urlopen('http://www.dr-chuck.com/',context=ctx).read()
soup = BeautifulSoup(html,"html.parser")

tags = soup('a')
for tag in tags:
    print(tag.get('href',None))



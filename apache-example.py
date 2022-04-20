
#!/usr/bin/env python
# coding:utf-8

from urllib import response
import requests,sys,colorama
from colorama import *

banner = '''\033[1;33;40m
                                     .__          
  ____ ___  ________    _____ ______ |  |   ____  
_/ __ \\  \/  /\__  \  /     \\____ \|  | _/ __ \ 
\  ___/ >    <  / __ \|  Y Y  \  |_> >  |_\  ___/ 
 \___  >__/\_ \(____  /__|_|  /   __/|____/\___  >
     \/      \/     \/      \/|__|             \/ 
'''

def examples():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    payload = '/examples/'
    poc = urls + payload
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(poc, headers=headers, timeout=15,verify=False)
        if response.status_code == 200 and "Apache Tomcat Examples" in response.content:
            print(u'\033[1;31;40m[+]{} is apache Sample directory exists'.format(urls))
            print(response.content)
            with open('./result.txt','a') as f:
                f.write(urls)
                f.write('\n')
        else:
            print('\033[1;32;40m[-]{} None'.format(urls))
    except:
        print('{} request timeout'.format(urls))

if __name__ == '__main__':
    print(banner)
    if len(sys.argv) != 2:
        print('Example:python3 apache-example.py urls.txt')
    else:
        with open('./urls.txt','r') as u:
            line = u.readlines()
            for url in line:
                urls = url.strip()
                if urls[-1] == '/':
                    urls = urls[:-1]
                examples()
            print('over')

                


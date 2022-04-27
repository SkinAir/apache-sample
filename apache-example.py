
#!/usr/bin/env python
# coding:utf-8

from doctest import DocFileSuite
from urllib import response
import requests,sys,colorama
from colorama import *
import sys

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
    # docs = '/docs/'
    payload = ['/docs','/examples/','/docs/appdev/sample/web/WEB-INF/web.xml','/media/example/','/config.xml','/config.xml']
    try:
        requests.packages.urllib3.disable_warnings()
        for exp in payload:
            response = requests.get(urls+exp, headers=headers,timeout=15,verify=False)
            size = len(response.text)
            if response.status_code == 200 and b"Apache Tomcat" in response.content:
                print(u'\033[1;31;40m[+] Size:[{}] {} is docs exists'.format(size,urls))
                #print(response.content)
                with open('./result.txt','a') as f:
                    f.write('[+]' + '[' + str(size) + ']' + urls + 'docs exists')
                    f.write('\n')
            elif response.status_code == 200 and b"Apache Tomcat Examples" in response.content:
                print(u'\033[1;31;40m[+] Size:[{}] {} is apache Sample directory exists'.format(size,urls))
                with open('./result.txt','a') as f:
                    f.write('[+]' + '[' + str(size) + ']' + urls + 'examples exists')
                    f.write('\n')
            elif response.status_code == 200 and b"Hello, World Application" in response.content:
                print(u'\033[1;31;40m[+] Size:[{}] {} is apache WEB-INF'.format(size,urls))
                with open('./result.txt','a') as f:
                    f.write('[+]' + '[' + str(size) + ']' + urls + 'WEB-INF exists')
                    f.write('\n')
            elif response.status_code == 200 and b"jQuery" in response.content:
                print(u'\033[1;31;40m[+] Size:[{}] {} is media-example exists'.format(size,urls))
                with open('./result.txt','a') as f:
                    f.write('[+]' + '[' + str(size) + ']' + urls + 'media-example exists')
                    f.write('\n')
            elif response.status_code == 200 and b"Apache Tomcat" in response.content:
                print(u'\033[1;31;40m[+] Size:[{}] {} is apache docs exists'.format(size,urls))
                with open('./result.txt','a') as f:
                    f.write('[+]' + '[' + str(size) + ']' + urls + 'docs exists')
                    f.write('\n')
            else:
                print('\033[1;32;40m[-]{} None'.format(urls))
    # except:
    #     print('{} request timeout'.format(urls))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    try:
        print(banner)
        path=sys.argv[1]
        if len(sys.argv) != 2:
            print('Example:python3 apache-example.py urls.txt')
        else:
            with open(path,'r') as u:
                line = u.readlines()
                for url in line:
                    urls = url.strip()
                    if urls[-1] == '/':
                        urls = urls[:-1]
                    examples()
                print('over')
    except:
        print('python3 ms2.py url.txt')
        sys.exit()


                


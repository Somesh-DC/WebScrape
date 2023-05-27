from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import pandas as pd

def find_content(web_text,word_catch,file_write):
    #print(web_text)
    #print(word_catch)
    for word in word_catch:
        #print(word)
        #print('Inside for outside while',count)
        subst=web_text
        strt=subst.find(word)
        print(strt)
        while len(subst)!=0:
            if strt ==-1:
                break
            else:
                subst=subst[strt:]
                #print(subst)
                end=subst.find('\n\n\n')
                print(end)
                target_text='\n'+subst[:end:]
                print(target_text, file = file_write)
                print(target_text)
                if len(subst)<3:
                    subst=''
                else:
                    #print('Here to run another time')    
                    subst=subst[end+3:]
                    strt=subst.find(word)
                    #print(subst)

word_catc=['Note\n','Tip\n']
sourceFile = open('demo.txt', 'w')
print('Start\n', file = sourceFile)
sourceFile.close()  
#print(substring, file = sourceFile)
urls=pd.read_csv('urls.csv')
for u in urls['url']:
    print('hi',u)
    url=u
    #url='https://docs.snowflake.com/user-guide/admin-trial-account'
    page=urlopen(url)
    print(page)
    html_bytes=page.read()
    html=html_bytes.decode("utf-8")
    soup=BeautifulSoup(html,"html.parser")
    print('Title: ',soup.find('title').text)
    substring='\n\nTitle: '+soup.find('title').text
    sourceFile = open('demo.txt', 'a')
    print(sourceFile)
    print(substring, file = sourceFile)
    a=soup.get_text()
    find_content(a,word_catc,sourceFile)
    print('\nEND Of File', file = sourceFile)
    sourceFile.close()

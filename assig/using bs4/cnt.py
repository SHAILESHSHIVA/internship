import os
import time
import re
from bs4 import BeautifulSoup as b
from file import sve
from collections import Counter
import re




now = time.localtime(time.time())
d = time.strftime('%y/%m/%d',now)
t = time.strftime('%H:%M',now)
lst = []
arr = []


def cnt(path,p):
    with open (path) as f2:
        sp = b(f2,'html.parser')
        text = sp.get_text().lower()
    print 'Enter "no" to exit'
    while True:
        w = raw_input('ENTER THE WORD WANT TO SEARCH IN THE FILE\n')
        if w!='no':
            cnt = text.count(w)
            print '"%s occured %d times in the file"'%(w,cnt)
            lst.append(w)
            arr.append([w,d,t])
            continue
        else:
            print 'want to see your searches'
            res = raw_input()
            if res !='no':
                c =  Counter(lst)
                print 'Top 5 words searched by you are '
                for i,j in  c.most_common(5):
                    print '"%s"::"%d"times'%(i,j)
            hdr = ['words','date','time']
            sve(p,hdr,arr)

            break        

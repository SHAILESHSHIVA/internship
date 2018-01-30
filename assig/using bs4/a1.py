import urllib
from bs4 import BeautifulSoup  as b
from collections import Counter
import time
import os
import csv




class search(object):
    # path ='html.txt'
    # s = []
    # s2 = []
    # lst=[]
    empty= os.stat('data.csv').st_size
    now = time.localtime(time.time())
    d = time.strftime('%y/%m/%d',now)+','
    t = time.strftime('%H:%M',now)


    def __init__(self,path):
        self.path = path
        self.s2 = []
        self.s = []
        self.lst = []

    def srch(self):
        with open(self.path) as f:
            sp = b(f,'html.parser')
           
            print 'Want to see tag list'
            ans = raw_input()
            if ans !='no':
                for t in sp.find_all():
                    self.s.append(t.name)
                for i in self.s:
                    self.s2.append('  %s=>%d '%(i,self.s.count(i)))
                for i in set(self.s2):
                    print i

    def cnt(self):
        with open (self.path) as f2:
            sp = b(f2,'html.parser')
            text = sp.get_text().lower()
        
        print 'Enter "no" to exit'
        while True:
            w = raw_input('ENTER THE WORD WANT TO SEARCH IN THE FILE\n')
            if w!='no':
                cnt = text.count(w)
                print '"%s occured %d times in the file"'%(w,cnt)
                self.lst.append(w)
                continue

            else:
                print 'want to see your searches'
                res = raw_input()
                if res !='no':
                    c =  Counter(self.lst)
                    print 'Top 5 words searched by you are '
                    for i,j in  c.most_common(5):
                        print '"%s"::"%d"times'%(i,j)

                with open('data.csv','ab') as d:
                    self.header = ['words,date,time']
                    dt = csv.writer(d,delimiter=' ')
                    if self.empty ==0:
                        dt.writerow(self.header)
                    for i in self.lst:
                        dt.writerow([i+',',self.d,self.t])      
                break
        
def main():
    sr = search('html.txt')
    sr.srch()
    sr.cnt()
    
if __name__ == '__main__':main()

        
        


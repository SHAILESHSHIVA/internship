import time
from collections import Counter
from file import sve



now = time.localtime(time.time())
d = time.strftime('%y/%m/%d',now)
t = time.strftime('%H:%M',now)
lst = []
arr = []

def prsr(path,p):
        file1 = open(path).read().lower()
        s1 = file1
        while True:
            w = raw_input('Enter the word you want to search from the file:\n')
            if  w!='no':
                cnt = s1.count(w)
                print 'occurence in the file is ""%d""'%(cnt)
                lst.append(w)
                arr.append([w,d,t])
                continue
            else:
                print '-' *60
                print '++++  want to see and save  your searches +++++ Say ""'
                res = raw_input()
                if res =='yes' or 'y':
                    print '*' *50
                    c =  Counter(lst)
                    print 'Top 5 words searched by you are '
                    for i,j in c.most_common(5):
                        print 'searched "%s" ==>"%d"times'%(i,j)

                hdr = ['words','date','time']
                sve(p,hdr,arr)
            break   
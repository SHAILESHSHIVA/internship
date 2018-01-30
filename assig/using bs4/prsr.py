from bs4 import BeautifulSoup as b



s2 = []
s = []

def prsr(path):
    with open(path) as f:
        sp = b(f,'html.parser')
        print 'Want to see tag list'
        ans = raw_input()
        if ans !='no':
            for t in sp.find_all():
                s.append(t.name)
            for i in s:
                s2.append('  %s=>%d '%(i,s.count(i)))
            for i in set(s2):
                print i
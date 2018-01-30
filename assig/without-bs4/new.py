import urllib


content= urllib.urlopen('https://stackoverflow.com/questions/45635592/typeerror-coercing-to-unicode-need-string-or-buffer-sre-sre-pattern-found?rq=1')
htmlSrc = content.read()


file2 = open('f2.txt','w')
file2.write(htmlSrc)
file2.close() 


file2 = open('f2.txt').read().lower()
s2 = file2
print s2
import urllib

from collections import Counter

#OPEN FILE THROUGH URLLIB MODULE AND STORING IN HTMLSrc variable

# content= urllib.urlopen('https://docs.python.org/2/index.html')
# htmlSrc = content.read()
# # #


# file1 = open('ext.txt','w')
# file1.write(htmlSrc)
# file1.close() 

#+++++++++++++++++++++++++++++Start from here+++++++++++++++++++++++++++++++++++++


file1 = open('ext.txt').read().lower()
s1 = file1

##CREATING TAGS LIST IN THIS SESSION  
    
l = ['<strong','<table','<form','<span','<h1','<span','<script','<li','<div','<html','<a','<h3','<link','<h2','<body','<p','<meta','<title','<td','<tr']
    # if len(l)<0:
    #     break
print 'tags counts are given below from file'    
while len(l)>-1:
    try:
        if len(l)>=0:
            s2 = l.pop()
            c = s1.count(s2)
            print '{0} : {1}'.format(s2.strip('<'),c)


            continue
      
    except IndexError as e:
         e
         print '#'*60
         break

#taking input and searching for the respective word

lst = []

while True:
    
    w = raw_input('Enter the word you want to search from the file:\n')
    if  w!='no':
        cnt =  s1.count(w)
        print 'occurence in the file is ""%d""'%(cnt)
        lst.append(w)
        continue
    
        
    else:
        print '#' *60
        print "You entered NO"
        print 'want to see your searches'
        res = raw_input()
  
        if res =='yes' or 'y':
            print '*' *50
            c =  Counter(lst)
            print 'Top 5 words searched by you are '
            for i,j in  c.most_common(5):
                print 'searched "%s" ==>"%d"times'%(i,j)
        print 'GOODBYE'
        break  

 

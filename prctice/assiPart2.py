import csv
import time
import os
from collections import Counter

file1 = open('ext.txt').read().lower()
s1 = file1

now = time.localtime(time.time())
r = time.strftime('%y/%d/%m'+','+'%H:%M',now)
lst = []
path = 'ext.csv'
fileEmpty = os.stat(path).st_size






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
       
         break

#taking input and searching for the respective word


print '---------PRESS "no" to Exit------------------ '

while True:
    
    w = raw_input('Enter the word you want to search from the file:\n')
   
   
    if  w!='no':
        w = w
        cnt =  s1.count(w)

        print 'occurence in the file is ""%d""'%(cnt)
        w = w +','+r
        lst.append([w,r])
        continue
    
        
    else:
        print '#' *60
      
        print '++++  want to see and save  your searches +++++ Say ""'
        res = raw_input()
       
        if res =='yes' or 'y':
            print '*' *50
            c =  Counter(lst)
            print 'Top 5 words searched by you are '
            for i,j in  c.most_common(5):
                print 'searched "%s" ==>"%d"times'%(i,j)


        with open(path,'ab') as file1:
              header = ['words,date,time']
              writer = csv.writer(file1,delimiter=' ')
              if fileEmpty == 0:
                writer.writerow(header)
              for row in lst:
                # r =[row]
                # writer.writerow(r)  
                writer.writerow([row])

              print 'stored in "ext.csv" file'
              print 'GOODBYE' 
        
        break 










































































# while True:
    
#     w = raw_input('Enter the word you want to search from the file:\n')
   
   
#     if  w!='no':
#         w = w
#         cnt =  s1.count(w)
#         print 'occurence in the file is ""%d""'%(cnt)
#         w = w +','+r
#         lst.append(w)
#         continue
    
        
#     else:
        
      
#         print '++++  want to see and save  your searches +++++ Say "y"'
#         res = raw_input()
       
#         if res =='yes' or 'y':
#             print '*' *50
#             c =  Counter(lst)
#             print 'Top 5 words searched by you are '
#             for i,j in  c.most_common(5):
#                 print 'searched "%s" ==>"%d"times'%(i,j)
        

#        ##storing in csv file
#         with open(path,'ab') as file:
#             wri = csv.writer(file,delimiter=' ')
#             wri.writerow(['WORDS,DATE,TIME'])

#             for lines in lst:
#                 wri.writerow(lines)
#             print 'stored in "ext.csv" file'
#             print 'GOODBYE' 
        
#         break 
       
#         with open(path,'ab') as file:
#             wri = csv.writer(file,delimiter=' ')
#             wri.writerow(header)

#             for lines in lst:
#                 wri.writerow(lines)
#             print 'stored in "ext.csv" file' 
    
#         break  
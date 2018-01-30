import csv
import time
from collections import Counter
import os.path

file1 = open('ext.txt').read().lower()
s1 = file1

now = time.localtime(time.time())
r = time.strftime('%y/%d/%m',now)+','
t = time.strftime('%H:%M',now)


lst = []
fileEmpty = os.stat('ext.csv').st_size
print fileEmpty


print '---------PRESS "no" to Exit------------------ '

while True:
    
    w = raw_input('Enter the word you want to search from the file:\n')
   
   
    if  w!='no':
        cnt =  s1.count(w)
        print 'occurence in the file is ""%d""'%(cnt)
        lst.append(w)
        print lst
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


        with open('ext.csv','ab') as file1:
              h = ['words,date,time']
              writer = csv.writer(file1,delimiter=' ')
              if fileEmpty == 0:
                writer.writerow(h)
              for i in lst:
                writer.writerow([i+',',r,t])        
              print 'stored in "ext.csv" file'
              print 'GOODBYE' 
        
        break

                #      reader = csv.reader(file1,delimiter=' ')
#         #      row= 0
#         #      for row in reader:
#         #         if row>=1:
#         #             lst.append[0][]
#         #             lst.append[1]
#         #             lst.append[2]

#         #         row = row+1
  


    


# # def scv(data,path):
# #     with open(path,'wb') as file:
# #         wri = csv.writer(file,delimiter=' ',quotechar='|')
# #         for lines in data:
# #             wri.writerow(lines)


# def rd(path):
   
#     with open(path,'rb') as f:
#          rd = csv.reader(f,delimiter=' ',quotechar='|')
#          for row in rd:
#              print ','.join(row )            

# if __name__ == '__main__':
   
#     # data = ,'paaja,amd,'.split(','),
#     #          'shaaz,surat,987897'.split(' ')]
#     path = 'ext.csv'
#     # scv(data,path)
#     rd(path)

  #names = []
# jobs = []
 
# # open file
# with open('persons.csv', 'rb') as f:
#     reader = csv.reader(f)
 
#     # read file row by row
#     rowNr = 0
#     for row in reader:
#         # Skip the header row.
#         if rowNr >= 1:
#             names.append(row[0])
#             jobs.append(row[1])
 
#         # Increase the row number
#         rowNr = rowNr + 1
 
# # Print data 
# print names
# print jobs
#         words = []
#         date = []
#         time = []




# import random
# import csv
# import time

# h = ['date','value']
# v = random.randint(0,100)
# with open('ext.csv','ab') as out:
#     file1 = csv.DictWriter(out,fieldnames = h)
#     out.seek(0,2)

#     if out.tell() ==0:
#         file1.writeheader()
#     out.writerow({'date':strftime('%y/%d',gmtime()),'value':v})


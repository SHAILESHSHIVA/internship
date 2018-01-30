from file import sve
from cnt import cnt
from prsr import prsr


class search(object):
    def __init__(self,path):
        self.path = path

    def tagsCount(self):
        cnt(self.path)



    def searchWords(self,p):
        prsr(self.path,p)

        
def main():
    s = search(raw_input('enter file path\n'))
    s.tagsCount()
    s.searchWords(raw_input('enter the csv file name\n'))




if __name__ == '__main__':main()
 






































































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
import urllib
from prsr import prsr
from cnt import cnt




class MiniSearch(object):
  
    def __init__(self,path):
        self.path = path
      

    def searchTag(self):
        prsr(self.path)

      

    def wordCount(self,p):
        cnt(self.path,p)
        
   
if __name__ == '__main__':
    sr = MiniSearch(raw_input('enter the file path\n')) 
    sr.searchTag()
    print '-'*50
    p = raw_input('csv file path\n')
    sr.wordCount(p)











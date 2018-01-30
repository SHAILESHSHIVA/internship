import csv
import os

def sve(path,h,arr):
    empty =os.stat(path).st_size
    with open(path,'ab') as f:
        out= csv.writer(f,delimiter=',')
        if empty ==0:
            out.writerow(h)
        out.writerows(arr)
        print 'saved in csv file'
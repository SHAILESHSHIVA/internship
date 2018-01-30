

def cnt(path):
    print 'do you want to see tag list'
    res = raw_input()
    if res !='no':
        file1 = open(path).read().lower()
        s1 = file1
        l = ['<strong','<table','<form','<span','<h1','<span','<script','<li','<div','<html','<a','<h3','<link','<h2','<body','<p','<meta','<title','<td','<tr']
        print 'tags counts are given below from file'    
        while len(l)>-1:
            try:
                if len(l)>=0:
                    s2 = l.pop()
                    c = s1.count(s2)
                    print ' {0} : {1} '.format(s2.strip('<'),c)
                    continue
            except IndexError as e:
                e
                break
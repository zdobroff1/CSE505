# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 21:02:01 2018

@author: Zach
"""
def manage():
    try:
        #f = open('C:/Users/Zach/Documents/CSE 505/clingo-5.3.0-win64/asprilo-master/instances/abc/structured/1x2x4/25sc/1-1.lp', 'r+')
        f = open('examples/1-1.lp', 'r+')
    except OSError:    
        print OSError
    robotCount = 0
    totalOrder = 0
    orderWords=['order', 'line']
    s= ""
    for line in f:
        #print line       
        if 'robot' in line:
            robotCount += 1
    f.close()
    try:
        #f2_read = open('C:/Users/Zach/Documents/CSE 505/clingo-5.3.0-win64/asprilo-master/instances/abc/structured/1x2x4/25sc/1-1.txt', 'r')
        f2_read = open('examples/1-1.txt', 'r')
    except OSError:    
        print OSError
    for linef2 in f2_read:
        totalOrder += 1
    if robotCount > 0:
        #print robotCount
        i=0
        lowOrder = 0
        highOrder = robotCount
        while totalOrder > 0:
            try:
                #f2 = open('C:/Users/Zach/Documents/CSE 505/clingo-5.3.0-win64/asprilo-master/instances/abc/structured/1x2x4/25sc/1-1.txt', 'r')
                f2 = open('examples/1-1.txt', 'r')
            except OSError:    
                print OSError
            try:
                #f_read = open('C:/Users/Zach/Documents/CSE 505/clingo-5.3.0-win64/asprilo-master/instances/abc/structured/1x2x4/25sc/1-1.lp', 'r+')                
                f_read = open('examples/1-1.lp', 'r+')
            except OSError:    
                print OSError            
            for line_read in f_read:
                if all(x in line_read for x in orderWords):
                    pass
                else:
                    s += line_read
            f_read.close()        
            try:
                #f_write = open('C:/Users/Zach/Documents/CSE 505/clingo-5.3.0-win64/asprilo-master/instances/abc/structured/1x2x4/25sc/1-1.lp', 'w')                
                f_write = open('examples/1-1.lp', 'w')
            except OSError:    
                print OSError
            f_write.write(s)
            s=""
            f_write.close()
            try:
                #f_append = open('C:/Users/Zach/Documents/CSE 505/clingo-5.3.0-win64/asprilo-master/instances/abc/structured/1x2x4/25sc/1-1.lp', 'a')                    
                f_append = open('examples/1-1.lp', 'a')    
            except OSError:    
                print OSError
            for i, line2 in enumerate(f2):
                #print "i :", i
                #print "lowOrder :", lowOrder
                #print "highOrder :", highOrder
                if i >= lowOrder and i < highOrder:
                    f_append.write(line2)
            f_append.close()
            lowOrder += robotCount
            highOrder += robotCount
            totalOrder -= robotCount

            #print "lowOrder :", lowOrder
            #print "highOrder :", highOrder
            #print "totalOrder :", totalOrder
if __name__ == '__main__':
    manage()

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 15:55:11 2018

@author: Zach
"""

import re

def update_adj():       
    fname = 'examples/1-2.lp'
    try:    
        f = open(fname, 'r+')    
    except OSError:    
        print OSError
    maxRow = 0
    maxCol = 0
    #s=''
    for line in f:
        #s+=line
        if 'node' in line:
            nums = re.findall('\d+',line)
            if nums[1] > int(maxCol):
                maxCol = nums[1]
            if nums[2] > int(maxRow):
                maxRow = nums[2]
    f.close()
    try:    
        f = open(fname, 'r+')    
    except OSError:    
        print OSError
    stationIDs = []
    deliverToStations = []
    productIDs = []
    shelfIDs = []
    #shelfLocations = []
    toAbove = []
    toBelow = []
    toRight = []
    toLeft = []
    #print s
    for line2 in f:
        #print line2
        if 'pickingStation' in line2 and 'at,(1,' in line2 and 'order' not in line2:
            #station in leftmost col
            stationID = re.findall('\d+',line2)
            stationIDs.append(stationID[0] + "l")
        elif 'pickingStation' in line2 and 'at(' + maxCol + ',' in line2 and 'order' not in line2:
            #station in rightmost col
            stationID = re.findall('\d+',line2)
            stationIDs.append(stationID[0] + "r")
        elif 'pickingStation' in line2 and ',1))' in line2 and 'order' not in line2:
            #pass #station in top row
            stationID = re.findall('\d+',line2)
            stationIDs.append(stationID[0] + "a")
        elif 'pickingStation' in line2 and ',' + maxRow + '))' in line2 and 'order' not in line2:
            #pass # station in bottow row
            stationID = re.findall('\d+',line2)
            stationIDs.append(stationID[0] + "b")
    f.close()
    #print 'stationIDs: ', stationIDs
    try:    
        f = open(fname, 'r+')    
    except OSError:    
        print OSError
    for line3 in f:
        if 'order' in line3 and 'pickingStation' in line3:
            deliverToStation = re.findall('\d+',line3)
            #print deliverToStation[1]
            #deliverToStations.append(deliverToStation[1])
            if deliverToStation[1] + "l" in stationIDs:
                deliverToStations.append(deliverToStation[0] + "l")
            elif deliverToStation[1] + "r" in stationIDs:
                deliverToStations.append(deliverToStation[0] + "r")
            elif deliverToStation[1] + "a" in stationIDs:
                deliverToStations.append(deliverToStation[0] + "a")
            elif deliverToStation[1] + "b" in stationIDs:
                deliverToStations.append(deliverToStation[0] + "b")
    #deliverToBorder = [s in stationIDs for s in deliverToStations]
    #print deliverToBorder
    f.close()
    #print 'deliverToStations: ', deliverToStations

    try:    
        f = open(fname, 'r+')    
    except OSError:    
        print OSError
    for line4 in f:
        if 'line' in line4 and 'order' in line4:
            productID = re.findall('\d+',line4)
            if productID[0] + "l" in deliverToStations:
                productIDs.append(productID[1] + "l")
            elif productID[0] + "r" in deliverToStations:
                productIDs.append(productID[1] + "r")                
            elif productID[0] + "a" in deliverToStations:
                productIDs.append(productID[1] + "a")    
            elif productID[0] + "b" in deliverToStations:
                productIDs.append(productID[1] + "b")                    
    f.close()
    #print 'productIDs: ', productIDs

    try:    
        f = open(fname, 'r+')    
    except OSError:    
        print OSError
    for line5 in f:
        if 'product' in line5 and 'on' in line5:
            shelfID = re.findall('\d+',line5)
            if shelfID[0] + "l" in productIDs:
                shelfIDs.append(shelfID[1] + "l")
            elif shelfID[0] + "r" in productIDs:
                shelfIDs.append(shelfID[1] + "r")
            elif shelfID[0] + "a" in productIDs:
                shelfIDs.append(shelfID[1] + "a")
            elif shelfID[0] + "b" in productIDs:
                shelfIDs.append(shelfID[1] + "b")
    f.close()
    #print 'shelfIDs: ', shelfIDs
   
    try:    
        f = open(fname, 'r+')    
    except OSError:    
        print OSError
    ##COPY SHELF TO 4 directions    
    for line6 in f:
        if 'shelf' in line6 and 'at' in line6:
            shelfLocation = re.findall('\d+',line6)
            if shelfLocation[0] + "l" in shelfIDs:
                #shelfLocations.append(line6 + "l")
                toLeft.append(line6)
            elif shelfLocation[0] + "r" in shelfIDs:
                #shelfLocations.append(line6 + "r")
                toRight.append(line6)
            elif shelfLocation[0] + "a" in shelfIDs:
                #shelfLocations.append(line6 + "a")
                toAbove.append(line6)
            elif shelfLocation[0] + "b" in shelfIDs:
                #shelfLocations.append(line6 + "b")
                toBelow.append(line6)
    f.close()
    fname_num = re.findall('\d+',fname)
    #1-1 for bottom left
    #1-2 for one space right
    #2-1 for one space above
    #0-1 for one space below
    #1-0 for one space left
    placeRow = fname_num[-1]
    placeCol = fname_num[-2]
    placeColp = int(placeCol) + 1
    placeRowp = int(placeRow) + 1
    placeColm = int(placeCol) - 1
    placeRowm = int(placeRow) - 1
    fnameAbove = fname[:9] + str(placeColp) + '-' + str(placeRow) + '.lp'
    fnameBelow = fname[:9] + str(placeColm) + '-' + str(placeRow) + '.lp'
    fnameRight = fname[:9] + str(placeCol) + '-' + str(placeRowp) + '.lp'
    fnameLeft  = fname[:9] + str(placeCol) + '-' + str(placeRowm) + '.lp'
    if len(toAbove) > 0:
        try: 
            f_a = open(fnameAbove, 'r')
        except OSError:    
            print OSError
        maxCol_a = 0
        maxRow_a = 0
        maxShelf_a = 0
        for line_a in f_a:
            if 'node' in line_a:
                nums_a = re.findall('\d+',line_a)
                if nums_a[1] > int(maxCol_a):
                    maxCol_a = nums_a[1]
                if nums_a[2] > int(maxRow_a):
                    maxRow_a = nums_a[2]
            if 'shelf' in line_a:
                shelfnums_a = re.findall('\d+',line_a)
                if shelfnums_a[0] > int(maxShelf_a):
                    maxShelf_a = shelfnums_a[0]
        maxShelf_a = int(maxShelf_a) + 1
        f_a.close()
        try:
            f_a = open(fnameAbove, 'a+')
        except OSError:    
            print OSError
        for line2_a in f_a:
            if 'pickingStation' in line2_a and ',' + maxRow_a + '))' in line2_a and 'order' not in line2_a:
                shelfnums_a2 = re.findall('\d+',line2_a)
                f_a.write("\ninit(object(shelf," + str(maxShelf_a) + "),value(at,(" + str(shelfnums_a2[1]) + "," + str(shelfnums_a2[2]) + "))).")
        f_a.close()
    if len(toBelow) > 0:
        try: 
            f_b = open(fnameBelow, 'r')
        except OSError:    
            print OSError
        maxCol_b = 0
        maxRow_b = 0
        maxShelf_b = 0
        for line_b in f_b:
            if 'node' in line_b:
                nums_b = re.findall('\d+',line_b)
                if nums_b[1] > int(maxCol_b):
                    maxCol_b = nums_b[1]
                if nums_b[2] > int(maxRow_b):
                    maxRow_b = nums_b[2]
            if 'shelf' in line_b:
                shelfnums_b = re.findall('d+',line_b)
                if shelfnums_b[0] > int(maxShelf_b):
                    maxShelf_b = shelfnums_b[0]
        maxShelf_b = int(maxShelf_b) + 1                    
        f_b.close()
        try:
            f_b = open(fnameBelow, 'a+')
        except OSError:    
            print OSError
        for line2_b in f_b:
            if 'pickingStation' in line2_b and ',1))' in line2_b and 'order' not in line2_b:
                shelfnums_b2 = re.findall('d+',line2_b)
                f_b.write("\ninit(object(shelf," + str(maxShelf_b) + "),value(at,(" + str(shelfnums_b2[1]) + "," + str(shelfnums_b2[2]) + "))).")
        f_b.close()

    if len(toRight) > 0:
        try: 
            f_r = open(fnameRight, 'r')
        except OSError:    
            print OSError
        maxCol_r = 0
        maxRow_r = 0
        maxShelf_r = 0
        for line_r in f_r:
            if 'node' in line_r:
                nums_r = re.findall('d+',line_r)
                if nums_r[1] > int(maxCol_r):
                    maxCol_r = nums_r[1]
                if nums_r[2] > int(maxRow_r):
                    maxRow_r = nums_r[2]
            if 'shelf' in line_r:
                shelfnums_r = re.findall('d+',line_r)
                if shelfnums_r[0] > int(maxShelf_r):
                    maxShelf_r = shelfnums_r[0]
        maxShelf_r = int(maxShelf_r) + 1                    
        f_r.close()
        try:
            f_r = open(fnameRight, 'a+')
        except OSError:    
            print OSError
        for line2_r in f_r:
            if 'pickingStation' in line2_a and 'at(' + maxCol_r + ',' in line2_r and 'order' not in line2_r:
                shelfnums_r2 = re.findall('\d+',line2_r)
                f_r.write("\ninit(object(shelf," + str(maxShelf_r) + "),value(at,(" + str(shelfnums_r2[1]) + "," + str(shelfnums_r2[2]) + "))).")
        f_r.close()
    
    if len(toLeft) > 0:
        try: 
            f_l = open(fnameLeft, 'r')
        except OSError:    
            print OSError
        maxCol_l = 0
        maxRow_l = 0
        maxShelf_l = 0
        for line_l in f_l:
            if 'node' in line_l:
                nums_l = re.findall('d+',line_l)
                if nums_l[1] > int(maxCol_l):
                    maxCol_l = nums_l[1]
                if nums_l[2] > int(maxRow_l):
                    maxRow_l = nums_l[2]
            if 'shelf' in line_l:
                shelfnums_l = re.findall('\d+',line_l)
                if shelfnums_l[0] > int(maxShelf_l):
                    maxShelf_l = shelfnums_l[0]
        maxShelf_l = int(maxShelf_l) + 1                    
        f_l.close()
        try:
            f_l = open(fnameLeft, 'a+')
        except OSError:    
            print OSError
        for line2_l in f_l:
            if 'pickingStation' in line2_l and 'at,(1,' in line2_l and 'order' not in line2_l:
                shelfnums_l2 = re.findall('d+',line2_l)
                f_l.write("\ninit(object(shelf," + str(maxShelf_l) + "),value(at,(" + str(shelfnums_l2[1]) + "," + str(shelfnums_l2[2]) + "))).")
        f_l.close()

#####  
    try:    
        f = open(fname, 'r+')    
    except OSError:    
        print OSError
    lines = f.readlines()  
    f.close()
    try:    
        f = open(fname, 'w')    
    except OSError:    
        print OSError
    for line_write in lines:
        if (len(toAbove) > 0 and line_write != toAbove[0]) or (len(toBelow) > 0 and line_write != toBelow[0]) \
            or (len(toRight) > 0 and line_write != toRight[0]) or (len(toLeft) > 0 and line_write != toLeft[0]):
            f.write(line_write)
        else:
            pass
                
    #print maxRow,maxCol
    f.close()
if __name__ == '__main__':
    update_adj()

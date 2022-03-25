#import util, layout
import sys, types, time, random, os
from datetime import timezone
import hashlib
import json
import os
import os.path
from pickletools import float8
import struct
from time import time
from sys import argv
from datetime import timezone
import datetime
from tokenize import Double
from contextlib import suppress

"""
Add a new evidence item to the blockchain and associate it
with the given case identifier. For users’ convenience, more
than one item_id may be given at a time, which will create a blockchain
entry for each item without the need to enter the case_id multiple times.
The state of a newly added item is CHECKEDIN. The given evidence
ID must be unique (i.e., not already used in the blockchain) to be accepted.
"""
def addItem():

    cItem = None #case id
    #iItem = None #item
    itemList = [] #list of items

    try:
        """get case id and parameters of items"""
        if sys.argv[2] == "-c" and sys.argv[4] == "-i":
            #print("-c", sys.argv[3], " -i")
            if sys.argv[6]:
                """list through -i items"""
                for item in sys.argv[5:]:
                    print("item",item)
                    itemList.append(item)
                    #ADD code HERE
        else:
            raise IndexError("not enough or too many arguments/parameters")
        print("add item")
    except IndexError:
        print("index error (addItem)")

    return 0


"""
Add a new checkout entry to the chain of custody for
the given evidence item. Checkout actions may only be
performed on evidence items that have already been added to the blockchain.
"""
def checkout():
    
    iItem = None
    
    try:
        """get parameter of item"""
        if sys.argv[2] == "-i":
            iItem = sys.argv[3]
            print("item",iItem)
            #ADD code HERE
        print("checkout")
    except IndexError:
        print("index error (checkout)")

    return 0

"""
Add a new checkin entry to the chain of custody for the given evidence item.
Checkin actions may only be performed on evidence items that have already
been added to the blockchain.
"""
def checkin():

    iItem = None
    
    try:
        """get parameter of item"""
        if sys.argv[2] == "-i":
            iItem = sys.argv[3]
            print("item",iItem)
            #ADD code HERE
        print("checkin")
    except IndexError:
        print("index error (checkin)")

    return 0

"""
Display the blockchain entries giving the oldest
first (unless -r is given).
"""
def log():
    
    rIndex = 0
    nIndex = 0
    cIndex = 0
    iIndex = 0   
    
    rItem = None
    nItem = None
    cItem = None
    iItem = None
       
    with suppress(ValueError):
        rIndex = sys.argv.index("-r")
        
    with suppress(ValueError):
        nIndex = sys.argv.index("-n")
        
    with suppress(ValueError):
        cIndex = sys.argv.index("-c")
        
    with suppress(ValueError):
        iIndex = sys.argv.index("-i")
    
    try:
        """check if -r is present"""
        if rIndex > 0:
            rItem = sys.argv[rIndex+1]
            #ADD code HERE (reverse order)
            print("")
            
        if nIndex > 0:
            nItem = sys.argv[nIndex+1]
            #ADD code HERE (reverse order)
            print("")
            
        if cIndex > 0:
            cItem = sys.argv[cIndex+1]
            #ADD code HERE (reverse order)
            print("")

        if iIndex > 0:
            iItem = sys.argv[iIndex+1]
            #ADD code HERE (reverse order)
            print("")
        
        print("log")
    except IndexError:
        print("index error ( log() )")

    #ADD code HERE


    return 0 

"""
Prevents any further action from being taken on the evidence 
item specified. The specified item must have a state of CHECKEDIN 
for the action to succeed.
"""
def remove():
    iItem = None #item
    yItem = None #reason
    oItem = None #owner

    try:
        """get parameter of item"""
        if sys.argv[2] == "-i":
            iItem = sys.argv[3]
            print("item",iItem)
            #ADD code HERE
            
        if sys.argv[4] == "-y":
            yItem = sys.argv[5]
            print("item",yItem)
            #ADD code HERE
            
        if len(sys.argv) > 6:
            if sys.argv[6] == "-o":
                oItem = sys.argv[7]
                print("item",yItem)
                #ADD code HERE
        print("remove")
    except IndexError:
        print("index error (remove)")    


    rIndex = 0
    nIndex = 0
    cIndex = 0
    iIndex = 0    
    
    rItem = None
    nItem = None
    cItem = None
    iItem = None
    
    rIndex = sys.argv.index("-r") > 0 if sys.argv.index("-r") > 0 else 0
    nIndex = sys.argv.index("-n") > 0 if sys.argv.index("-n") > 0 else 0
    cIndex = sys.argv.index("-c") > 0 if sys.argv.index("-c") > 0 else 0
    iIndex = sys.argv.index("-i") > 0 if sys.argv.index("-i") > 0 else 0
    
        
    try:
        """check if -r is present"""
        if rIndex > 0:
            rItem = sys.argv[rIndex+1]
            #ADD code HERE (reverse order)
            print("")
            
        if nIndex > 0:
            nItem = sys.argv[nIndex+1]
            #ADD code HERE (reverse order)
            print("")
            
        if cIndex > 0:
            cItem = sys.argv[cIndex+1]
            #ADD code HERE (reverse order)
            print("")

        if iIndex > 0:
            iItem = sys.argv[iIndex+1]
            #ADD code HERE (reverse order)
            print("")
        
        print("remove")
    except IndexError:
        print("index error ( log() )")

    #ADD code HERE


    return 0 


"""
Sanity check. Only starts up and checks for the initial block.
"""
def init():

    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "/BCHOC_FILE_PATH"
    abs_file_path = os.path.join(script_dir, rel_path)  
    

    exists = os.path.isfile(abs_file_path)
   
    if exists:

        blockchain = open(abs_file_path, "rb")

    else:

        print("no existing chain found, creating genesis block and initializing chain")
        
  
        # Getting the current date
        # and time
        dt = datetime.datetime.now(timezone.utc)
        utc_time = dt.replace(tzinfo=timezone.utc)
        utc_timestamp = utc_time.timestamp()
        print("timestamp currently is: " + utc_timestamp)
        
        
        
        Previous_Hash= None
        Timestamp= float(utc_timestamp)
        Case_ID= None
        Evidence_Item_ID= None
        State = "INITIAL"
        Data_Length = 14 
        Data = "Initial Block"

        block = struct.pack("20s d 16s I 11s I",Previous_Hash,Timestamp,Case_ID,Evidence_Item_ID,State,Data_Length,Data)

        with open(abs_file_path,'w') as f:
            f.write(block)




    return 0

"""
Parse the blockchain and validate all entries.
"""
def verify():
   return 0


#Main
if __name__ == '__main__':
    print("test")
    if sys.argv[1] == 'add':
        addItem()

    elif sys.argv[1] == 'checkout':
        checkout()

    elif sys.argv[1] == 'checkin':
        checkin()

    elif sys.argv[1] == 'log':
        log()

    elif sys.argv[1] == 'remove':
        remove()

    elif sys.argv[1] == 'init':
        init()

    elif sys.argv[1] == 'verify':
        verify()

"""
You can test a method call by:
 python3 bchoc add
It should return:
 test
 add item
"""

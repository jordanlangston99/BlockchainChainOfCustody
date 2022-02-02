#import util, layout
import sys, types, time, random, os

def addItem():
   return 0

def checkout():
   return 0

def checkin():
   return 0

def log():
   return 0

def remove():
   return 0

def init():
   return 0

def verify():
   return 0


#Main
if __name__ == '__main__':
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
    

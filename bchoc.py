#! /usr/bin/Python3

import util, layout
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
    else if sys.argv[1] == 'checkout'
        return checkout()
    else if sys.argv[1] == 'checkin'
        return checkin()
    else if sys.argv[1] == 'log'
        return log()
    else if sys.argv[1] == 'remove'
        return remove()
    else if sys.argv[1] == 'init'
        return init()
    else if sys.argv[1] == 'verify'
        return verify()
    return 0

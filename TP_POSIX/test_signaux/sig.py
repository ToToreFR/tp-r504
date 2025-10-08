#!/usr/bin/python3
import signal as sig
from time import sleep
import sys
import os

x=1

def signal_handler(s, frame):
       print( "réception du signal ", sig.Signals(s).name )
       exit(1)

def signal_handler_2(s, frame):
       print( "réception du signal ", sig.Signals(s).name )


sig.signal(sig.SIGINT, signal_handler)
sig.signal(sig.SIGQUIT, signal_handler_2)


while True:
        print("pid=", os.getpid(), x)
        sleep(.5)
        x += 1

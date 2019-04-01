#!/usr/bin/python
from threading import Timer
from  subprocess import call
import sys
import time
import copy
import os

class Bakup_Dir(object):
    def __init__(self, wait=1, dir1="./file", dir2="./file_bak_cla"):
        self.wait = wait
        self.dir1 = dir1
        self.dir2 = dir2
    
    def action(self):
        call("rsync -av --delete %s/ %s" % (self.dir1, self.dir2), shell=True)
    
    def eventHandler(self):
        if os.listdir(self.dir1) != os.listdir(self.dir2):
            print(os.listdir(self.dir1))
            t = Timer((self.wait), self.action)
            t.start()
            print("Event ok!!!")
        else:
            print("No Event!!!")
    
    def run(self):
        try:
            while True:
                self.eventHandler()
                time.sleep(3)
        except Exception as err:
            print("Error is : %s" % err)
        finally:
            sys.exit(0)

bd = Bakup_Dir()
bd.run()

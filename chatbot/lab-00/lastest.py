#!/usr/bin/env python
# -*- coding: utf-8 -*-

import aiml
import commands
import sys
import time 
import commands
from os import system
import marshal # sesje 
import os.path
 
 
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    BLACK = '\033[36m'
    RED =  '\033[31m'
    GREEN =  '\033[32m'
    BLUE =  '\033[34m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
 
    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.BLACK=''
        self.RED=''
        self.FAIL = ''
        self.ENDC = ''
 
k = aiml.Kernel()
czerep="czerep.br"
 
# read dictionary and create brain in file czerep.brp
 
if os.path.isfile(czerep):
    k.bootstrap(brainFile = czerep)
else:
    homedir=os.getcwd()
    #Change to the directory whe    re the AIML files are located
    os.chdir('./dic') # going to dictionary
    list=os.listdir('./');
    for item in list: #load dictionary one by one 
        k.learn(item)
       
     
    #k.setPredicate("master","ravi")
     
    #Change back to homedir to save the brain for subsequent loads
    os.chdir(homedir)
    k.saveBrain(czerep) # save new brain
# name of bot
k.setBotPredicate('name', "Hal 9000")
os.system('fortune | cowsay -f $(ls /usr/share/cowsay/cows/ | shuf -n1)')# welcome cowsay is not importan you can del this
while True:
    input = raw_input("[YOU     ]" )
  
# close bot if you use onely spell quit
    if input == "quit":
        sys.exit(0)
# end of new code
  
    response = k.respond(input)
    # print out on the shell
     
    print bcolors.BLACK+"[          ]"+bcolors.WARNING+response+bcolors.ENDC
    

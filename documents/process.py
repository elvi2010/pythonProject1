import os
import subprocess
import multiprocessing as mp
import time


def start():
 print("start!")
 print(os.getpid())
 process = mp.Process(target=welcome("welcome!"), args=())
 print(os.getpid())
 process.join()
 print(process.name)
 process.kill()
 print(process.is_alive())



def Welcome(message):
     print("message!")

def work():
 print("work!")

def finishing():
     print("finishing!")
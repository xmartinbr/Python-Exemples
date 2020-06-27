from threading import Thread
import time

class myHilo(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        
    def run(self):
        print ("() inicio {0}".format(self.getName()))
        time.sleep(1)
        print ("() terminado {0}".format(self.getName()))

if __name__ == "__main__":
    for x in range(4):
        hilo = myHilo(name="Thread-({0})".format(x+1))
        hilo.start()
        time.sleep(.5)

'''
import threading
import time

class myHilo(threading.Thread):
    
    def run(self):
        print ("() inicio {0}".format(self.getName()))
        time.sleep(1)
        print ("() terminado {0}".format(self.getName()))

if __name__ == "__main__":
    for x in range(4):
        hilo = myHilo(name="Thread-({0})".format(x+1))
        hilo.start()
        time.sleep(.5)
'''        



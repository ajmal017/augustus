import datetime
import numpy as np 
import pandas as pd 
import pytz
from queue import Queue,Empty

class EventEngine(object):
    def __init__(self):
        self.__queue=Queue()
        self.__isactive=False


    def __run(self):
        while self.__isactive==True:
            try:
                event=self.__queue.get(block=True,timeout=1)
            except Empty:
                pass

    def __process(self):
        pass

    def __begin(self):
        pass

    def __end(self):
        pass
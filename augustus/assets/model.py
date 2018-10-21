import math
import datetime

class Model(object):
    def __init__(self,date,open,close,high,low,volume,code):
        self.date=date
        self.open=open  
        self.close=close
        self.high=high
        self.low=low 
        self.volume=volume
        self.code=code

    def get_date(self):
        return self.date

    def get_open(self):
        return self.open 
    
    def get_close(self):
        return self.close 

    def get_high(self):
        return self.high

    def get_low(self):
        return self.low

    def get_volume(self):
        return self.volume

    def get_code(self):
        return self.code
        


import math
import datetime

class Model(object):
    def __init__(self,date,openingPrice,closingPrice,highest,lowest,volume,code):
        self.date=date
        self.openingPrice=openingPrice  
        self.closingPrice=closingPrice
        self.highest=highest
        self.lowest=lowest
        self.volume=volume
        self.code=code

    def get_date(self):
        return self.date

    def get_openingPrice(self):
        return self.openingPrice 
    
    def get_closingPrice(self):
        return self.closingPrice 

    def get_highest(self):
        return self.highest

    def get_lowest(self):
        return self.lowest

    def get_volume(self):
        return self.volume

    def get_code(self):
        return self.code
        


from enum import Enum

class ExecutionType(Enum):
    Buy='Buy'
    Sell='Sell'
    Short_Sell='Short_Sell'
    Short_Cover='Short_Cover'
    Cancel='Cancel'
    Exit='Exit'

class OrderStatus(Enum):
    Set='Set'
    Submitted='Submitted'
    Partial='Partial'
    Completed='Completed'
    Canceled='Canceled'
    Expired="Expired"
    Declined='Declined'
    Margin="Margin"
    Triggered='Triggered'




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

class Event(Enum):
    Record_result='Record_result'
    Data_cleaned='Data_cleaned'
    Info_updated='Info_updated'
    Signal_appear='Signal_appear'
    submit_order='submit_order'





import sys # this module in python provides variables to maniupulate different parts of the python runtime environments
from src.logger import logging

# this below is for error message detail : when exception arises I will push this on custom message
def error_messsage_detail(error, error_detail:sys):
    
    _,_,exc_tb = error_detail.exc_info()
    # on which file/line the exception has occured will be stored on exc_tb variable
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message
    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)   # inherites error message from error_message_details
        self.error_message = error_messsage_detail(error_message, error_detail = error_detail )
        
    def __str__(self):
        return self.error_message
    
    
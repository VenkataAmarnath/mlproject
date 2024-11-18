import sys  # provides func and variables that are used to manipulate diff parts of python runtime environment
import os
from src.logger import logging



def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()  # exc_tb give info:filename, line number of error
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_number=exc_tb.tb_lineno
    

    error_message=f"Error in Python script: filename-{file_name} line number-{line_number} error message-{str(error)}"

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) # since inheriting from Exception class
        self.error_message=error_message_details(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message



"""
if __name__=='__main__':
    try:
        a=1/0
    except Exception as e:
        logging.info("Divided by zero")
        raise CustomException(e,sys)
"""
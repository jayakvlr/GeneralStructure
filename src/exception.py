
import sys
import logging
def error_message_details(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    filename=exc_tb.tb_frame.f_code.co_filename
    line_number=exc_tb.tb_lineno
    error_message="Error occured in python script name [{0}] at line number [{1}] with error message [{2}]"\
        .format(filename,line_number,str(error))
    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_details)

    def __str__(self):
        return self.error_message

"""if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divided by zero")
        raise CustomException(e,sys)"""

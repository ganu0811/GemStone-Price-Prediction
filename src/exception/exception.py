import sys


class CustomException(Exception):
    def __init__(self,error_message, error_details:sys):
        self.error_message = error_message
        _,_,exc_tb=error_details.exc_info()
        # exc_info is execution information of the current thread
        #  exc_tb is the traceback object
        
        self.line_number = exc_tb.tb_line_number
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        
    
    def __str__(self):
        return "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(self.file_name,self.line_number,self.error_message)


if __name__ == '__main__':
    try:
        a=1/0

    except Exception as e:
        raise CustomException(e,sys)
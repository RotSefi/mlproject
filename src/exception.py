import sys


def error_message_detail(error):
    _, _, exc_tb = sys.exc_info()
    if exc_tb is None:
        return f"Error: {error} (no traceback available)"
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = (
        "Error occured in Python script name: {0}, line: {1}, message: {2}".format(
            file_name, exc_tb.tb_lineno, str(error)
        )
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message)

    def __str__(self):
        return self.error_message

import re
from datetime import datetime

def check_date_format(date_string) -> datetime:
    """
    Check if the input string is in the format of "dd-mm-yyyy" and return datetime object
    """
    date_format = re.compile(r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[012])-(19|20)\d\d$')
    match = date_format.match(date_string)
    if match:
        date_obj = datetime.strptime(date_string, "%d-%m-%Y")
        return date_obj
    



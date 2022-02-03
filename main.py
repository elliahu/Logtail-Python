# This is an example project of Logtail python integration
# This project shocases how to use Logtail in your python projects
# For more infromation please visit https://github.com/elliahu/Logtail-Python

# SETUP

# Import Logtail client library and deault logging library
from logtail import LogtailHandler
import logging
import sys

# Check for program arguments
if len(sys.argv) != 2:
    print("Program requires source token as an argument, run the program as followed\npython main.py <source-token>");
    sys.exit();

# Create handler
handler = LogtailHandler(source_token=sys.argv[1])

# Create logger
logger = logging.getLogger(__name__)
logger.handlers = []
logger.setLevel(logging.DEBUG) # Set minimal log level
logger.addHandler(handler) # asign handler to logger

# LOGGING EXAMPLE
# Following code shocases logger usage

# Send debug log using the debug() method
logger.debug('I am using Logtail!')

# Send info level log about interesting events using the info() method
logger.info('I love Logtail!')

# Send warning level log about warrying events using the warning() method
# You can also add ecustom structured information to the log by passing it as a second argument
logger.warning('Log structured data', extra={
    'item': {
        'url': "https://fictional-store.com/item-123",
        'price': 100.00
    }
})

# Send error level log about errors in runtime using the error() method
logger.error('Oops! An error occured!')

# Send critical level log about critical events in runtume using the critical() method
logger.critical('Its not working, needs to be fixes ASP!')

# Send exception level log about errors in runtime using the exception() method
# Error level log will be sent. Exception info is added to the logging message. 
# This method should only be called from an exception handler.
try:
    nonexisting_function() # Calling nonexisting function
except Exception as Argument:
    logger.exception("Error occurred while calling non-existing function") # Additional info will be added
    # OUTPUT:
    # Error occurred while calling non-existing function
    #Traceback (most recent call last):
    #   File "logtail.py", line 48, in
    #       nonexisting_function()
    #NameError: name 'nonexisting_function' is not defined

print('All done! You can check your logs now.')
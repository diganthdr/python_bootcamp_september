from api.getapi import api as apiapi
from reports.reports import api as reportsapi

apiapi()
reportsapi()

# import logging
# logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

# logging.debug('a debug message')
# logging.info('an info message')
# logging.warning('a warning message')
# logging.error('an error message')
# logging.critical('a critical message')

# fd = open("debug.txt", "w+")

# count = 0
# for x in range(5):
#     count = count +1
#     fd.write(str(count))

# count_apple = count
# fd.write(str(count_apple))
# fd.close()



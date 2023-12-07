import pandas as pd
from logger import Logger
# Use logs when doing any data transforms
# Can also be used as a callback function
# Having log levels and specific messages will make terminal and observers (splunk etc.) cleaner to use
log = Logger(save_file='test.txt')
log.drop_row("123")
log.drop_column('A')
log.appended_row('123 {row info}')
log.appended_column('Column D')
log.transform_summary_histogram()
import matplotlib.pyplot as plt
# Class can be used to save logs, set log levels, and visualize of data transforms
# Counts of data transforms can be compared against existing data sets to see where data may be missing
class Logger:
    def __init__(self, log_level='info', save_file=None):
        self.dropped_rows = 0
        self.appended_rows = 0
        self.dropped_columns = 0
        self.appended_columns = 0
        self.save_file = save_file
        # Let's define levels as info and debug
        if log_level == 'info' or log_level == 'debug':
            self.log_level = log_level
        else:
            print("[WARN] Invalid Log Level. Defaulting to INFO")
            self.log_level = 'info' # Default
            
    def info(self, message): 
        log_message = f"[INFO]  {message}"
        print(log_message)
        if self.save_file:
            with open(self.save_file, 'a') as logfile:
                logfile.write(f'{log_message}\n')
    
    def debug(self, message):
        log_message = f"[DEBUG]  {message}"
        print(log_message)
        if self.save_file:
            with open(self.save_file, 'a') as logfile:
                logfile.write(f'{log_message}\n')

    def drop_row(self, row_info):
        self.debug(f"[DROP] Dropped Row {row_info}")
        self.dropped_rows += 1
    
    def appended_row(self, row_info):
        self.debug(f"[APPEND] Appended Row {row_info}")
        self.appended_rows += 1

    def drop_column(self, column_info):
        self.debug(f"[DROP] Dropped Row {column_info}")
        self.dropped_columns += 1

    def appended_column(self, column_info):
        self.debug(f"[APPEND] Appended Column {column_info}")
        self.appended_columns += 1
    
    def transform_summary(self):
        labels = ['Dropped Rows', 'Appended Rows', 'Dropped Columns']
        counts = [self.dropped_rows, self.appended_rows, self.dropped_columns]
        # Print counts
        for label, count in zip(labels, counts):
            print(f'{label}: {count}')
    
    def transform_summary_histogram(self):
        labels = ['Dropped Rows', 'Appended Rows', 'Dropped Columns']
        counts = [self.dropped_rows, self.appended_rows, self.dropped_columns]
        plt.bar(labels, counts, color=['red', 'green', 'blue'])
        plt.xlabel('Variables')
        plt.ylabel('Counts')
        plt.title('Histogram of Counts')
        plt.show()

import datetime


class Logger:
    def __init__(self, filename):
        self.filename = filename

    def push_log(self, message):
        with open(self.filename, 'a') as file:
            date_str = datetime.datetime.now().strftime("[%b %d %Y %H:%M:%S] ===> ")
            file.write(date_str + message + '\n')
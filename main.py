from datetime import datetime, timedelta
import os.path, time


try:
    if datetime.strptime(time.ctime(os.path.getctime("BabyFile.txt")),"%a %b %d %H:%M:%S %Y") < datetime.now() and datetime.strptime(time.ctime(os.path.getctime("BabyFile.txt")),"%a %b %d %H:%M:%S %Y")+ timedelta(days=10) > datetime.now():
            print("created: %s" % time.ctime(os.path.getctime("BabyFile.txt")))
        ##################
            print("hello world")
        ##################
except:
    print("ERROR")


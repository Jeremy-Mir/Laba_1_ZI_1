import zipfile
from datetime import datetime, timedelta
import os.path, time
from zipfile import ZipFile



if os.path.exists("test.zip"):
    zip_arh = 'test.zip'
    passwd = '123'
    with ZipFile(zip_arh) as zf:
        zf.extractall(pwd=bytes(passwd, 'utf-8'))
        zf.write('BabyFil e.txt')
        text = zf.read(f'BabyFile.txt', pwd=bytes(passwd, 'utf-8')).decode()

    if text =="123456":
        if datetime.strptime(time.ctime(os.path.getctime("BabyFile.txt")),"%a %b %d %H:%M:%S %Y") < datetime.now() and datetime.strptime(time.ctime(os.path.getctime("BabyFile.txt")), "%a %b %d %H:%M:%S %Y") + timedelta(days=10) > datetime.now():
            print("created: %s" % time.ctime(os.path.getctime("BabyFile.txt")))
            ##################
            print("hello world")
            ##################
        else:
            print("ERROR3")
    else:
        print("ERROR2")
    zf.close()
else:
    print("ERROR1")



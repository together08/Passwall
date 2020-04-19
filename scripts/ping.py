import os

def ping_baidu():
    global rusult
    run = "ping baidu.com"
    rusult = os.system(run)


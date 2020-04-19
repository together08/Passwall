import base64
import requests
import wget

# 下载订阅URL的文件，并重命名
sub_url = ""
myfile = requests.get(sub_url)



decoded_url = ""
decoded_url = base64.b64decode(url).decode("utf-8")


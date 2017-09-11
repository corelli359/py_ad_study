# -*- coding: utf-8 -*-
import requests

url = "http://salescloud.cfldcn.com:666/api/House/GetDetail"

headers = {
    'host': "salescloud.cfldcn.com:666",
    'content-length': "103",
    'dzkptoken': "ozJ7Uxs+CPaWxnpNrB3lkje/kZjzC/8YmjqM4Km5Zz/KWMHuumtZA/MNQlO+miyeVtB/RGiYYAfMNbjbWXGzTRMHMpcN+y9bZXd4pZT0jQ6Z9CMlx0hZmUZlic88YSaS",
    'origin': "http://salescloud.cfldcn.com",
    'user-agent': "Mozilla/5.0 (Linux; Android 6.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    'content-type': 'application/json',
    'accept': "application/json, text/javascript, */*; q=0.01",
    'dzkpwx': "oSag30QVHqoVcfxh70gQyPkKwMU0",
    'referer': "http://salescloud.cfldcn.com/house/HouseDetail?activeguid=77465832-41d9-0140-af1e-eaa255468507&RoomGuid=6e0f03bf-0050-e711-80c2-288023a71bc9",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,en-US;q=0.8",
}

payload = {
    "activeguid": "77465832-41d9-0140-af1e-eaa255468507", "roomguid": "6e0f03bf-0050-e711-80c2-288023a71bc9"
}
response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

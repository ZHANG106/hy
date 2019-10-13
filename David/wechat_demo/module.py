import requests

data = {
    "button": [
        {
            "name": "lol",
            "type": "view",
            "url": "http://www.soso.com/"
        }
    ]
}

token = '26_h8UoG68HI8ZPIQ3ku__wbcC8Gv__nrtcS6tOOiMs6EB2D4vgJfmlTYy2lmnHc09wHc6hhEzs427etz2YbVbCvFUkHs5LFUPQHskVycKFBf7CSDUAsbFNlAMguVW0o_sGaDFk6sUjqWuyhSWyVSGaADALIW'
url = r'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s' % token
try:
    res = requests.post(url=url, data=data)
    print(res.json())
except Exception as e:
    print(repr(e))

#-*-coding:utf-8-*-

import requests


y = "美国潮牌Dickies帝客男士休闲双肩包 79元包邮 https://u.jd.com/PtCzhn 包的价格还可以  就是需要拼购"

headers = {
    'Host' : 'qwd.jd.com',
    'User-Agent' : 'jxj/2.1.5',
    'Cookie' : ' 你的cookie'
}

url = "https://qwd.jd.com/cps/zl?content=" + y + "&shareSource=1_2_1"

r =  requests.get(url, headers=headers)

print(r.json().get('content'))

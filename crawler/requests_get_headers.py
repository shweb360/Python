#response查看response编码
import requests
url='https://www.baidu.com'
k=input("请输入关键字：").strip()
response=requests.get(
    url=url,
    #请求头
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
    },
    #请求参数
    params={'wd':k},
    #请求携带cookie信息
    cookies={
        'user_session':'wGMHFJKgDcmRIVvcA14_Wrt_3xaUyJNsBnPbYzEL6L0bHcfc'
    },
    
    
)
#查看网页编码
print(response.encoding)
#查看状态码
print(response.status_code)
with open('a.html','w',encoding='utf-8') as f:
    f.write(response.text)
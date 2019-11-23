#request发送GET请求
import requests

resp=requests.get('http://www.baidu.com/')
# print(resp.text)
# print(resp.content)
# print(resp.cookies)
# print(resp.status_code)
# print(resp.url)
print(resp.headers)
print(resp.history)
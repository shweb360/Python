import requests
respose=requests.get('http://www.cnblogs.com/sss4/')
print(respose.text)  #显示文本内容
print(respose.content) #显示二进制内容（比如爬 图片 或视频需要）
print(respose.status_code) #返回的状态码
print(respose.headers) #获取响应头
print(respose.cookies) #获取服务端响应的cokies信息
print(respose.cookies.get_dict()) #获取字典形式的cokies信息
print(respose.cookies.items()) #获取列表类型的cookis信息
print(respose.url) #获取请求的URLhttp://www.cnblogs.com/sss4/
print(respose.history)#获取跳转前的url
print(respose.json()) #获取json数据
respose.encoding='gbk'#设置 requests模块的
#requests发送POST请求
# POST请求：用户先server端提交上传数据一般会使用POST请求
# POST请求的特点：
'''
 *有请求体，数据保存在请求体中
 *上传提交的数据无上限
 *请求体中如果存在中文，会使用URL编码！
 *requests.post()用法与requests.get()完全一致，
    特殊的是requests.post()有一个data参数，
    用来存放请求体数据，也就是POST请求的请求体；
'''


#模拟浏览器登陆github
import requests
import re

#访问登陆页面
rep=requests.get(
    url="https://www.github.com",
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'},
)
authenticity_token=re.findall(r'name="authenticity_token".*?value="(.*?)"',rep.text,re.S)[0]
# print(r1.cookies.items()) #获取元祖类型的cookies信息
# print(r1.cookies.get_dict())#获取字典类型的cokies信息
cookies=rep.cookies.get_dict()

req=requests.post(
    url='https://github.com/session',
    data={
    'commit':'Sign in',
    'utf8':'✓',
    'authenticity_token':authenticity_token,
    'login':'13220198866@163.com',
    'password':'123.com'
    },
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'},
    cookies=cookies
)

#访问设置个人主页
cookies2=req.cookies.get_dict() #获取登录页面返回的cokies信息
r3=requests.get('https://github.com/settings/emails',cookies=cookies2)

print('13220198866@163.com' in r3.text)


#如果需要向server端传说json数据，必须设置 content-ype:application/json,并且用data传值, 否则服务端取不到值
requests.post(url='',
              data={'':1,},
              headers={
                  'content-type':'application/json'
})



#来源：https://www.cnblogs.com/sss4/p/7813379.html

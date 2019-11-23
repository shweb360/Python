#列表
users=['wushang','hanjuan','xinyue','xiaoming','admin','baode']
for user in users:
    print(user)

#元组
goods=(11,22,33)
for good in goods:
    print(good)

#字典
dics={"name":"wushuang","age":"q20","atel":"t13671524058"}
for name,value in dics.items():
    print(value.title())

#对数字列表执行简单的统计计算
digits=[1,2,3,4,5,6,7,8,9]
squares=[value**2 for value in range(1,10)]
print(squares)

#遍历切片
players=['jack','tom','michael','eli']
my_player=players[:2]
print(my_player)
my_player2=players[:]
print(my_player2)

#先创建一个空字典
mydic={}
mydic["name"]="wu"
mydic["age"]=19
print(mydic)

del mydic['age']
print(mydic)

user_0={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi'
}

for key,value in user_0.items():
    print("\nKey:"+key)
    print("\nvalue："+value)    


#嵌套
alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

wxrs=[]
for wxr in range(30):
    new_wxr={'color':'green','points':5,'speed':'fast'}
    wxrs.append(new_wxr)

for wxr in wxrs[:5]:
    print(wxr)


#在字典中存储列表
ss={
    'crust':'thick',
    'toppings':['mushroom','extra cheese'],
}
#在字典中存储字典
users={
    'aelnstein':{
        'first':'albert',
        'last':'einstein',
        'location':'priceton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    }
}
for username,user_info in users.items():
    fullname=user_info['first']+user_info['last']
    location=user_info['location']
    print('Fullname:'+fullname)
    print('location:'+location)
    print('\n')

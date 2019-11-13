
#1、读取文件
f=open('F:/03学习区/13Python/02Demo/教程地址.txt','r')
content=f.read();
print(content);
f.close()

#2、写入文件
f=open('F:/03学习区/13Python/02Demo/教程地址.txt','w')
content=f.write('wushuang');
print(content);
f.close()
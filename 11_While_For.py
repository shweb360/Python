#while 循环
#实例使用了 while 来计算 1 到 100 的总和：
counter=1
sum=0
while counter<=100:
	sum=sum+counter
	counter+=1
print("1到 %d 之和为:%d" %(counter,sum))


#fo循环
sum2=0
for a in range(101):
	sum2=sum2+a
print(sum2)

print("------------------")
languages=["C","C++","Perl","Python"]
for x in languages:
	print(x)

print("------------------")

for letter in "Runoob":
	if letter=='b':
		break
	print("当前字母为：",letter)

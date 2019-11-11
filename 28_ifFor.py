#if Statements
x=int(input("Please enter an integer:"))
if x <0:
	x=0
	print("Negative changed to zero")
elif x==0:
	print("zeor")
	
#for Statements
words=['cat','window','defenestrate']
for w in words:
	print(w,len(w))
	
for i in range(5):
	print(i)

n=100
sum=0
counter=1
while counter<=n:
	sum+=counter
	counter=counter+1
print("1 到 %d 之和为: %d" % (n,sum))	
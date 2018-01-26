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
import json 
filename="F:\\03学习区\\13Python\\02Demo\\python\\pi_digits.txt"
numbers=[1,2,3,4,5]

#存储数据json.dump()
with open(filename,'w') as file_object:
    json.dump(numbers,file_object)

#读取数据json.load()
with open(filename) as file_object:
    numbers2=json.load(file_object)
print(numbers2)    
#Python3 元组
#Python 的元组与列表类似，不同之处在于元组的元素不能修改。
#元组使用小括号，列表使用方括号。
#元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
tup1=("Google","Runoob",1997,2000);
tup2=(1,2,3,4,5);
tup3="a","b","c","d";
print(tup1);
print(tup2);
print(tup3);

print(type(tup1));

#元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
tup4=(50)
type(tup4)


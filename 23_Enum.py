#Enum可以把一组相关常量定义在一个class中，
#且class不可变，而且成员可以直接比较。
from enum import Enum
Month=Enum("Month",('Jan','Feb','Mar','Apr'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
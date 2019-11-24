file_name="F:\\03学习区\\13Python\\02Demo\\python\\pi_digits.txt"
with open(file_name) as file_object:
    # contents=file_object.read()
    # 读取文件中的每一行
    #lines=file_object.readlines()
    # print(contents)
    #逐行读取
    for line in file_object:
        print(line.rstrip())

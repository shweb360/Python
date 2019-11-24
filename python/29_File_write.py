file_name="F:\\03学习区\\13Python\\02Demo\\python\\pi_digits.txt"

#????
with open(file_name,'w') as file_object:
    file_object.write('I love programming\n')
    file_object.write('I love python\n')
    file_object.write('I love C# \n')

#????
with open(file_name,'a') as file_object:
    file_object.write("I love swimming")
    
with open(file_name) as file_object:   
    for line in file_object:
        print(line.rstrip())
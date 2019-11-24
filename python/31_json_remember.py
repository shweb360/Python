import json 
filename="F:\\03学习区\\13Python\\02Demo\\python\\pi_digits.txt"

username=input("What is your name?\n")
with open(filename,'w') as file_object:
    json.dump(username,file_object)
    print("We will remember you when you come back," + username)
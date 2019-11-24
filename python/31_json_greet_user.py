import json 
filename="F:\\03学习区\\13Python\\02Demo\\python\\pi_digits.txt"

with open(filename) as file_object:
    username=json.load(file_object)
    print("Wecom back " + username)
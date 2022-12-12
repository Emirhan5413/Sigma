file = open("data.py","w")
file.write("Name = 'Emirhan'\nSurname = 'Unlu'\nGender = 'Man'\nUsername = 'Arcehmi'\nJob = 'Computer Engineer'")

file.close

file = open("data.py", "r")

x = file.readlines()

dictionary = {}

dictionary["Name"] = x[0].split("=")[1].split("\n")[0]
dictionary["Surname"] = x[1].split("=")[1].split("\n")[0]
dictionary["Gender"] = x[2].split("=")[1].split("\n")[0]
dictionary["Username"] = x[3].split("=")[1].split("\n")[0]
dictionary["Job"] = x[4].split("=")[1].split("\n")[0]

print(dictionary)

file.close


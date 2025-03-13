
employee_file = open("Employees.txt", "r") #"w" = write, "a" = append, "r+" = read and write
#print(employee_file.readable()) #returns True or False
#print(employee_file.read()) #returns file content
#print(employee_file.readlines()[1]) #[] returns the index

for employee in employee_file.readlines():
    print(employee)

employee_file.close()

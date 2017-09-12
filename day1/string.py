name = input('your name:').strip("o")
Age = input('Age:').strip()
Job = input('job:').strip()

# print('Information of: ' + name + '\nYour name: ' + name + '\nAge: ' + Age + '\nJob: ' + Job )

msg = '''
Inofrmation of: %s
     Your name: %s
           Age: %s
           Job: %s
''' %(name, name, Age, Job)

print(msg)

# print('Inofrmation of: %s\nYour name: %s\nAge: %s\nJob: %s' %(name, name, Age, Job))

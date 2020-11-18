
# Add an if statement with elifs to check user
# If they are Student output 'Student Access'
# If they are Teacher output 'Teacher Access'
# If they are Headteacher output 'Headteacher Access'
# Otherwise output 'Access Denied' 

print ("Enter Student, Teacher or Headteacher")

user = input("if you are a student enter 's', a teacher enter 't' if a headteacher enter 'h': ")

if user == 's':
    print("student access")
elif user == 't':
    print("teacher access")
elif user == 'h':
    print("head teacher access")
    

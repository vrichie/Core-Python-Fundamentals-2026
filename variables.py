"""
category    type    example
string      str     "james" == 'james'
Numbers     int     3
            float   3.40
            complex 2j
sequence    list [1,2,3,4]
            tuple (1,2,3)
map         dict {"name":"james","age":48}
boolean     bool True/False
 """

#variables
_var="name"
firstName = "James" ##camelCase
FirstName = None ##PascalCase
first_name ="james" ## snake case

grade ='A'
isActive=True
num=3.5
# print(first_name+str(num))

# casting means converting from one data type to another data types
age=str(36)
num1=int('38')
print(type(num1))
print(bool(0))
a,b,c='hey',45,False
print(a,b,c)
msg = '''---------ywb----------
Name : ywb
Age : 18
job : Teacher
Hobby : no
-------------------'''
print(msg)

# 公共模板
name = input("name : :")
age = input("age :")
job = input("job :")
hobby = input("hobby :")
# % 占位替换符
msg_template = '''------------%s-------
Name : %s
Age : %s
job : %s
Hobby : %s
-------------------''' % (name, name, age, job, hobby)
print(msg_template)

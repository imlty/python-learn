username = input('用户名 :')
password = input('密码 :')
code = 'qwer'
your_code = input('验证码')
if your_code == code:
   if username == 'alex' and password == '123':
       print('登录成功')
   else:
       print('用户名或密码错误')
else:
    print('验证错误')
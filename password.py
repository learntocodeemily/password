i = 0
while i < 3:
    password = input('请输入你的密码：')
    if password == 'a123456':
        print('登入成功!') 
        break   
    else:
        print('密码错误！还有', 2-i, '次机会')
        i = i + 1


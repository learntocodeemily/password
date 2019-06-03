password = 'a123456'
i = 0
while i < 3:
    pwd = input('请输入你的密码：')
    if pwd == password:
        print('登入成功!') 
        break   
    else:
        print('密码错误！还有', 2-i, '次机会')
        i = i + 1


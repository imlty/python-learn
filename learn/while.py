# 基本结构
'''
while 条件
    循环体
'''

# 原理
count = 1
flag = True
# while flag:
#     print('不一样 ')
#     print(count)
#     count = count + 1
#     if count == 100:
#         flag = False

sum = 0
while count <= 100:
    sum = sum + count
    count = count + 1

print(sum)

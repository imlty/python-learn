# 1. 初识
print("the first python script!!")
print("the first python script!!")
print("the first python script!!")

# 2.

# 3. 速览
# this is the first comment
sapm = 1  # this is the second comment
# is the third
text = "# 这是注释嘛"
print(sapm)
print(text)

# 4. 循环
x = int(input("input your number"))

if x < 0:
    print('your number is < 0')
elif x == 0:
    print('your number is == 0')
else:
    print("more")

words = ['cat', 'windows', 'java']
for w in words:
    print(w, len(w))

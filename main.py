
# 별찍기
for i in range(1,6):
    print("*"*i)

# 역전시키기
for i in range(1, 6):
    print(' ' * (5 - i) + '*' * i)

#피라미드 만들기
for i in range(1, 6):
    print(' ' * (5 - i) + '*' * (2 * i - 1))

#다이아몬드 만들기
for i in range(1, 6):
    print(' ' * (5 - i) + '*' * (2 * i - 1))
    if 5 == i:
     for j in range(4, 0, -1):
        print(' ' * (5 - j) + '*' * (2 * j - 1))
    for i in range(1, 10):
        result = ' '

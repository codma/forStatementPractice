
# 별찍기
for i in range(1,6):
    print("*"*i)

# 역전시키기
list=[5,4,3,2,1]
for i in list:
    print(" "*i,"*"*(6-i))

#피라미드 만들기
list=[5,4,3,2,1]
for i in list:
    print("  "*i," *"*(6-i),"* "*(6-i))
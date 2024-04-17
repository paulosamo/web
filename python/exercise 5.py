
math = int(input("math: "))
eng = int(input("eng: "))
kis = int(input("kis: "))
bio = int(input("bio: "))
chem = int(input("chem: "))
sum = math + eng + kis + bio + chem

average = sum/5

print(average)

if average < 0 or average > 100:
    print("invalid number")

if 0<= average <= 30:
    print("E")

elif 40<= average <= 50:
    print("D")

elif 51<= average <=60:
    print("C")

elif 61<= average <=70:
    print("B")

elif 71>= average <100:
    print("A")
else:
    print("invalid number")

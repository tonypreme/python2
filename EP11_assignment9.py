# ค้นหาจำนวนตัวอักษรและนับจำนวนสมาชิกใน ชนิดข้อมูล list

message=["aa","ab","ac","aac","ccaa","abc"]
result=[]

for item in message:
    result.append(item.count("a"))
    # .count คือการนับจำนวนตัวอักษร ** นับตัวอักษรเฉพาะ a
print(result)



# Arbitrary Arguments (*args) ระบุแบบไม่จำกัด

def add(x,y,z):
    print(x+y+z)

# add(10,20) # โครงสร้างกำหนดไว้ต้องส่งค่าไปทั้งหมด 3 ค่า 
add(10,20,5)

# -----------------------------------------------
# กำหนดแบบ ไม่ต้องกำหนดจำนวนค่าด้านใน
# Arguments (*args)

def number(*agrs):
    print(agrs)

number()
number(10)
number(10,50)
number(10,12,50)
number(10,20,30,50,"tony")
# สามารถโยนข้อมูลลงไปได้เรื่อยๆ 

# -----------------------------------------------
# ต้องการหาค่า 

def number2(*agrs):
    print(agrs[0]+agrs[1])

number2(10,20)
   

def number3(*agrs):
    sum=0
    for i in range(len(agrs)):
        sum+=agrs[i]
        print(sum)

number3(200,300)
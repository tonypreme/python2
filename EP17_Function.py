# ฟังก์ชั่น ( Function )

'''
https://www.youtube.com/watch?v=2_TK8JYJiwQ&t=18397s&ab_channel=KongRuksiam
ฟังในนี้เวลา 5:06:40 
'''
# สาเหตุที่เราต้องเขียน function

a,b,c,d = 10,23,40,50

# คำสั่งที่มันซ้ำๆ 

if a%2 == 0:
    print("เลขคู่")
else :
    print("เลขคี่")

if b%2 == 0:
    print("เลขคู่")
else :
    print("เลขคี่")

if c%2 == 0:
    print("เลขคู่")
else :
    print("เลขคี่")

if d%2 == 0:
    print("เลขคู่")
else :
    print("เลขคี่")

# ------------------------------------

# การส้ราง function และเรียกใช้งาน

'''
โครงสร้าง

def ชื่อฟังก์ชั่น():
    statement 
'''
#สร้าง ฟังก์ชั่น เรียกอีกอย่างว่าโปรแกรมย่อย

def sayhi(): # ชื่อฟังก์ชั่นห้ามซ้ำกัน 
    print("Hello Function")

def sayThailand():
    print("สวัสดี")

def sayEngland():
    print("Hello / Hi")

def add():
    x=3+1
    print(x)


# เรียกใช้งาน ในโปรแกรมหลัก

sayThailand() # การเรียกคือการอ้างอิงไปถึงชื่อที่เราสร้าง 
add()
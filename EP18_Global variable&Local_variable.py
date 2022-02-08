# Global variable และ Local variable

'''
ฟังฟ์ชั่นใช้คู่กับ ตัวแปร
'''

def displayNumber():
    x=10
    print("Hello = ",x,"ใน")


x=20 # ตัวแปรจะแยกกับตัวของฟังก์ชั่นถึงแม้ตัวแปร x จะมี 2 ตัว  
displayNumber()
print("Hello = ",x,"นอก") # จะแยกกับตัวฟังก์ชั่น

# Global variable x นอก function
'''
ตัวโปรแกรมหลัก หรือทุกส่วน สามารถเข้าถึงตัวแปรนี้ได้ 
'''
# Local variable x ใน function
'''
ตัวแปรทำงานส่วนนั้นๆ แล้วจบการทำงานไปเลย
'''

# สรุปคือ Global ตัวแปรด้านนอก ที่สามารถอ้างอิงถึงได้จากทุกที่
# สรุปคือ Local  ตัวแปรด้านในของฟังก์ชั่น ไม่สามารถอ้างอิงถึงได้ ทำงานภายในแค่ function

# ------------------------------------
# การส่งค่าเข้ามาในฟังก์ชั่น 

def myData(name,lname): # ใส่พารามิเตอร์ เข้าไปเพื่อสามารถส่งข้อมูลเข้าไปในฟังก์ชั่น
    print("ชื่อ = ",name,lname)

# พอใน ฟังก์ชั่นมี 2 ค่าแล้วต้องใส่ข้อมูลให้ครบไม่งั้นจะไม่ทำงาน

myData("tony","ja")
myData("maew","jok")
myData(3,1.2)
# Recursive Funtion

'''
ฟังก์ชั่นเรียก ฟังก์ชั่นของตัวเอง 
โดยมีการทำซ้ำไปเรื่อยๆ
เหมาะสำหรับ โปรแกรมที่ซับซ้อน 

ค่าแฟกทอเรียล = 4! 
หรือการจัดเรียงข้อมูล
หรือ ยกตัวอย่างป้ายไฟ วนไฟซ้ำๆ เรื่อยๆ 
'''
# EX
# อันดับแรกหาจุดวนซ้ำ ทำเงื่อนไข
# สุดท้าย หาจุดออกจากฟังก์ชั่น (return)

def a():
    print("A")
    a() # เรียกฟังก์ชั่นเดิม เพื่อวนเรียกซ้ำ
    # เหมือนทำ loop แต่ไม่มีืั้สิ้นสุด 
# a() 

# ------------------------------------------
# ทำ 1-5 โดย ไม่ใช้ คำสั่ง loop 

def addNumber(number1):
    if number1==5:
        return # กำหนดจุดออก ถ้า + จนถึง 5 จะ return ออกมา
        # เป็นค่าว่าง 
    print(number1+1) # 0
    number1+=1 # +1 
    addNumber(number1)

def summation(number):
    if number==1:
        return number
    else :
        return number+summation(number-1)

x=summation(5) # ? = 5 + 4 + 3 ... => + 1 
print(x)
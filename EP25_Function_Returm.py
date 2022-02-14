# Function Returm

'''
1. ไม่มีการรับค่าและส่งค่า
def name():

2. มีการส่งค่าเข้าไปทำงาน
def name(a,b):

3. รับค่าเข้าไปทำงาน และส่งออกมา
def name(a,b):
    return a+b

4. ไม่มีการรับค่าเข้ามา แต่ส่งค่าออกไป

'''

# def add(a,b):
#     return a+b

# x=add(10,20)
# print(x)
    
# def showNumber():
#     return 500

# y=showNumber()
# print(y)
    

def randomNumber(x):
    if x=='100':
        print("ถูกหวย")
        return 1000 
        # เป็นตัวเลขที่ส่งกลับมาหลังจากใส่ค่าเข้าไปสามารถนำไปใช้งานต่อได้
    else:
        print('ไม่ถูกหวย')
        return 0

money=randomNumber('100')
x=300 # <= ยอดหนี้ ยกตัวอย่าง
result=money-x
print("ยอดหนี้ = " ,x)
print("เงินรางวัล = " ,money)
print("เงินคงเหลือ = " ,result)
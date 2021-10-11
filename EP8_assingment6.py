# กลุ่มสมาชิกเลขยำกกำลัง 

number=[1,2,3,4,5,6,7]

# เคสที่ 1 ปกติ

print("ก่อนยกกำลัง :",number)
for i in range(len(number)): # len() หาจำนวนของกลุ่มข้อมูล
    number[i]=number[i]**2 # ** คือยกกำลัง 2 
print("ยกกำลัง 2 แล้ว :",number)

# เคสที่ 2 แบบลดรูป 
number=[x*x for x in number] # ใช้ loop for ใน list ได้
print(number)

'''
ดึงข้อมูลทีละตัวจาก number 
นำตัวเลขแต่ละตัวมา * กันเอง หรือ **2 ยกกำลัง 2 
และเก็บข้อมูลไว้ที่ number 
'''